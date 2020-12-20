from django import forms
from .models import Image


class LoadImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('url_image', 'load_image',)


class ResizeImageForm (forms.ModelForm):
    class Meta:
        model = Image
        fields = ('width', 'length',)


