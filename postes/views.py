from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q, Count
from .models import Category, Post
from django.core.paginator import Paginator

def homepage(request):
    posts = Post.objects.order_by('-created_at')
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    recent_posts = Post.objects.order_by('-created_at')[:5]
    all_categories = Category.objects.annotate(post_count=Count('post')).filter(post_count__gt=0)

    # Use first post for OG, fallback if empty
    first_post = posts.first() if posts.exists() else None

    context = {
        'posts': page_obj,
        'recent_posts': recent_posts,
        'all_categories': all_categories,
        'og_post': first_post,
    }
    return render(request, 'postes/index.html', context)


def post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    recent_posts = Post.objects.order_by('-created_at')[:5]
    all_categories = Category.objects.annotate(post_count=Count('post')).filter(post_count__gt=0)

    context = {
        'post': post,
        'recent_posts': recent_posts,
        'all_categories': all_categories,
        'og_post': post,
    }
    return render(request, 'postes/post.html', context)


def category_Post(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(categories__in=[category]).order_by('-created_at')

    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    recent_posts = Post.objects.order_by('-created_at')[:5]
    all_categories = Category.objects.annotate(post_count=Count('post')).filter(post_count__gt=0)

    context = {
        'category': category,
        'posts': posts,
        'recent_posts': recent_posts,
        'all_categories': all_categories,
        'og_post': posts[0] if posts else None,
    }
    return render(request, 'postes/category.html', context)


def search(request):
    query = request.GET.get('q')
    if not query:
        return redirect('homepage')

    posts = Post.objects.filter(
        Q(title__icontains=query) | Q(overview__icontains=query)
    ).distinct().order_by('-created_at')

    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    recent_posts = Post.objects.order_by('-created_at')[:5]
    all_categories = Category.objects.annotate(post_count=Count('post')).filter(post_count__gt=0)

    context = {
        'query': query,
        'posts': posts,
        'recent_posts': recent_posts,
        'all_categories': all_categories,
        'og_post': posts[0] if posts else None,
    }
    return render(request, 'postes/search.html', context)


def custom_404(request, exception):
    return render(request, '404.html', status=404)


def custom_500(request):
    return render(request, '500.html', status=500)
