from django.db import models
from django.contrib.auth.models import User


class Users(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self): # Метод возвращает строковое представление объекта
        return f'{self.user}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'