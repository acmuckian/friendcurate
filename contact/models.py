from django.db import models

# Create your models here.


class ContactRequest(models.Model):
    """
    Stores a single entry of a request to make contact.
    """
    name = models.CharField(max_length=200)
    email = models.EmailField(default="example@example.com")
    body = models.TextField(max_length=1000)

    def __str__(self):
        return f"Contact request from {self.name}"


class NewsletterSubscription(models.Model):
    """
    Stores a single entry of a subscription to the newsletter.
    """
    email = models.EmailField(default="example@example.com")
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
