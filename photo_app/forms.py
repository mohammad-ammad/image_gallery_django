from django import forms
from .models.upload import Upload

class ImageForm(forms.ModelForm):
    class Meta:
        model = Upload
        fields = ['image']