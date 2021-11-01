from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Bond
from .serializers import BondSerializer
import requests
import logging

# class HelloWorld(APIView):
#     def get(self, request):
#         return Response("Hello World!")


@api_view(['GET'])
def get_bond(request):
    # if request.method == 'GET':
    # bonds = Bond.objects.all()
    filters = request.GET.dict()
    bonds = Bond.objects.all().filter(**filters)

    serializer = BondSerializer(bonds, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def post_bond(request):
    try:
        lei = request.data['lei']
    except:
        return Response("Lei is not available", status=status.HTTP_400_BAD_REQUEST)
    
    resp =  requests.get(f"https://api.gleif.org/api/v1/lei-records/{lei}")
    logging.debug(resp.json())
    legal_name = resp.json()["data"]["attributes"]["entity"]["legalName"]["name"]
    
    request.data['legal_name'] = legal_name

    serializer = BondSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)