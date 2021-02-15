from django.db import models
# from datetime import date

# Create your models here.
class userlogin(models.Model):
    f_name = models.CharField(max_length=100, default=None)
    l_name = models.CharField(max_length=100, blank=True, null = True,default=None)
    DOB = models.DateField(max_length=10,  null=True, blank=True)
    gender = models.CharField(max_length=100, blank=True)
    email_id = models.EmailField(max_length=70,null=True,unique=True)
    phone_no = models.IntegerField(null=True, default=None)
    password = models.CharField(max_length=100)