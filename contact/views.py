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
    contact_form = ContactForm(prefix="contact")
    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, "Thanks for contacting us!")
            return redirect(reverse('contact') + '?contacted=1')
    else:
        contact_form = ContactForm(prefix="contact")
    subscribe_form = NewsletterForm(prefix="contact_subscribe")
    context = {
         "contact_form": contact_form,
         "subscribe_form": NewsletterForm()
               }
    return render(request, "contact/contact.html", context)


def subscribe(request):
    """
    Allows visitors and users to subscribe to the newsletter.
    **Context**
    ``form``
        An instance of :form: `contact.NewsletterForm`.
    """
    form = NewsletterForm(request.POST or None, prefix="footer_subscribe")
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "You subscribed to our newsletter!")
        return redirect(reverse('contact') + '?subscribed=1')
    # If not valid, try the other prefix
    if request.method == "POST":
        form = NewsletterForm(request.POST, prefix="contact_subscribe")
        if form.is_valid():
            form.save()
            messages.success(request, "You subscribed to our newsletter!")
            return redirect(reverse('contact') + '?subscribed=1')
    # Default forms for rendering
    contact_form = ContactForm()
    subscribe_form = NewsletterForm(prefix="contact_subscribe")
    context = {
        "contact_form": contact_form,
        "subscribe_form": subscribe_form,
    }
    return render(request, "contact/contact.html", context)
