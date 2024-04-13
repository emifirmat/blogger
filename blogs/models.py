from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Blog(models.Model):
    """A blog"""
    name = models.CharField(max_length=80)
    date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class Post(models.Model):
    """A post made in a blog"""
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="posts")
    title = models.CharField(max_length=80)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"