from django.shortcuts import render
from django.http import HttpResponse
from newtask.models import users
from newtask.serializers import userSerializer
from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status


# Create your views here.

class user_details(APIView):
    def get(self,request):
    
        # todo = users.objects.all()
        # todo = users(first_name = "Aman",last_name = "gusain", age = 22, email_id = "aman@gamil.com",location = "delhi 110084")
        # todo.save()
        # return HttpResponse(todo.id)
        
        todo = users.objects.get(pk=1)
        d = userSerializer(todo)
        d.data
        return Response({"data":d.data})

