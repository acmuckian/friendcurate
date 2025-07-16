from .models import Comment, Profile, User
from django import forms 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]
        
    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        for field in ["email", "password"]:
            self.fields[field].help_text = None

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'avatar']