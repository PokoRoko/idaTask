# Generated by Django 3.1.4 on 2020-12-20 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saveimage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='length',
            field=models.IntegerField(default=0, verbose_name='Длина'),
        ),
        migrations.AlterField(
            model_name='image',
            name='width',
            field=models.IntegerField(default=0, verbose_name='Ширина'),
        ),
    ]
