from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from crud_without_serializers.serializers import wweSerializer
from crud_without_serializers.models import WWE
from rest_framework import status

# Create your views here.

class wrestling(APIView):
    
    def get(self,request):
        id = request.GET.get('id')
        if id:
            a = WWE.objects.filter(id=id)
            serializer = wweSerializer(a,many=True)
            return Response(serializer.data)
        else:
            a = WWE.objects.all()
            serializer = wweSerializer(a,many=True)
            return Response(serializer.data)


    def post(self,request):
        
        a = WWE.objects.create(
            p_name=request.data.get("p_name"),
            p_chest=request.data.get('p_chest'),
            p_height=request.data.get('p_height'),
            p_color=request.data.get('p_color'),        
            p_lock=request.data.get('p_lock'),
        )
        
        return Response({"status":"create record","record_id":a.id})


       
    def put(self,request):
        
        id = request.GET.get('id')
        if id:
            a = WWE.objects.filter(id=id).update(
            p_name=request.data.get('p_name'),
            p_chest=request.data.get('p_chest'),
            p_height=request.data.get('p_height'),
            p_color=request.data.get('p_color'),
            p_lock=request.data.get('p_lock'),
            )
            return Response({"status":"record updated"})
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

    
