from django.contrib import admin
from .models import Img, Comment, Profile
from django_summernote.admin import SummernoteModelAdmin

class ImgAdmin(SummernoteModelAdmin):
    list_display = ('title', 'status')
    fields = ('title', 'slug', 'caption', 'image', 'author', 'favourites', 'status')
    search_fields = ['title']
    list_filter = ('status',)
    summernote_fields = ('caption',)
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Img, ImgAdmin)
admin.site.register(Comment)
admin.site.register(Profile)
