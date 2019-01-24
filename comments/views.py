from django.shortcuts import render, redirect
from .models import Comment

# Create your views here.
def comment_delete(request, id=None, post_id=None):
    comment = Comment.objects.get(id=id)
    print(comment)
    comment.delete()

    return redirect('details', id=post_id)