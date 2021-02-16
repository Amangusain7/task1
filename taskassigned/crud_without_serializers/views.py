from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from crud_without_serializers.serializers import wweSerializer
from crud_without_serializers.models import WWE
from rest_framework.parsers import JSONParser 
from rest_framework import status

# Create your views here.

class wrestling(APIView):
    
    def get(self,request):
        id = request.GET.get('id')
        if id:
            a = WWE.objects.get(id=id)
            serializer = wweSerializer(a)
            return Response(serializer.data)
        else:
            a = WWE.objects.all()
            serializer = wweSerializer(a,many=True)
            return Response(serializer.data)


    def post(self,request):
        wwe_data = JSONParser().parse(request)
        serializer = wweSerializer(data=wwe_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self,request):
        
        wwe_data = JSONParser().parse(request)
        id = request.GET.get('id')
        if id:
            a = WWE.objects.get(id=id)
            serializer = wweSerializer(a, data = wwe_data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("please enter a valid id")    
    
    
    def delete(self,request):
        
        id = request.GET.get('id')
        if id:
            deletedata = WWE.objects.get(id=id)
            deletedata.delete()
            return Response("CONTENT DELETED")
        else:
            return Response("Cannot delete data without id")

    
