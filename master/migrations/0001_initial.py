# Generated by Django 3.1.3 on 2020-11-18 18:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CharacterSummary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Полное имя')),
                ('role', models.CharField(max_length=255, verbose_name='Роль')),
            ],
            options={
                'verbose_name': 'Персонаж',
                'verbose_name_plural': 'Персонажи',
            },
        ),
        migrations.CreateModel(
            name='Comic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comic_id', models.PositiveIntegerField(verbose_name='Идентификатор комикса Marvel')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('release_date', models.DateTimeField(verbose_name='Дата выхода')),
                ('characters', models.ManyToManyField(to='master.CharacterSummary', verbose_name='Персонажи')),
            ],
            options={
                'verbose_name': 'Комикс',
                'verbose_name_plural': 'Комиксы',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=255, verbose_name='Путь')),
                ('extension', models.CharField(max_length=255, verbose_name='Расширение')),
            ],
            options={
                'verbose_name': 'Изображение комикса',
                'verbose_name_plural': 'Изображения комиксов',
            },
        ),
        migrations.CreateModel(
            name='StorySummary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Каноническое название')),
                ('story_type', models.CharField(max_length=255, verbose_name='Тип истории')),
            ],
            options={
                'verbose_name': 'История',
                'verbose_name_plural': 'Истории',
            },
        ),
        migrations.CreateModel(
            name='UserSavedComics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comics', models.ManyToManyField(to='master.Comic', verbose_name='Комиксы')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Сохраненные комиксы пользователя',
                'verbose_name_plural': 'Сохраненные комиксы пользователей',
            },
        ),
        migrations.AddField(
            model_name='comic',
            name='images',
            field=models.ManyToManyField(to='master.Image', verbose_name='Обложки'),
        ),
        migrations.AddField(
            model_name='comic',
            name='stories',
            field=models.ManyToManyField(to='master.StorySummary', verbose_name='Истории'),
        ),
    ]
