from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
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
    return render(
        request,
        "contact/contact.html",
        {
            "contact_form": contact_form
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
            email = request.POST.get("email")
            subject = "Thanks for subscribing to Friendcurate"
            message = (
                "Thank you for subscribing to our newsletter,"
                + "you will see the latest developments"
                + "in visual arts and about our site!"
                + "Go back https://friendcurate.herokuapp.com/"
            )
            from_email = "acmuckian@gmail.com"
            recipient_list = [email]
            send_mail(subject,
                      message, from_email, recipient_list, fail_silently=False)
            return redirect("/")
    else:
        form = NewsletterForm

    context = {"form": form}
    return render(request, "index.html", context)
