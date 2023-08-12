from django.shortcuts import render
from .models import Post, Category, Author


def blog(request):
    """Renders all catagory of blog posts"""
    categories = Category.objects.all()[0:3]
    featured = Post.objects.filter(featured=True)
    latest = Post.objects.order_by('-timestamp')[0:3]
    context = {
        'object_list': featured,
        'latest': latest,
        'categories': categories,
    }
    return render(request, 'blog.html', context)


def post(request, slug):
    """Renders the post detail page"""
    post = Post.objects.get(slug=slug)
    context = {
        'post': post,
    }
    return render(request, 'post_detail.html', context)


def category_post_list(request, slug):
    """Will render the posts by category in future versions"""
    category = Category.objects.get(slug=slug)
    posts = Post.objects.filter(categories__in=[category])
    context = {
        'posts': posts,
    }
    return render(request, 'post_list.html', context)


def allposts(request):
    """renders all posts"""
    posts = Post.objects.order_by('-timestamp')
    context = {
        'posts': posts,
    }
    return render(request, 'all_posts.html', context)
