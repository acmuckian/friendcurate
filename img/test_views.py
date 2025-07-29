from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase, Client
from .forms import CommentForm
from .models import Img, Profile

class TestImgViews(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="username",
            password="password",
            email="test@test.com"
        )
        self.img = Img(title="Image title", author=self.user,
                         slug="image-title", caption="image caption", status="published")
        self.img.save()

    def test_render_post_detail_page_with_comment_form(self):
        response = self.client.get(reverse(
            'img_detail', args=['image-title']))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Image title", response.content)
        self.assertIsInstance(
            response.context['comment_form'], CommentForm)


class TestProfile(TestCase):
  def SetUp(self):
    self.user = User.objects.create_user(
            username="username",
            password="password",
            email="test@test.com"
        )
    self.profile = Profile(user=self.user, avatar="default.jpg", bio="about me")

  def test_profile_page(self):
            response = self.client.get(reverse('profile', kwargs={'user_id': self.user.id}))
            self.assertEqual(response.status_code, 200)
            self.assertContains(response, self.user.username)
            self.assertContains(response, self.profile.bio)


