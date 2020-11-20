# Generated by Django 3.1.3 on 2020-11-19 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0002_auto_20201118_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charactersummary',
            name='role',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Роль'),
        ),
        migrations.AlterField(
            model_name='comic',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='storysummary',
            name='story_type',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Тип истории'),
        ),
    ]
