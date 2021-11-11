from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework import status
from .models import Bond
from .serializers import BondSerializer
import requests

class HelloWorld(APIView):
    def get(self, request):
        return Response("Bond API")

@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class BondView(APIView):
    def get(self, request):
        filters = request.GET.dict()
        bonds = Bond.objects.all().filter(userid=request.user.id)

        serializer = BondSerializer(bonds, many=True)
        return Response(serializer.data)


    def post(self, request):
        try:
            lei = request.data['lei']
        except:
            return Response("Lei is not available", status=status.HTTP_400_BAD_REQUEST)
        
        
        try:
            resp =  requests.get(f"https://api.gleif.org/api/v1/lei-records/{lei}")
            legal_name = resp.json()["data"]["attributes"]["entity"]["legalName"]["name"]
        except:
            return Response("Lei id not found in the database", status=status.HTTP_400_BAD_REQUEST)
        
        request.data["userid"] = request.user.id
        request.data['legal_name'] = legal_name

        serializer = BondSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)