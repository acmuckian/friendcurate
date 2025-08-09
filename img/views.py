from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
from .models import Img, Comment, User
from .forms import CommentForm, UserUpdateForm, ProfileUpdateForm
from . import forms


# Create your views here.


class ImgList(generic.ListView):
    model = Img
    queryset = Img.objects.exclude(slug__isnull=True).exclude(slug__exact='')
    template_name = "img/index.html"
    paginate_by = 6


def img_detail(request, slug):
    """
    Displays an individual instance of :model:img.Img
    **Context**
    ``img``
        An instance of :model:`img.Img`.
    ``comments``
        All comments related to the img.
    ``comment_count``
        A count of comments related to the img.
    ``comment_form``
        An instance of :form:`img.CommentForm`.

    **Template:**
    :template:`img/single.html`
    """
    queryset = Img.objects.filter(status='published')
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by('-created_on')
    comment_count = post.comments.filter(approved=True).count()
    comment_form = CommentForm()
    edit_comment_id = request.GET.get('edit_comment')
    edit_comment = None
    edit_form = None

    if edit_comment_id:
        try:
            edit_comment = Comment.objects.get(
                pk=edit_comment_id,
                post=post,
                author=request.user
                )
            edit_form = CommentForm(instance=edit_comment)
        except Comment.DoesNotExist:
            edit_comment = None

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('img_detail', slug=slug)
    return render(
        request,
        "img/single.html",
        {
            "img": post,
            "comments": comments,
            "comment_form": comment_form,
            "edit_comment": edit_comment,
            "edit_form": edit_form,
        },
    )


def img_delete(request, slug):
    """
    Deletes an image.

    **Context**
    ``img``
        An instance of :model:`img.Img`.
    """
    queryset = Img.objects.filter(status="published")
    img = get_object_or_404(queryset, slug=slug)
    if img.author == request.user:
        img.delete()
        messages.add_message(request, messages.SUCCESS, 'Image removed!')
        return HttpResponseRedirect(reverse('home'))
    else:
        messages.add_message(request, messages.ERROR,
                             'You can only delete your own images!')
        return redirect('img_detail', slug=img.slug)


@login_required
def submit_image(request):
    """
    Allows a logged-in user to submit an image to the site.

        **Context**
    ``form``
        An instance of :form:`img.form`.
        **Template:**
    :template:`img/submit.html`
    """

    if request.method == "POST":
        form = forms.CreateImg(request.POST, request.FILES)
        if form.is_valid():
            newimg.status = "published"
            newimg = form.save(commit=False)
            newimg.author = request.user
            if not newimg.slug:
                newimg.slug = slugify(newimg.title)
            original_slug = newimg.slug
            counter = 1
            while Img.objects.filter(slug=newimg.slug).exists():
                newimg.slug = f"{original_slug}-{counter}"
                counter += 1
            newimg.save()
            newimg.save()
            messages.add_message(request, messages.SUCCESS, "Image Submitted!")
            return redirect("img_detail", slug=newimg.slug)
    else:
        form = forms.CreateImg()
    return render(request, "img/submit.html", {"form": form})


def comment_edit(request, slug, comment_id):
    """
    Display an individual comment for edit.

    **Context**

    ``post``
        An instance of :model:`img.Img.
    ``comment``
        A single comment related to the img.
    ``comment_form``
        An instance of :form:`img.CommentForm`
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
            messages.add_message(
                request,
                messages.ERROR,
                'Error updating comment!'
                )
    return HttpResponseRedirect(reverse('img_detail', args=[slug]))


@login_required
def comment_delete(request, slug, comment_id):
    """
    Delete an individual comment.

    **Context**

    ``img``
        An instance of :model:`img.Img`.
    ``comment``
        A single comment related to the img.
    """
    queryset = Img.objects.filter(status="published")
    img = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id, post=img)
    if request.method == "POST":
        if comment.author == request.user:
            comment.delete()
            messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
        else:
            messages.add_message(
                request,
                messages.ERROR,
                'You can only delete your own comments!'
                  )
    else:
        messages.error(request, 'Invalid request method.')
    return HttpResponseRedirect(reverse('img_detail', args=[slug]))


@login_required
def add_favourite(request, id):
    """
    Allows a user to add an image to their favourites.
        **Context**

    ``img``
        An instance of :model:`img.Img`.
    ``favourites``
        A favourite related to the img.
        **Template**
        :template:`img/favourites.html`
    """
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
    """
    Allows a user to see their favourites.
        **Context**

    ``img``
        An instance of :model:`img.Img`.
    ``favourites``
        A favourite related to the img.
        **Template**
        :template:`img/favourites.html`
    """
    favourite_images = Img.objects.filter(
        favourites=request.user,
        status='published'
        )

    return render(
        request,
        'img/favourites.html',
        {"favourite_images": favourite_images}
    )


@login_required
def profile(request, user_id):
    """
    Allows a user to see their profile.
        **Context**
    ``user``
        An instance of :model:`auth.User`.
        **Template**
        :template:`user/profile.html`
    """
    user = get_object_or_404(User, pk=user_id)
    if not hasattr(user, 'profile'):
        from .models import Profile
        Profile.objects.create(user=user)
    if request.user == user and request.method == "POST":
        user_form = UserUpdateForm(
            request.POST,
            instance=request.user
        )
        profile_form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(
                request,
                'Your profile has been updated successfully')
            return redirect('profile', user_id=request.user.id)
        else:
            messages.error(request, 'Error updating your profile')
    else:
        user_form = UserUpdateForm(instance=user)
        profile_form = ProfileUpdateForm(instance=user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'users/profile.html', context)
