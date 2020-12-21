from django.shortcuts import render, redirect
from .forms import LoadImageForm, ResizeImageForm
from .models import Image
import os
from pathlib import Path

def list_image(request):
    images = Image.objects.order_by('id')  # Получаем все обьекты из модели
    return render(request, 'saveimage/list_image.html', {"images": images})


def form_upload(request):
    if request.method == 'POST':
        form_load = LoadImageForm(request.POST, request.FILES)
        formresize = ResizeImageForm(request.POST, request.FILES)
        if form_load.is_valid():
            form_load.save()
            # adres = os.path.join(Path(__file__).resolve().parent.parent)
            # img_path = form_load.instance.load_image.url
            # img_url = adres+img_path
            #img_url =img_path

            #print('!!!!'+img_url)
            img_url = form_load.instance
            return render(request, 'saveimage/form_resize.html',
                          {'form_resize': ResizeImageForm,
                           'img_url': img_url
                           })
    else:
        form_load = LoadImageForm()

    return render(request, 'saveimage/form_upload.html', {
        'form_load': LoadImageForm,
    })



def form_resize(request):
    if request.method == 'POST':
        formresize = ResizeImageForm(request.POST, request.FILES)
        if formresize.is_valid():
            formresize.save()
            return redirect('home')
    else:
        formresize = ResizeImageForm()
    return render(request, 'saveimage/form_resize.html', {
        'form_resize': ResizeImageForm,
    })
