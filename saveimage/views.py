from django.shortcuts import render, redirect
from .forms import LoadImageForm, ResizeImageForm


def form_upload(request):
    if request.method == 'POST':
        form_load = LoadImageForm(request.POST, request.FILES)
        if form_load.is_valid():
            form_load.save()
            return redirect('saveimage/resize_image.html')
    else:
        form_load = LoadImageForm()
    return render(request, 'saveimage/form_upload.html', {
        'form_load': LoadImageForm,
    })


def form_resize(request):
    if request.method == 'POST':
        form_resize = ResizeImageForm(request.POST, request.FILES)
        if form_resize.is_valid():
            #form_resize.save()
            return redirect('home')
    else:
        form_resize = ResizeImageForm()
    return render(request, 'saveimage/resize_image.html', {
        'form_resize': ResizeImageForm,
    })
