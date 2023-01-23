from django.db import models
from Main.models import Users
from ckeditor_uploader.fields import RichTextUploadingField



class Ad(models.Model):
    header = models.CharField("Заголовок",max_length=225)
    content_upload = RichTextUploadingField("Текстовое поле",blank=True,null=True)
    datetime = models.DateTimeField("Дата и время",auto_now_add=True)
    user = models.ForeignKey(Users,on_delete=models.CASCADE,verbose_name="Пользователь")
    category = models.ForeignKey('Category', on_delete=models.CASCADE,verbose_name="Категория")
    game =models.ForeignKey('Game',on_delete=models.CASCADE, verbose_name="Игра")

    def __str__(self):
        return f'{self.header}'

    def get_absolute_url(self): # метод для определения уникального url-адреса
        return f'/{self.id}'

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
    

class Category(models.Model):
    name = models.CharField("Категория", max_length=225)

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Game(models.Model):
    name = models.CharField("Игра", max_length=225)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name ='Игра'
        verbose_name_plural = 'Игры'


class Comment(models.Model):
    text = models.CharField("Текст")
    datetime = models.DateTimeField("Дата и время",auto_now_add=True)
    ad = models.ForeignKey(Ad,on_delete=models.CASCADE,verbose_name="Объявление")
    user = models.ForeignKey(Users,on_delete=models.CASCADE, verbose_name="Пользователь")
    active = models.BooleanField("Видимость комментария",default=False)
    def __str__(self):
        return f'{self.user}'
    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
