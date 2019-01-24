from posts.views import (
    all_posts,
    all_categories,
    all_authors,
    posts_create,
    posts_details,
    posts_update,
    posts_delete,
)
from django.urls import path

urlpatterns = [

    path('all-posts/<int:id>/', all_posts, name='all-posts'),
    path('categories/', all_categories, name='categories'),
    path('all-authors/', all_authors, name='all-authors'),
    path('create/', posts_create, name='create'),
    path('details/<int:id>/', posts_details, name='details'),
    path('update/<int:id>/', posts_update, name='update'),
    path('delete/<int:id>', posts_delete, name='delete'),

]











