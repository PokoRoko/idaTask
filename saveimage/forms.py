from django import forms
from .models import Image


class LoadImageForm(forms.ModelForm):

    def clean(self):

        url_image = self.cleaned_data.get('url_image')
        load_image = self.cleaned_data.get('load_image')
        if (not load_image and not url_image) or (load_image and url_image):
            raise forms.ValidationError('Выберете один метод загрузки изображения!')
        return self.cleaned_data

    class Meta:
        model = Image
        fields = ('url_image', 'load_image',)


class ResizeImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('width', 'length',)
