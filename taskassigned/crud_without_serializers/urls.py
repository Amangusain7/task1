from django.urls import path, include

from crud_without_serializers import views

urlpatterns=[
    path('',views.wrestling.as_view())
]