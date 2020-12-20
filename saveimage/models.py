from django.db import models

# Create your models here.


class Image(models.Model):
    name = models.CharField('Имя файла', max_length=100)
    url_image = models.URLField('Ссылка', max_length=200, blank=True,)
    load_image = models.ImageField('Файл', blank=True,)
    length = models.IntegerField('Высота', default=0)
    width = models.IntegerField('Ширина', default=0)

    def __str__(self):
        """
        Магический метод, который отвечает за строковое
        представление обьекта класса
        """
        return self.name

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"
