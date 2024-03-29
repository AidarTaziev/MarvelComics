# Generated by Django 3.1.3 on 2020-11-20 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0012_auto_20201119_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savedcomic',
            name='comic_id',
            field=models.PositiveIntegerField(verbose_name='Идентификатор комикса'),
        ),
        migrations.AlterField(
            model_name='savedcomic',
            name='release_date',
            field=models.DateField(verbose_name='Дата выхода'),
        ),
        migrations.AlterField(
            model_name='story',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Название'),
        ),
    ]
