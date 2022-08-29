from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

# Create your models here.

class Category(models.Model):
   owner = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE, related_name='category_owner')
   name = models.CharField(null=False, blank=False, max_length=50)

   def __str__(self):
      return self.name

class Record(models.Model):
   owner = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE, related_name='record_owner')
   category = models.ForeignKey(Category, on_delete=models.CASCADE)
   title = models.CharField(max_length=50)
   file = models.FileField(validators=[
      FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'ppt', 'xlsx', 'png', 'jpg'])
   ])

   def __str__(self):
      return self.title