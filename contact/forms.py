from django import forms
from .models import ContactRequest, NewsletterSubscription


class ContactForm(forms.ModelForm):
    """
    Form for contact requests
    """
    class Meta:
        model = ContactRequest
        fields = ['name', 'email', 'body', ]


class NewsletterForm(forms.ModelForm):
    """
    Form for subscribing to the newsletter
    """
    class Meta:
        model = NewsletterSubscription
        fields = ['email', ]
