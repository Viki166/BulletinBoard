from django.forms import ModelForm
from django import forms
from Main.models import Contact

class ContactForm(ModelForm):
    """Форма подписки на рассылку"""
    class Meta:
        model = Contact
        fields = ("email",)
        widgets = {
            'email': forms.EmailInput(attrs={"class":"form-control bg-transparent text-white w-100 py-3 ps-4 pe-5","placeholder": "Your email.."}) 
            }
        labels ={"email":""}