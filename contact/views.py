from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.urls import reverse
from .forms import ContactForm, NewsletterForm

# Create your views here.


def contact_us(request):
    """
    Allows user contact requests.
    **Context**
    ``contact_form``
        An instance of :form: `contact.ContactForm`.
    **Template:**
    :template:`contact/contact.html`
    """
    contact_form = ContactForm()
    subscribe_form = NewsletterForm()
    return render(
        request,
        "contact/contact.html",
        {
            "contact_form": contact_form, 
            "subscribe_form": subscribe_form
        }
    )


def subscribe(request):
    """
    Allows visitors and users to subscribe to the newsletter.
    **Context**
    ``form``
        An instance of :form: `contact.NewsletterForm`.
    """
    if request.method == "POST":
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You subscribed to our newsletter!")
            return redirect(reverse('contact') + '?subscribed=1')
    else:
        form = NewsletterForm()
    context = {"form": form}
    return render(request, "index.html", context)
