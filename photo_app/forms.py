from django import forms
from .models.upload import Upload

class ImageForm(forms.ModelForm):
    class Meta:
        model = Upload
        fields = ('name', 'author', 'description', 'image')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'})
        }