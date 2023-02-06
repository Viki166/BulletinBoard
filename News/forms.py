from django.forms import ModelForm
from News.models import News,NewsComment
from django import forms



class NewsForm(ModelForm):
    class Meta:
        model=News
        fields = ('header','text','user','image','category')

class NewsCommentForm(ModelForm):
    class Meta:
        model = NewsComment
        fields = ('text',)

        widgets = {
            'text': forms.Textarea( attrs = {'rows':5, 'placeholder':'Комментарий'}),
        }