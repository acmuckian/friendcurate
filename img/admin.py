from django.contrib import admin
from .models import Img, Comment
from django_summernote.admin import SummernoteModelAdmin

class ImgAdmin(SummernoteModelAdmin):
    list_display = ('title', 'status')
    search_fields = ['title']
    list_filter = ('status',)
    summernote_fields = ('caption',)

admin.site.register(Img, ImgAdmin)
admin.site.register(Comment)
