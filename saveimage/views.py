from django.shortcuts import render, redirect
from .forms import LoadImageForm, ResizeImageForm


def form_upload(request):
    if request.method == 'POST':
        form_load = LoadImageForm(request.POST, request.FILES)
        if form_load.is_valid():
            form_load.save()
            #return redirect('saveimage/form_resize.html')
            return render(request, 'saveimage/form_resize.html')

    else:
        form_load = LoadImageForm()
    return render(request, 'saveimage/form_upload.html', {
        'form_load': LoadImageForm,
    })


def form_resize(request):
    if request.method == 'POST':
        formresize = ResizeImageForm(request.POST)
        if formresize.is_valid():
            formresize.save()
            return redirect('home')
    else:
        formresize = ResizeImageForm()
    return render(request, 'saveimage/form_resize.html', {
        'form_resize': ResizeImageForm,
    })
