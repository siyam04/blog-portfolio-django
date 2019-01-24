from django.contrib.contenttypes.models import ContentType
from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
)
from django.http import Http404
from django.contrib import messages
from urllib.parse import quote_plus
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Same App importing
from comments.forms import CommentForm
from comments.models import Comment
from .models import Post, Category
from .forms import PostForm
from user_info.models import Profile


# Function-Based views
def all_posts(request, id):
    posts_list = Post.objects.filter(category__id=id)
    context = {'all_posts': posts_list}
    template = 'posts/posts_list.html'
    return render(request, template, context)


def all_categories(request):
    category_list = Category.objects.all().order_by('-id')
    context = {'all_categories': category_list}
    template = 'posts/category_list.html'
    return render(request, template, context)


def all_authors(request):
    authors_list = User.objects.all().order_by('-id')
    context = {'all_authors': authors_list}
    template = 'posts/author_list.html'
    return render(request, template, context)


@login_required
def posts_create(request):
    """Creating Posts using model form"""
    try:
        profile = Profile.objects.get(user = request.user)
        posts = Post.objects.filter(user__profile_name = profile.profile_name)
        form = PostForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = profile
            instance.save()
            messages.success(request, 'Created Successfully ! Pending For Admin Approval...', extra_tags='html_safe')
            return redirect('details', id=instance.id)
        context = {
            'form': form,
            'posts': posts,
        }
        template = 'posts/post_create.html'
        return render(request, template, context)
    except:
        return redirect('profile')


def posts_details(request, id=None):
    """Displaying single item"""
    instance = Post.objects.get(id=id)
    posts = Post.objects.filter(user__profile_name=instance.user.profile_name)
    share_string = quote_plus(instance.content)

    form = CommentForm(request.POST or None)
    comments = instance.comments
    context = {
        'title': instance.title,
        'instance': instance,
        'share_string': share_string,
        'comments': comments,
        'comment_form': CommentForm(),
        'posts': posts,
    }
    if form.is_valid():
        print('working')
        comment = form.save(commit=False)
        comment.content_type = instance.get_content_type
        comment.object_id = instance.id
        try:
            comment.name = request.user
        except:
            return redirect('signup')
        c_type = comment.content_type
        comment.content_type = ContentType.objects.get(model=c_type)
        parent_obj = None
        try:
            parent_id = int(request.POST.get("parent_id"))
        except:
            parent_id = None

        if parent_id:
            parent_qs = Comment.objects.filter(id=parent_id)
            if parent_qs.exists() and parent_qs.count() == 1:
                parent_obj = parent_qs.first()
        comment.parent = parent_obj
        comment.save()
        template = 'posts/post_details.html'
        return render(request, template, context)

    template = 'posts/post_details.html'
    return render(request, template, context)


@login_required
def posts_update(request, id=None):
    """Updating individual item"""
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, request.FILES or None,
                    instance=instance)
    if request.user.username == instance.user.user.username:
        if form.is_valid():
            instance = form.save(commit=False)
            instance.draft = True
            instance.save()
            messages.success(request, 'Updated Successfully ! Pending For Admin Approval...', extra_tags='html_safe')
            return redirect('details', instance.id)
    else:
        raise Http404
    context = {
        'title': instance.title,
        'instance': instance,
        'form': form,
    }
    template = 'posts/post_update.html'
    return render(request, template, context)


@login_required
def posts_delete(request, id=None):
    """Deleting individual item"""
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, 'Deleted Successfully !', extra_tags='html_safe')
    return redirect('home')
