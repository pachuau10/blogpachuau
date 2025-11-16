import os
from pathlib import Path
import dj_database_url
from decouple import config
import cloudinary
import cloudinary.uploader
import cloudinary.api

# -----------------------------------------------------------
# BASE DIR
# -----------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# -----------------------------------------------------------
# SECURITY
# -----------------------------------------------------------
SECRET_KEY = config("SECRET_KEY", default="change-me")
DEBUG = config("DEBUG", default=True, cast=bool)
ALLOWED_HOSTS = ["*"]

# -----------------------------------------------------------
# INSTALLED APPS
# -----------------------------------------------------------
INSTALLED_APPS = [
    # Django default apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Your app
    'postes',

    # Cloudinary
    'cloudinary',
    'cloudinary_storage',

    # CKEditor
    'ckeditor',
    'ckeditor_uploader',
]

# -----------------------------------------------------------
# MIDDLEWARE
# -----------------------------------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# -----------------------------------------------------------
# URLS
# -----------------------------------------------------------
ROOT_URLCONF = 'myblog.urls'

# -----------------------------------------------------------
# TEMPLATES
# -----------------------------------------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# -----------------------------------------------------------
# WSGI
# -----------------------------------------------------------
WSGI_APPLICATION = 'myblog.wsgi.application'

# -----------------------------------------------------------
# DATABASE — NeonDB PostgreSQL
# -----------------------------------------------------------
DATABASES = {
    'default': dj_database_url.parse(
        config("DATABASE_URL"),
        conn_max_age=600,
        ssl_require=True
    )
}

# -----------------------------------------------------------
# PASSWORD VALIDATION
# -----------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# -----------------------------------------------------------
# LANGUAGE / TIME
# -----------------------------------------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# -----------------------------------------------------------
# STATIC (Cloudinary)
# -----------------------------------------------------------
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'

# -----------------------------------------------------------
# MEDIA (Cloudinary)
# -----------------------------------------------------------
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# ❗ REMOVE THESE (Cloudinary does not use local media)
# MEDIA_URL = '/media/'
# MEDIA_ROOT = BASE_DIR / "media"

# -----------------------------------------------------------
# CLOUDINARY CONFIG
# -----------------------------------------------------------
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': config("CLOUD_NAME"),
    'API_KEY': config("CLOUD_API_KEY"),
    'API_SECRET': config("CLOUD_API_SECRET"),
}

cloudinary.config(
    cloud_name=config("CLOUD_NAME"),
    api_key=config("CLOUD_API_KEY"),
    api_secret=config("CLOUD_API_SECRET"),
)

# -----------------------------------------------------------
# CKEDITOR SETTINGS
# -----------------------------------------------------------
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_IMAGE_BACKEND = "pillow"

# -----------------------------------------------------------
# DEFAULT PRIMARY KEY FIELD TYPE
# -----------------------------------------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
