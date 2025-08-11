from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Comment, Profile, User, Img


class CommentForm(forms.ModelForm):
    """
    Form for creating comments
    """
    class Meta:
        model = Comment
        fields = ['body', ]


class UserUpdateForm(UserChangeForm):
    """
    Form for updating the user model
    """
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", ]

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        for field in ["email", "password"]:
            self.fields[field].help_text = None


class ProfileUpdateForm(forms.ModelForm):
    """
    Form for updating the user's profile page
    """
    class Meta:
        model = Profile
        fields = ['bio', 'avatar', ]


class CreateImg(forms.ModelForm):
    """
    Form for creating an image
    """
    caption = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        required=False  # <--- This disables browser validation
    )

    class Meta:
        model = Img
        fields = ["title", "image", "caption", ]

    def clean_caption(self):
        data = self.cleaned_data.get('caption', '').strip()
        import re
        text_only = re.sub('<[^<]+?>', '', data).strip()
        if not text_only:
            raise forms.ValidationError("Caption is required.")
        return data
