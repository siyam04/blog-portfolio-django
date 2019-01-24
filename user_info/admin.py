from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    """Customizing Admin Interface"""
    list_display_links = ['user']
    list_filter = ['profile_name', 'email']
    search_fields = ['user', 'email']
    list_display = ['id', 'user', 'profile_name', 'email', 'address', 'profile_image']


admin.site.register(Profile, ProfileAdmin)

