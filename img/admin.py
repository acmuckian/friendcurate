from django.contrib import admin
from .models import Img, Comment
from django_summernote.admin import SummernoteModelAdmin

class ImgAdmin(SummernoteModelAdmin):

        list_display = ('title', 'slug', 'status')
        search_fields = ['title']
        list_filter = ('status',)
        prepopulated_fields = {'caption': ('title',)}
        summernote_fields = ('content',)

admin.site.register(Img)
admin.site.register(Comment)
