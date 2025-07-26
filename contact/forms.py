from django import forms
from .models import ContactRequest, NewsletterSubscription

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactRequest
        fields = ['name', 'email','body',]


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscription
        fields = ['email',]