from django.test import TestCase
from .forms import ContactForm, NewsletterForm
# Create your tests here.

class TestContactForm(TestCase):
   def contact_form_is_valid(self):
        contact_form = ContactForm({
            'name': 'contact',
            'email':'contact@contact.com',
            'body' : 'hello'
        })
        self.assertTrue(contact_form.is_valid(), msg="form is invalid")
   def test_name_is_required(self):
        form = ContactForm({
            'name': '',
            'email': 'contact@contact.com',
            'message': 'Hello!'
        })
        self.assertFalse(
            form.is_valid(),
            msg="Name was not provided, but the form is valid"
        )

class TestNewsLetterForm(TestCase):
    def newsletter_form_is_valid(self):
        newsletter_form = NewsletterForm({
            'email':'newsletter@email.com',
        })
        self.assertTrue(newsletter_form.is_valid(), msg="form is not valid")