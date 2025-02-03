from django import forms
from .models import Blog, Post

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title']
        labels = {'title': ''}

class 