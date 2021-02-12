from django.db import models

# Create your models here.
class users(models.Model):
    first_name = models.CharField(max_length=100, default="")
    last_name = models.CharField(max_length=100, blank=True)
    age = models.IntegerField(null=True,default = None)
    email_id = models.EmailField(max_length=70, unique=True)
    location = models.CharField(max_length=250,default = "")
