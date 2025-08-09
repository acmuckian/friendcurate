from django.db import models
from django.contrib.auth.models import User
from django.core.files.images import get_image_dimensions
from django.core.exceptions import ValidationError
from cloudinary.models import CloudinaryField


# Create your models here.


class Img(models.Model):
    """
    Stores a single entry of image related to :model: `auth.User`.
    """
    options = ( ('draft', 'Draft'),
               ('published', 'Published')
    )
    image = CloudinaryField('image', blank=False, null=False)
    slug = models.SlugField(max_length=200, unique=True)
    title = models.CharField(max_length=200, unique=True, blank=False, null=False)
    caption = models.TextField(max_length=1000, unique=True, blank=False, null=False)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="img_posts"
    )
    favourites = models.ManyToManyField(
        User, related_name='favourite', default=None, blank=True)
    status = models.CharField(max_length=10, choices=options, default='draft')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]
    
    def __str__(self):
        return f"{self.title} | written by {self.author}"


class Comment(models.Model):
    """
    Stores a single comment entry related to :model:`auth.User`and
    :model:`img.Img`.
    """
    post = models.ForeignKey(
        Img, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"


class Profile(models.Model):
        """
        Stores a single profile related to :model:`auth.User`.
        """
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        avatar = models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics')
        bio = models.TextField(max_length=500, blank=True)

        def clean(self):
            if not self.avatar:
                raise ValidationError("Avatar image is required.")
            else:
                w, h = get_image_dimensions(self.avatar)
            if w > 1000 or h > 1000:
                raise ValidationError("Avatar must not be over 1000 x 1000 pixels.")

        def __str__(self):
            return f"{self.user.username}'s Profile"