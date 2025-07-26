from django.db import models

# Create your models here.

class ContactRequest(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField
    body = models.TextField(max_length=1000)

    def __str__(self):
        return f"Contact request from {self.name}"
    
class NewsletterSubscription(models.Model):
    email = models.EmailField
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.email