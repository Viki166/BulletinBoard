from django import template
from Main.forms import ContactForm


register = template.Library()


@register.inclusion_tag('contacts/tags/form.html')
def contact_form():
    form = ContactForm
    return {"contact_form": form}