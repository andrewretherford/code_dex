from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Record(models.Model):
   owner = models.ForeignKey(User, on_delete=models.CASCADE)
   category = models.CharField(max_length=50)
   file = models.FileField()