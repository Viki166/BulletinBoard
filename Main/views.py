from Main.models import Contact
from Main.forms import ContactForm
from django.views.generic import ListView,CreateView
from Main.tasks import send_email
from News.models import News


class MainView(ListView):
    model = News
    template_name = 'main/index.html'
    context_object_name = 'news'



class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    success_url = "/"

    def form_valid(self,form):
        form.save()
        send_email.delay(form.instance.email)
        return super().form_valid(form)

    