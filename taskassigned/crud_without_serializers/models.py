from django.db import models

# Create your models here.
class WWE(models.Model):
    p_name = models.CharField(max_length=100, default=None)
    p_lock = models.CharField(max_length=100, default=None)
    p_chest = models.IntegerField(blank=True,null=True)
    p_height = models.IntegerField(null=True,blank=True)
    p_color = models.CharField(max_length=100,null=True, default=None)