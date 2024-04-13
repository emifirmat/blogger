"""Forms for views.py of blogs app"""
from django import forms

from .models import Blog, Post


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ["name"]
        labels = {"name": ""}


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content"]
