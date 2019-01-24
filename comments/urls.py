from .views import (
    comment_delete,
)
from django.urls import path

urlpatterns = [

    path('delete/<int:id>/<int:post_id>', comment_delete, name='comment_delete'),

]











