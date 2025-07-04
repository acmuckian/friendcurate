from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Img, Comment
from .forms import CommentForm


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
    comment_form = CommentForm()
    if request.method == "POST":
        comment_form = comment_form(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post 
            comment.save()
    

    return render(
        request,
        "img/single.html",
        {
            "img": post,
            "comments": comments,
            "comment_form": comment_form,
        },
    )

def img_delete(request, slug):
    queryset = Img.objects.filter(status="published")
    img = get_object_or_404(queryset, slug=slug)
    if img.author == request.user:
        img.delete()
        messages.add_message(request, messages.SUCCESS, 'Image removed!')
        return HttpResponseRedirect(reverse('home'))
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own images!')
        return redirect('img_detail', slug=img.slug)


def comment_edit(request, slug, comment_id):
    """
    Display an individual comment for edit.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.
    ``comment``
        A single comment related to the post.
    ``comment_form``
        An instance of :form:`blog.CommentForm`
    """
    if request.method == "POST":

        queryset = Img.objects.filter(status='published')
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Error updating comment!')
    return HttpResponseRedirect(reverse('img_detail', args=[slug]))

@login_required
def comment_delete(request, slug, comment_id):
    """
    Delete an individual comment.

    **Context**

    ``img``
        An instance of :model:`blog.Post`.
    ``comment``
        A single comment related to the post.
    """
    queryset = Img.objects.filter(status="published")
    img = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id, post=img)
    if request.method == "POST":
        if comment.author == request.user:
            comment.delete()
            messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
        else:
         messages.add_message(request, messages.ERROR,
                             'You can only delete your own comments!')
    else:
        messages.error(request, 'Invalid request method.')
    return HttpResponseRedirect(reverse('img_detail', args=[slug]))

@login_required
def add_favourite(request, id):
    img = get_object_or_404(Img, id=id)
    if img.favourites.filter(id=request.user.id).exists():
        img.favourites.remove(request.user)
        messages.add_message(request, messages.SUCCESS, 'Favourite removed!')
    else:
        img.favourites.add(request.user)
        messages.add_message(request, messages.SUCCESS, 'Favourite added!')
    return redirect('img_detail', slug=img.slug)

@login_required

def my_favourites(request):
    favourite_images = Img.objects.filter(favourites=request.user, status='published')

    return render(
        request,
        'img/favourites.html',
        {"favourite_images": favourite_images}
    )
