from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class profile(models.Model):
    name=models.CharField(max_length=70)
    roll=models.IntegerField()
    email=models.EmailField(max_length=200)
    city=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class biodata(models.Model):
    fname=models.CharField(max_length=100)
    roll=models.IntegerField()
    email=models.EmailField(max_length=70)
    city=models.CharField(max_length=70)
    
    def __str__(self):
        return self.fname