from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q, Count
from django.core.paginator import Paginator
from .models import Category, Post
from cloudinary.utils import cloudinary_url

# --- Helper for OG images ---
def get_og_image(post):
    # Replace 'image' with your actual Post model image field
    image_field_name = 'image'
    if hasattr(post, image_field_name) and getattr(post, image_field_name):
        return cloudinary_url(getattr(post, image_field_name).name, format="auto", width=1200, height=630)[0]
    return None

# --- Homepage ---
def homepage(request):
    posts = Post.objects.order_by('-created_at')
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    recent_posts = Post.objects.order_by('-created_at')[:5]
    all_categories = Category.objects.annotate(post_count=Count('post')).filter(post_count__gt=0)

    # Safe OG image for first post
    og_image = None
    if page_obj and page_obj.object_list:
        first_post = page_obj.object_list[0]
        og_image = get_og_image(first_post)

    context = {
        'posts': page_obj,
        'recent_posts': recent_posts,
        'all_categories': all_categories,
        'og_image': og_image,
    }
    return render(request, 'postes/index.html', context)

# --- Single post detail ---
def post(request, slug):
    post = get_object_or_404(Post, slug=slug)

    recent_posts = Post.objects.order_by('-created_at')[:5]
    all_categories = Category.objects.annotate(post_count=Count('post')).filter(post_count__gt=0)

    # Safe OG image for this post
    og_image = get_og_image(post)

    context = {
        'post': post,
        'recent_posts': recent_posts,
        'all_categories': all_categories,
        'og_image': og_image,
    }
    return render(request, 'postes/post.html', context)

# --- About page ---
def about(request):
    return render(request, 'postes/about.html')

# --- Category posts ---
def category_Post(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(categories__in=[category]).order_by('-created_at')

    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    recent_posts = Post.objects.order_by('-created_at')[:5]
    all_categories = Category.objects.annotate(post_count=Count('post')).filter(post_count__gt=0)

    # Safe OG image for first post in this category
    og_image = None
    if posts and posts.object_list:
        og_image = get_og_image(posts.object_list[0])

    context = {
        'category': category,
        'posts': posts,
        'recent_posts': recent_posts,
        'all_categories': all_categories,
        'og_image': og_image,
    }
    return render(request, 'postes/category.html', context)

# --- Search ---
def search(request):
    query = request.GET.get('q')
    if not query:
        return redirect('homepage')

    posts = Post.objects.filter(
        Q(title__icontains=query) |
        Q(overview__icontains=query)
    ).distinct().order_by('-created_at')

    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    recent_posts = Post.objects.order_by('-created_at')[:5]
    all_categories = Category.objects.annotate(post_count=Count('post')).filter(post_count__gt=0)

    # Safe OG image for first post in search results
    og_image = None
    if posts and posts.object_list:
        og_image = get_og_image(posts.object_list[0])

    context = {
        'query': query,
        'posts': posts,
        'recent_posts': recent_posts,
        'all_categories': all_categories,
        'og_image': og_image,
    }
    return render(request, 'postes/search.html', context)

# --- Custom error pages ---
def custom_404(request, exception):
    return render(request, '404.html', status=404)

def custom_500(request):
    return render(request, '500.html', status=500)
