from django.db import models

# Create your models here.
class users(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField(null=True)
    email_id = models.EmailField(max_length=70, null=True, unique=True)
    location = models.TextField()
