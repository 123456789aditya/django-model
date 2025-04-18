from django.db import models

# Create your models here.

class profile(models.Model):
    name=models.CharField(max_length=70)
    email=models.EmailField(max_length=240)
    city=models.CharField(max_length=100)
    roll=models.IntegerField(max_length=70)
