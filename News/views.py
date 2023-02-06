from News.models import News,Category,NewsComment
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from News.forms import NewsForm, NewsCommentForm
from django.views.generic.edit import FormMixin
from Main.models import Users, User
from django.urls import reverse_lazy


class NewsList(ListView):
    template_name = 'news/news.html'
    context_object_name = 'all_news'
    queryset = News.objects.all().order_by('-id')
    ordering = ['-id']
    paginate_by = 6
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = NewsForm
        return context


class NewsDetail(FormMixin, DetailView):
    model = News
    template_name = 'news/news-detail.html'
    context_object_name = 'news'
    form_class = NewsCommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = NewsCommentForm
        context['comments'] = NewsComment.objects.all()
        return context
    
    def post(self, request,*args,**kwargs):
        form = NewsCommentForm(request.POST)
        if form.is_valid():
            news = self.get_object()
            form.instanse.news = news
            form.instance.user = Users.objects.get(user=User.ogjects.get(username=request.user.uesrname))
            form.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self, **kwargs):
        reverse_lazy('news_detail',kwargs={'pk':self.get_object().pk})


class NewsCreate(CreateView):
    models=News
    template_name='news/news-create.html'
    form_class= NewsForm
    success_url=reverse_lazy('news')

class NewsUpdate(UpdateView):
    models=News
    template_name='news/news-create.html'
    form_class= NewsForm
    success_url=reverse_lazy('news')
    
    def get_object(self,**kwargs):
        id= self.kwargs.get('pk')
        return News.objects.get(pk=id)



class NewsDelete(DeleteView):
    template_name='news/news-delete.html'
    queryset = News.objects.all()
    success_url =reverse_lazy('news')