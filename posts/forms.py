from django import forms
from django.forms import TextInput, Textarea, SelectDateWidget, Select
from .models import Post



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'category', 'content', 'published', 'image']

        widgets = {
            'title': TextInput(attrs={'class':'form-control'}),
            'category': Select(attrs={'class':'form-control'}),
            'published': SelectDateWidget(attrs={'class':'form-control'}),
            'content': Textarea(attrs={'class':'form-control'}),
        }
