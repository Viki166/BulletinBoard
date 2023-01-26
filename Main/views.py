from Main.models import Contact
from Main.forms import ContactForm
from django.views.generic import CreateView
from django.urls import reverse_lazy


class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    success_url = "/"

    def form_valid(self,form):
        form.save()
        return super().form_valid(form)
