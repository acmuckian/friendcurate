from .forms import NewsletterForm

def footer_subscribe_form(request):
    return {'footer_subscribe_form': NewsletterForm(prefix="footer_subscribe")}