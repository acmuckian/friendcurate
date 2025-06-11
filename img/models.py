from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# class Category(models.Model):
#     name = models.CharField(max_length=50)


class Img(models.Model):
    options = ( ( 'draft', 'Draft'),
               ('published', 'Published')
    )
    image = models.ImageField()
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
        