from django import forms
from .models import Record

class UploadForm(forms.ModelForm):
   class Meta:
      model = Record
      fields = ('title', 'category', 'file')