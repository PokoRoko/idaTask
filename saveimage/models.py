from django.db import models

# Create your models here.


class Image(models.Model):

    url_image = models.URLField('Ссылка', max_length=200, blank=True)
    load_image = models.ImageField('Файл', blank=True)
    length = models.IntegerField('Длина', max_length=4)
    width = models.IntegerField('Ширина', max_length=4)

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"