    
from . import views
from django.urls import path
from django.contrib.auth.models import User
from django.contrib.auth import views as auth_views



urlpatterns = [
    path("subscribe", views.subscribe, name="subscribe"),
    path("contact_us", views.contact_us, name="contact")
]