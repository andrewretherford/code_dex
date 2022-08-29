from django import forms
from django.forms.models import inlineformset_factory
from .models import *

class UploadForm(forms.ModelForm):
   class Meta:
      model = Record
      fields = ('title', 'category', 'file')