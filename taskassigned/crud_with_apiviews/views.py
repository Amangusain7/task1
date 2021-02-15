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
        
        li = userlogin.objects.all()
        serializer = infoSerializer(li,many=True)
        return Response({"info":serializer.data})
        
        # li = userlogin(f_name="aman",l_name="gusain",DOB="1999-2-24",gender="MALE",email_id="aman@gusain",phone_no=80000500011,password="844#abc")
        # li.save()
        # return Response(li.id)

        # li = userlogin.objects.get(pk=4)
        # a = infoSerializer(li)
        # return Response({"data":a.data})

    def post(self,request):
        serializer = infoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def get_object(self, pk):
        try:
            return userlogin.objects.get(pk=pk)
        except userlogin.DoesNotExist:
            raise Http404

    
    def put(self,request,pk):
        li = self.get_object(pk)
        # a = get_object_or_404(userlogin.objects.all(),pk=pk)
        # a = self.get_object(pk)
        # data = request.data.get('a')
        serializer = infoSerializer(li, data=data, partial=True)
        # b = infoSerializer(instance=a, data=request.data)

        if b.is_valid():
            b.save()
            return Response(b.data)
        return Response(b.errors, status=status.HTTP_400_BAD_REQUEST)

        
    def delete(self, request):

        deleteUserData = userlogin.objects.all().delete()
        print(deleteUserData,'@@@@@@@@@@@@@@@@@@@@')
        return Response('DELETED')