from django.contrib import admin
from .models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'leave_a_message', 'timestamp', 'content_type',
                    'object_id', 'content_object', 'parent']


admin.site.register(Comment, CommentAdmin)