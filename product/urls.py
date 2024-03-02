from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    ROLE_CHOICE = [
        ('Author', 'Автор'),
        ('Student', 'Студент'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Имя')
    role = models.CharField(max_length=100, choices=ROLE_CHOICE, blank=True, null=True, verbose_name='Роль')

    class Meta:

        verbose_name = 'Профиль'
    verbose_name_plural = 'Профили'
