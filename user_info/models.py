from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_image = models.ImageField(upload_to='profile_image', blank=True)
    profile_name = models.CharField(blank=True, max_length=50)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.profile_name
