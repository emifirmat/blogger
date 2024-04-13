from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import Http404

from .forms import BlogForm, PostForm
from .models import Blog, Post

# Create your views here.
def check_blog_post(blog, post):
    """check that the post belong to the blog"""
    if post.blog != blog:
        raise Http404
    

def check_blog_owner(request, blog):
    """Check that the user is the owner of the blog"""
    if blog.owner != request.user:
        raise Http404


def index(request):
    """Home page"""
    blogs = Blog.objects.all().order_by("-date")
    posts = Post.objects.all().order_by("-date")
    
    if len(posts) > 5:
        posts = posts[:5]

    if len(blogs) > 5:
        blogs = blogs[:5]
    
    return render(request, "blogs/index.html", {
        "blogs": blogs,
        "posts": posts,
    })


def blogs(request):
    """Show list of all the blogs ordered by creation time"""
    blogs = Blog.objects.all().order_by("-date")
    return render(request, "blogs/blogs.html", {
        "blogs": blogs,
    })


def blog(request, blog_id):
    """ Show a particular blog with its posts"""
    blog = Blog.objects.get(pk=blog_id)
    posts = blog.posts.all().order_by("-date")
    return render(request, "blogs/blog.html",{
        "blog": blog,
        "posts": posts,
    })


@login_required
def new_blog(request):
    """Create a New Blog"""
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.owner = request.user
            form.save()
            return redirect("blogs:index")
    else:
        form = BlogForm()
    
    return render(request, "blogs/new_blog.html",{
        "form": form,
    })


def post(request, blog_id, post_id):
    """Show a particular post from a particular blog"""
    blog = Blog.objects.get(pk=blog_id)
    post = Post.objects.get(pk=post_id)
    check_blog_post(blog, post)

    return render(request, "blogs/post.html", {
        "post": post,
        "blog": blog,
    })


@login_required
def new_post(request, blog_id):
    """Create a new post for a particular blog"""
    blog = Blog.objects.get(pk=blog_id)
    check_blog_owner(request, blog)

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.blog = blog
            new_post.save()

            return redirect("blogs:blog", blog_id=blog.id)
    else:
        form = PostForm()

    return render(request, "blogs/new_post.html",{
        "form": form,
        "blog": blog,
    })


@login_required
def edit_post(request, blog_id, post_id):
    """Edit an existing post"""
    blog = Blog.objects.get(pk=blog_id)
    post = Post.objects.get(pk=post_id)
    check_blog_post(blog, post)
    check_blog_owner(request, blog)
    

    if request.method == "POST":
        form = PostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("blogs:post", blog_id=blog.id, post_id=post.id)
    else:
        form = PostForm(instance=post)

    return render(request, "blogs/edit_post.html",{
        "form": form,
        "blog": blog,
        "post": post,
    })