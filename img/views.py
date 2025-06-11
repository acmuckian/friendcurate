from django.shortcuts import render
from django.views import generic
from .models import Img, Comment
# Create your views here.
class ImgList(generic.ListView):
    model = Img
    queryset = Img.objects.all()
    template_name = "img/index.html"
    paginate_by = 6