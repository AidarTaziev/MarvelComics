from django.db import models


class Image(models.Model):
    path = models.CharField(max_length=255, verbose_name="Путь")
    extension = models.CharField(max_length=255, verbose_name="Расширение")

    class Meta:
        verbose_name = "Обложка комикса"
        verbose_name_plural = "Обложкиы комиксов"

    def __str__(self):
        return self.path


class Character(models.Model):
    name = models.CharField(max_length=255, verbose_name="Полное имя")
    role = models.CharField(max_length=255, null=True, blank=True, verbose_name="Роль")

    class Meta:
        verbose_name = "Персонаж"
        verbose_name_plural = "Персонажи"

    def __str__(self):
        return self.name


class Story(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    story_type = models.CharField(max_length=255, null=True, blank=True, verbose_name="Тип истории")

    class Meta:
        verbose_name = "История"
        verbose_name_plural = "Истории"

    def __str__(self):
        return self.name


class SavedComic(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name="Пользователь")
    comic_id = models.PositiveIntegerField(verbose_name="Идентификатор комикса")
    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    release_date = models.DateField(verbose_name="Дата выхода")
    images = models.ManyToManyField(Image, verbose_name="Картинки")
    characters = models.ManyToManyField(Character, verbose_name="Персонажи")
    stories = models.ManyToManyField(Story, verbose_name="Истории")

    class Meta:
        unique_together = (("user", "comic_id"),)
        verbose_name = "Комикс"
        verbose_name_plural = "Комиксы"

    def __str__(self):
        return self.title



