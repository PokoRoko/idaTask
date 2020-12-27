from django import forms
from .models import Image


class LoadImageForm(forms.ModelForm):
    def clean(self):
        """Переопределяем clean для вывода ошибке при пустых или двух заполненых полях"""
        url_image = self.cleaned_data.get('url_image')
        load_image = self.cleaned_data.get('load_image')
        if (not load_image and not url_image) or (load_image and url_image):
            raise forms.ValidationError('Выберете один метод загрузки изображения!')
        return self.cleaned_data

    class Meta:
        model = Image
        fields = ('url_image', 'load_image',)


class ResizeImageForm(forms.ModelForm):
    def clean(self):
        """Переопределяем clean для вывода ошибке при пустых или двух заполненых полях"""
        width = self.cleaned_data.get('width')
        length = self.cleaned_data.get('length')
        if width == 0 and length == 0:
            raise forms.ValidationError('Установите минимум одно значение!')
        return self.cleaned_data

    class Meta:
        model = Image
        fields = ('width', 'length',)


