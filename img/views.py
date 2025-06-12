from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Img, Comment
# Create your views here.
class ImgList(generic.ListView):
    model = Img
    queryset = Img.objects.all()
    template_name = "img/index.html"
    paginate_by = 6

def img_detail(request, slug):

    queryset = Img.objects.filter(status='published')
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.filter(approved=True).order_by('created_on')

    return render(
        request,
        "img/single.html",
        {
            "img": post,
            "comments": comments,
        },
    )

