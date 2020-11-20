from django.db import models

# Create your models here.
class Image(models.Model):
    path = models.CharField(max_length=255, verbose_name="Путь")
    extension = models.CharField(max_length=255, verbose_name="Расширение")

    class Meta:
        verbose_name = "Изображение комикса"
        verbose_name_plural = "Изображения комиксов"

    def __str__(self):
        return self.file.name


class CharacterSummary(models.Model):
    name = models.CharField(max_length=255, verbose_name="Полное имя")
    role = models.CharField(max_length=255, null=True, blank=True, verbose_name="Роль")

    class Meta:
        verbose_name = "Персонаж"
        verbose_name_plural = "Персонажи"

    def __str__(self):
        return self.name


class StorySummary(models.Model):
    name = models.CharField(max_length=255, verbose_name="Каноническое название")
    story_type = models.CharField(max_length=255, verbose_name="Тип истории")

    class Meta:
        verbose_name = "История"
        verbose_name_plural = "Истории"

    def __str__(self):
        return self.name


class Comic(models.Model):
    comic_id = models.PositiveIntegerField(verbose_name="Идентификатор комикса Marvel")
    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    release_date = models.DateTimeField(verbose_name="Дата выхода")
    images = models.ManyToManyField(Image, verbose_name="Обложки")
    characters = models.ManyToManyField(CharacterSummary, verbose_name="Персонажи")
    stories = models.ManyToManyField(StorySummary, verbose_name="Истории")

    class Meta:
        verbose_name = "Комикс"
        verbose_name_plural = "Комиксы"

    def __str__(self):
        return self.title