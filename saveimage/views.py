from django.shortcuts import render
from .forms import LoadImageForm, ResizeImageForm
from .models import Image
from django.db.models import Max
from PIL import Image as ImgPil
from idatask.settings import MEDIA_URL


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
            img_url = form_load.instance.load_image.url
            return render(request, 'saveimage/form_upload.html',
                          {'form_resize': ResizeImageForm,
                           'img_url': img_url,
                           'errors': form_load.non_field_errors(),
                           })

        if form_resize.is_valid():
            # Возвращает последнюю загруженну картинку для редактирования
            max_id = Image.objects.aggregate(Max('id'))['id__max']  # Определяет последнюю запись в модели
            print(f'Загружено {max_id} фотографий')
            img_url = Image.objects.get(id=max_id)

            # Получаем новые размеры из формы
            new_width = int(request.POST.get('width'))
            new_height = int(request.POST.get('length'))
            img_path = img_url.load_image.path
            cache_resize_image = ImgPil.open(img_path)
            width, height = cache_resize_image.size

            # Куда и в каком формате сохраняем временное изображение
            cache_image_path = f'{MEDIA_URL}cache_image.{cache_resize_image.format}'
            # Изменение размера изображения если есть ширина и высота
            if new_width != 0 and new_height != 0:
                res_image = cache_resize_image.resize((new_width, new_height), ImgPil.ANTIALIAS)
                res_image.save(f'uploads/cache_image.{cache_resize_image.format}')
            # Изменение только ширины и пропорционально высоты изображения
            elif new_width != 0 and new_height == 0:
                new_height = int(new_width * height / width)
                res_image = cache_resize_image.resize((new_width, new_height), ImgPil.ANTIALIAS)
                res_image.save(f'uploads/cache_image.{cache_resize_image.format}')
            # Изменение только высоты и пропорционально ширины изображения
            elif new_width == 0 and new_height != 0:
                new_width = int(new_height * width / height)
                res_image = cache_resize_image.resize((new_width, new_height), ImgPil.ANTIALIAS)
                res_image.save(f'uploads/cache_image.{cache_resize_image.format}')
            return render(request, 'saveimage/form_upload.html', {
                'form_load': ResizeImageForm,
                'img_url': cache_image_path,
            })

        # Если форма загрузки нового изображения неверная, выдаст ошибку
        else:
            return render(request, 'saveimage/form_upload.html',
                          {'form_resize': LoadImageForm,
                           'errors': form_load.non_field_errors(),
                           })

    # При входе на страницу
    return render(request, 'saveimage/form_upload.html', {
        'form_load': LoadImageForm,
    })
