# from django.contrib import admin
from django.urls import path, include
from newtask import views


urlpatterns = [
    # path('admin/', admin.site.urls), 
    path('',views.user_info),
]