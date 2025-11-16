from django.contrib import admin
# Only import models that still exist in your models.py
from .models import Category, Post 

admin.site.register(Category)
admin.site.register(Post)

# Do NOT register Author, as it no longer exists.