from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Count, Q
from django.core.paginator import Paginator
from .models import Post, Category

def homepage(request):
    posts = Post.objects.order_by('-created_at')
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    recent_posts = Post.objects.order_by('-created_at')[:5]
    all_categories = Category.objects.annotate(post_count=Count('post')).filter(post_count__gt=0)

    context = {
        'posts': page_obj,
        'recent_posts': recent_posts,
        'all_categories': all_categories,
    }
    return render(request, 'postes/index.html', context)


def post(request, slug):
    post = get_object_or_404(Post, slug=slug)

    recent_posts = Post.objects.order_by('-created_at')[:5]
    all_categories = Category.objects.annotate(post_count=Count('post')).filter(post_count__gt=0)

    # Safe handling of featured_image
    featured_image = getattr(post, 'featured_image', None)

    context = {
        'post': post,
        'featured_image': featured_image,  # pass to template
        'recent_posts': recent_posts,
        'all_categories': all_categories,
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
    }
    return render(request, 'postes/search.html', context)


def about(request):
    return render(request, 'postes/about.html')


def custom_404(request, exception):
    return render(request, '404.html', status=404)


def custom_500(request):
    return render(request, '500.html', status=500)
