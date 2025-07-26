from django.test import TestCase
from .forms import CommentForm, ProfileUpdateForm, UserUpdateForm
# Create your tests here.

class TestCommentForm(TestCase):

    def test_form_is_valid(self):
        comment_form = CommentForm({'body':'Post'})
        self.assertTrue(comment_form.is_valid)
    def test_form_is_invalid(self):
        comment_form = CommentForm({'body': ''})
        self.assertFalse(comment_form.is_valid(), msg="Form is valid")

class TestProfileUpdateForm(TestCase):

    def test_form_is_valid(self):
        profile_update_form = ProfileUpdateForm({
            'avatar': 'picture.jpg',
            'bio': 'About me'
                    })
        self.assertTrue(profile_update_form.is_valid)
