from crud_with_apiviews import views
from django.urls import path, include

from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns=[
    
    path('task2/',views.detailslist.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
