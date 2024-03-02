from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Имя')

    class Meta:
        verbose_name = 'Профиль'

    verbose_name_plural = 'Профили'
