from django.db import models
from urllib.request import urlopen
from tempfile import NamedTemporaryFile
from django.core.files import File


class Image(models.Model):
    name = models.CharField('Имя файла', max_length=100)
    url_image = models.URLField('Ссылка', max_length=200, blank=True,)
    load_image = models.ImageField('Файл', blank=True,)
    length = models.IntegerField('Высота', default=0)
    width = models.IntegerField('Ширина', default=0)

    def __str__(self):
        return self.name

    # Переопределяем новый сэйв чтобы автоматически сохранялись изображения по ссылке
    def save(self, *args, **kwargs):
        if self.url_image and not self.load_image:
            img_temp = NamedTemporaryFile(delete=True)
            img_temp.write(urlopen(self.url_image).read())
            file_name = self.url_image[self.url_image.rfind("/")+1:]  # Определяем имя файла в url
            img_temp.flush()
            self.load_image.save(file_name, File(img_temp))
        super(Image, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"
