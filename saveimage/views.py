from django.shortcuts import render
from .forms import LoadImageForm, ResizeImageForm
from .models import Image
from django.db.models import Max
from PIL import Image as ImgPil
from idatask.settings import MEDIA_URL, MEDIA_ROOT
from django.shortcuts import redirect


def list_image(request):
    images = Image.objects.order_by('-id')  # Получаем все обьекты из модели
    return render(request, 'saveimage/list_image.html', {"images": images})


def form_upload(request):
    """Если в форме отправки есть изображение, обновит и покажет окно для изменения размера"""
    if request.method == 'POST':
        form_load = LoadImageForm(request.POST, request.FILES)
        # Проверяет форму и загружает изображение
        if form_load.is_valid():
            form_load.save()
            img_url = form_load.instance.load_image.url
            return redirect('/resize/', img_url=img_url)
        # Если форма загрузки нового изображения неверная, выдаст ошибку
        else:
            return render(request, 'saveimage/form_upload.html',
                          {'form_resize': LoadImageForm,
                           'errors': form_load.non_field_errors(),

                           })
    # Для кнопки "добавить изображение"
    return render(request, 'saveimage/form_upload.html', {
        'form_load': LoadImageForm,
    })


def resize(request, open_image=''):
    """Если в форме отправки есть изображение, обновит и покажет окно для изменения размера"""
    if request.method == 'GET':
        # Если open_image пустое значит переход был со страницы загрузки и открывает загруженное изображение
        if open_image == '':
            max_id = Image.objects.aggregate(Max('id'))['id__max']  # Определяет последнюю запись в модели
            img_url = Image.objects.get(id=max_id)
            path_image = MEDIA_URL + str(img_url.load_image)
            open_image = img_url.load_image.name
        # Если open_image не пустое открывает изображение по ссылке
        else:
            path_image = MEDIA_URL + open_image
        return render(request, 'saveimage/resize_page.html',
                      {'form_resize': ResizeImageForm,
                       'img_url': path_image,
                       'file_name': open_image,
                       })

    if request.method == 'POST':
        form_resize = ResizeImageForm(request.POST, request.FILES)
        if form_resize.is_valid():
            # Получаем новые размеры из формы
            new_width = int(request.POST.get('width'))
            new_height = int(request.POST.get('length'))
            if open_image == '':  # Если нет значения из url
                # Возвращает последнюю загруженную картинку для редактирования
                max_id = Image.objects.aggregate(Max('id'))['id__max']  # Определяет последнюю запись в модели
                img_url = Image.objects.get(id=max_id)
                img_path = img_url.load_image.path

            # Если нет значения из url открывает изображение для редактирования
            else:
                img_path = MEDIA_ROOT + open_image
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
            return render(request, 'saveimage/resize_page.html', {
                'form_resize': ResizeImageForm,
                'img_url': cache_image_path,
                'file_name': open_image,
            })
        # Если форма изменения размера не прошла валидацию
        else:
            if open_image == '':  # Если нет значения из url
                # Возвращает последнюю загруженную картинку для редактирования
                max_id = Image.objects.aggregate(Max('id'))['id__max']  # Определяет последнюю запись в модели
                img_url = Image.objects.get(id=max_id)
                img_path = img_url.load_image.path

            # Если нет значения из url открывает изображение для редактирования
            else:
                cache_image_path = MEDIA_URL + open_image
            # cache_resize_image = ImgPil.open(img_path)
            #
            # # Куда и в каком формате сохраняем временное изображение
            # cache_image_path = f'{MEDIA_URL}cache_image.{cache_resize_image.format}'
            return render(request, 'saveimage/resize_page.html', {
                'form_resize': ResizeImageForm,
                'img_url': cache_image_path,
                'file_name': open_image,
                'errors': form_resize.non_field_errors()
            })
