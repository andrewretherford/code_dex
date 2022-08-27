from django import forms
from .models import *

class UploadForm(forms.ModelForm):
   class Meta:
      model = Record
      fields = ('title', 'category', 'file')

class CategoryForm(forms.ModelForm):
   class Meta:
      model = Category
      fields = '__all__'