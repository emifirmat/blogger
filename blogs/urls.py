"""urls patterns for blogs app"""
from django.urls import path

from . import views


app_name = "blogs"
urlpatterns = [
    # Home page
    path("", views.index, name="index"),
    # Blogs page
    path("blogs", views.blogs, name="blogs"),
    # Blog page
    path("blogs/<int:blog_id>", views.blog, name="blog"),
    # Create a new blog
    path("new_blog", views.new_blog, name="new_blog"),
    # Post page
    path("blogs/<int:blog_id>/<int:post_id>", views.post, name="post"),
    # Create new post
    path("blogs/<int:blog_id>/new_post", views.new_post, name="new_post"),
    # Edit post
    path("blogs/<int:blog_id>/<int:post_id>/edit", views.edit_post, name="edit_post"),
]