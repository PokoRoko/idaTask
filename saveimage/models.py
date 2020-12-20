from django.db import models

# Create your models here.


class Image(models.Model):
    name = models.CharField('Имя файла',max_length=100)
    url_image = models.URLField('Ссылка', max_length=200, blank=True)
    load_image = models.ImageField('Файл', blank=True)
    length = models.IntegerField('Длина')
    width = models.IntegerField('Ширина')

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"