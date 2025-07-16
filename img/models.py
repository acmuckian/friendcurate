from django.db import models
from django.contrib.auth.models import User
from django.core.files.images import get_image_dimensions
from django.core.exceptions import ValidationError
from cloudinary.models import CloudinaryField


# Create your models here.
# class Category(models.Model):
#     name = models.CharField(max_length=50)


class Img(models.Model):
    options = ( ( 'draft', 'Draft'),
               ('published', 'Published')
    )
    image = CloudinaryField('image', default='placeholder')
    slug = models.SlugField(max_length=200, unique=True)
    title = models.CharField(max_length=200, unique=True)
    caption = models.CharField(max_length=1000, unique=True)
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
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        avatar = models.ImageField( default='default.jpg', upload_to='profile_pics')
        bio = models.TextField(max_length=500, blank=True)

    def clean(self):
        if not self.avatar:
            raise ValidationError("Avatar image is required.")
        else:
            w, h = get_image_dimensions(self.avatar)
            if w != 200 or h != 200:
                raise ValidationError("Avatar must be exactly 200x200 pixels.")


        def __str__(self):
            return f"{self.user.username}'s Profile"