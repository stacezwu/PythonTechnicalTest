from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework import generics, status
from .models import Bond
from .serializers import BondSerializer
import requests
import logging

@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class HelloWorld(APIView):
    def get(self, request):
        return Response("Hello World!")

# class UserCreate(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = (AllowAny, )

# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
class BondView(APIView):
# @api_view(['GET'])
    def get(self, request):
        # if request.method == 'GET':
        # bonds = Bond.objects.all()
        filters = request.GET.dict()
        bonds = Bond.objects.all().filter(userid=request.user.id)

        serializer = BondSerializer(bonds, many=True)
        return Response(serializer.data)


    # @api_view(['POST'])
    def post(self, request):
        try:
            lei = request.data['lei']
        except:
            return Response("Lei is not available", status=status.HTTP_400_BAD_REQUEST)
        
        resp =  requests.get(f"https://api.gleif.org/api/v1/lei-records/{lei}")
        legal_name = resp.json()["data"]["attributes"]["entity"]["legalName"]["name"]
        
        request.data["userid"] = request.user.id
        request.data['legal_name'] = legal_name

        serializer = BondSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)