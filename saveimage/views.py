from django.shortcuts import render
from .forms import LoadImageForm, ResizeImageForm
from .models import Image
from django.db.models import Max
from PIL import Image as ImgPil
from idatask.settings import BASE_DIR


def list_image(request):
    images = Image.objects.order_by('-id')  # Получаем все обьекты из модели

    return render(request, 'saveimage/list_image.html', {"images": images})


def form_upload(request):
    """Если в форме отправки есть изображение, обновит и покажет окно для изменения размера"""
    if request.method == 'POST':
        form_load = LoadImageForm(request.POST, request.FILES)
        form_resize = ResizeImageForm(request.POST, request.FILES)
        if form_load.is_valid():
            form_load.save()
            img_url = form_load.instance
            return render(request, 'saveimage/form_upload.html',
                          {'form_resize': ResizeImageForm,
                           'img_url': img_url,
#                           'errors' :
                           })

        if form_resize.is_valid():
            form_resize.save()
            # Возвращает последнюю загруженну картинку для редактирования
            max_id = Image.objects.aggregate(Max('id'))['id__max']  # Определяет последнюю запись в модели
            print(f'Загружено {max_id} фотографий')
            img_url = Image.objects.get(id=max_id-1)

            with ImgPil.open(img_url.load_image.path, 'r') as img:
                width, height = img.size
                print(width, height)


            # Считывает значения с формы изменения изображения
            print(request.POST.get('width'))
            print(request.POST.get('length'))

            return render(request, 'saveimage/form_upload.html', {
                'form_load': ResizeImageForm,
                'img_url': img_url,
            })
    return render(request, 'saveimage/form_upload.html', {
        'form_load': LoadImageForm,
    })
