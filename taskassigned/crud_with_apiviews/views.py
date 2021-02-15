from django.shortcuts import render
from rest_framework.views import APIView
from crud_with_apiviews.models import userlogin
from rest_framework.response import Response
from crud_with_apiviews.serializers import infoSerializer
from rest_framework import status
# from datetime import datetime

# Create your views here

class detailslist(APIView):
    
    def get(self, request):
        
        email_id = request.GET.get('email_id')
        id = request.GET.get('id')
        
        if id:
            li = userlogin.objects.get(id=id)
            serializer = infoSerializer(li)
            return Response(serializer.data)

        elif email_id:
            li = userlogin.objects.get(email_id=email_id)
            serializer = infoSerializer(li)
            return Response(serializer.data)

        else:
            li = userlogin.objects.all()
            serializer = infoSerializer(li,many=True)
            return Response(serializer.data)

    
    def post(self,request):

        serializer = infoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    

    def put(self,request):
        
        id = request.GET.get('id')
        if id:
            li = userlogin.objects.get(id=id)
            serializer = infoSerializer(li, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("please enter a valid id")

        
    def delete(self, request):
        
        email_id = request.GET.get('email_id')
        id = request.GET.get('id')
        if id:
            deleteUserData = userlogin.objects.get(id=id)
            deleteUserData.delete()

        elif email_id:
            deleteUserData = userlogin.objects.get(email_id=email_id)
            deleteUserData.delete()