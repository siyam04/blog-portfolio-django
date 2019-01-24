from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.urls import reverse

from comments.models import Comment
from .utils import get_read_time
from django.conf import settings
from django.utils import timezone
from markdown_deux import markdown
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.utils.safestring import mark_safe

# from user_info.models import Profile


class Category(models.Model):
    category_name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_name


class Post(models.Model):
    user = models.ForeignKey('user_info.Profile', on_delete=models.CASCADE, related_name='post')
    title = models.CharField(max_length=120)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='post')
    content = models.TextField(max_length=3000, blank=False)
    slug = models.SlugField(unique=True, null=True, blank=True)
    draft = models.BooleanField(default=True)
    read_time = models.IntegerField(default=0)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    published = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now)
    image = models.ImageField(null=True, blank=True, upload_to='image')

    class Meta:
        ordering = ['-created', '-updated']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("details", kwargs={"id": self.id})

    @property
    def comments(self):
        instance = self
        qs = Comment.objects.filter_by_instance(instance)
        return qs

    @property
    def get_content_type(self):
        instance = self
        content_type = ContentType.objects.get_for_model(instance.__class__)
        return content_type

# Counting the total views
    def get_markdown(self):
        content = self.content
        markdown_text = markdown(content)
        return mark_safe(markdown_text)


# Signals Passing before saving to the DataBase
def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug and instance.title:
        instance.slug = slugify(instance.title)
    if instance.content:
        html_string = instance.get_markdown()
        read_time_var = get_read_time(html_string)
        instance.read_time = read_time_var


pre_save.connect(pre_save_receiver, sender=Post)
