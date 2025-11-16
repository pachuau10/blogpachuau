from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField


# -------------------------------------------------------------
# CATEGORY
# -------------------------------------------------------------
class Category(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField(unique=True)

    # FIX → Cloudinary instead of ImageField
    thumbnail_img = CloudinaryField(
        'image',
        folder='category_img',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title


# -------------------------------------------------------------
# POST
# -------------------------------------------------------------
class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    overview = models.TextField(max_length=300)
    content = RichTextField()

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)

    # Already correct → Cloudinary
    thumbnail_img = CloudinaryField(
        'image',
        folder='post_img',
        blank=True,
        null=True
    )

    featured = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title


# -------------------------------------------------------------
# PROFILE
# -------------------------------------------------------------
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # FIX → Cloudinary instead of ImageField
    profile_picture = CloudinaryField(
        'image',
        folder='profile_img',
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.user.username} Profile"
