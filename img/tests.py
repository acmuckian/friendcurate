from django.test import TestCase
from .forms import CommentForm, ProfileUpdateForm, UserUpdateForm, CreateImg
# Create your tests here.

class TestCommentForm(TestCase):

    def test_form_is_valid(self):
        comment_form = CommentForm({'body':'Post'})
        self.assertTrue(comment_form.is_valid)
    def test_form_is_invalid(self):
        comment_form = CommentForm({'body': ''})
        self.assertFalse(comment_form.is_valid(), msg="Form is valid")

class TestImgForm(TestCase):
    def img_form_is_valid(self):
        img_form = CreateImg({
            "title": "My Img",
            "image": "img.png",
            "caption": "My Caption"
        })
        self.assertTrue(img_form.is_valid)

class TestProfileUpdateForm(TestCase):

    def test_form_is_valid(self):
        profile_update_form = ProfileUpdateForm({
            'avatar': 'picture.jpg',
            'bio': 'About me'
                    })
        self.assertTrue(profile_update_form.is_valid)
