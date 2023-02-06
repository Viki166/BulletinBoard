from django.db import models
from django.contrib.auth.models import User
from Main.models import Users

class News(models.Model):
    header = models.CharField("Заголовок",max_length=225)
    text = models.TextField("Текст")
    image = models.ImageField("Картинка",null=True)
    user = models.ForeignKey(Users,on_delete=models.CASCADE,verbose_name="Пользователь")
    datetime = models.DateTimeField("Дата и время",auto_now_add=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name="Категория")

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural ='Новости'

    def __str__(self):
        return f'{self.header}'

    def get_absolute_url(self): 
        return f'/{self.id}'


class Category(models.Model):
    name = models.CharField("Категория",max_length=225)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class NewsComment(models.Model):
    text = models.TextField("Текст")
    user = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name="Пользователь")
    news = models.ForeignKey('News', on_delete=models.CASCADE,verbose_name="Новость")
    datetime = models.DateTimeField("Дата и время", auto_now_add=True)

    def __str__(self):
        return f'{self.user}'
    
    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

