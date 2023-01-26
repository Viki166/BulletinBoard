from django.db import models
from django.contrib.auth.models import User


class Users(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, verbose_name="Пользователь")

    def __str__(self): # Метод возвращает строковое представление объекта
        return f'{self.user}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

class Contact(models.Model):
    email = models.EmailField("Email")
    datetime = models.DateTimeField("Дата и время", auto_now_add=True)

    def __str__(self):
        return f'{self.email}'
    
    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'