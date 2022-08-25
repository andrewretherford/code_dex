from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

# Create your models here.

class Record(models.Model):
   owner = models.ForeignKey(User, on_delete=models.CASCADE, default='1')
   title = models.CharField(max_length=50, default='New Note')
   category = models.CharField(max_length=50)
   file = models.FileField(validators=[
      FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'ppt', 'xlsx', 'png', 'jpg'])
   ])

   def __str__(self):
      return self.title