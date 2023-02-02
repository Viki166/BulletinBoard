from Main.models import Contact
from Main.forms import ContactForm
from django.views.generic import CreateView
from Main.tasks import send_email

class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    success_url = "/"

    def form_valid(self,form):
        form.save()
        send_email.delay(form.instance.email)
        return super().form_valid(form)

    