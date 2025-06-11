from django.shortcuts import render
from django.views import generic
from .models import Img, Comment
# Create your views here.
class ImgList(generic.ListView):
    model = Img
    queryset = Img.objects.filter(author=1)
    template_name = ""
    paginate_by = 6