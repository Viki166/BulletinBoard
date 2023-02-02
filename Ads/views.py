from Ads.models import Ad,Game, Comment
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from Ads.forms import AdForm, CommentForm
from django.views.generic.edit import FormMixin
from Main.models import Users
from django.contrib.auth.models import User
from Ads.filters import CommentsFilter
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.template import Context, Template
from django.shortcuts import render




class AdsListView(ListView):
    model = Ad
    template_name = "ads/ads.html"
    context_object_name = 'ads'
    queryset = Ad.objects.all().order_by('-id')
    ordering = ['-id']
    paginate_by = 3

    def get_context_data(self,**kwargs): # возвращает контекстные данные для отображения объекта
        context = super().get_context_data(**kwargs)
        context['games'] = Game.objects.all()
        context['form'] = AdForm
        """Комментарии к своим объявлениям"""
        for comment in Comment.objects.all():
            if comment.user.user == self.request.user and comment.user.user == comment.ad.user.user:
                comment.active = True
                comment.save()
        return context


class DetailAd(FormMixin,DetailView):
    model = Ad
    template_name = 'ads/ad.html'
    context_object_name ='ad'
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm
        context['comments'] = Comment.objects.all()
        return context
    
    def post(self, request,*args,**kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            ad = self.get_object()
            form.instance.ad = ad
            form.instance.user = Users.objects.get(user=User.objects.get(username=request.user.username))
            form.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self, **kwargs):
       return reverse_lazy('ad_detail',kwargs={'pk':self.get_object().pk})


class AdCreateView(CreateView):
    model = Ad
    form_class = AdForm
    template_name = 'ads/ad_create.html'
    success_url = reverse_lazy('ads')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AdForm
        return context

    def post(self,request,*args,**kwargs):
        """Добавить пользователя в Users, если его там нет"""
        if not(Users.objects.filter(user=self.request.user)):
            Users.objects.create(user=self.request.user)
        form = AdForm(request.POST)
        if form.is_valid():
            form.instance.user = Users.objects.get(user=request.user)
            form.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class AdUpdateView(UpdateView):
    model = Ad
    form_class = AdForm
    template_name = 'ads/ad_create.html'
    success_url = reverse_lazy('ads')

    def get_object(self,**kwargs):
        id = self.kwargs.get('pk')
        return Ad.objects.get(pk=id)
    


class AdDeleteView(DeleteView):
    template_name = 'ads/ad_delete.html'
    queryset = Ad.objects.all()
    success_url = reverse_lazy('ads')


class Comments(ListView):
    model = Comment
    template_name = "ads/comment.html"
    context_object_name = 'comments'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] =  CommentsFilter(self.request.GET, queryset=Comment.objects.all())
        return context

def updateCommentActive(request,pk,type):
    comment = Comment.objects.get(pk=pk)
    if type == 'public':
        comment.active = True
        comment.save()
        template = Template("""<div class="post-content"><p>Комментарий опубдикован.</p></div>""")
        context = Context({'comment': comment})
        return HttpResponse(template.render(context))
    elif type == 'delete':
        comment.delete()
        template = Template("""<div class="post-content"><p>Комментарий удален.</p></div>""")
        context = Context({'comment': comment})
        return HttpResponse(template.render(context))
    return reverse_lazy('ads')


def Gamelist(request,game):
    list = Game.objects.filter(name=game)
    Ads = Ad.objects.filter(game=game)
    return render(request, 'ads/game.html',{'list':list,'Ads':Ads})

