from django import forms
from .models import FileUpload


class FileUpload(forms.ModelForm):
    class Meta:
        model = FileUpload
        fields = ['file']
