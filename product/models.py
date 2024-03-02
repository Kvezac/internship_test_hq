from datetime import datetime

from django.core.validators import MaxValueValidator
from django.db import models

from user.models import Profile


class Product(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Автор')
    name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Название курса')
    start_date = models.DateField(default=datetime.now, blank=True, verbose_name='Дата начала')
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Название курса: {self.name}; Автор курса: {self.author.name}; Цена курса {self.cost}"


class Lesson(models.Model):
    product = models.OneToOneField('Product', on_delete=models.SET_NULL, null=True, blank=True, related_name='lesson')
    title = models.CharField(max_length=255, null=True, blank=True, verbose_name='Название урока')
    video_link = models.URLField(max_length=255, null=True, blank=True, verbose_name='Ссылка на видео')

    def __str__(self):
        return f"Название курса: {self.product.name} Название урока: {self.title}"


class Group(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Название группы')
    members = models.ManyToManyField(Profile, related_name='group_members')
    limit_group_size = models.IntegerField(default=0, validators=MaxValueValidator(100),
                                           verbose_name='Студентов в группе')

    def __str__(self):
        return f"Название группы: {self.name}; Количество участников: {self.limit_group_size}"
