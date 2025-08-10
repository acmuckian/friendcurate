from contact.forms import NewsletterForm

def subscribe_form(request):
    return {'subscribe_form': NewsletterForm()}