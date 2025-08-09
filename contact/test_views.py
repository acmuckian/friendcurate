from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import CommentForm
from .models import NewsletterSubscription, ContactRequest

class TestContactViews(TestCase):
    