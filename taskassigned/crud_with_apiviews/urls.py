from django.urls import path, include
from crud_with_apiviews import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns=[
    
    path('',views.detailslist.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
