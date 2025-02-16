from pathlib import Path
from decouple import config
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('DJANGO_SECRET_KEY', default="fallback_key")

INSTALLED_APPS = [
    'rest_framework',
    'storages',
    'corsheaders',
    'api.apps.ApiConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'gfunbackend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'gfunbackend.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STORAGES = {
    'default': {
        'BACKEND': 'storages.backends.s3.S3Storage',
        'OPTIONS': {
            'access_key' : config('DO_ACCESS_KEY_ID'),
            'secret_key' : config('DO_SECRET_ACCESS_KEY'),
            'bucket_name' : config('DO_BUCKET_NAME'),
            'region_name' : config('DO_REGION_NAME'),
            'endpoint_url' : config('DO_ENDPOINT_URL'),
            'location' : 'media'
        },
        'file_overwrite' : False,
        
    },
    "staticfiles": {
        "BACKEND": "storages.backends.s3.S3Storage",
        'OPTIONS': {
            'access_key' : config('DO_ACCESS_KEY_ID'),
            'secret_key' : config('DO_SECRET_ACCESS_KEY'),
            'bucket_name' : config('DO_BUCKET_NAME'),
            'region_name' : config('DO_REGION_NAME'),
            'endpoint_url' : config('DO_ENDPOINT_URL'),
            'location' : 'media'
        },
        'file_overwrite' : False,
    }
}

# URLs for accessing uploaded files
#MEDIA_URL = f"{config('DO_BUCKET_URL')}/media/"
# Static files (CSS, JS, etc.)
STATIC_URL = f"https://{config('DO_BUCKET_NAME')}.{config('DO_ENDPOINT_URL').replace('https://', '')}/static/"

# Media files (uploads)
MEDIA_URL = f"https://{config('DO_BUCKET_NAME')}.{config('DO_ENDPOINT_URL').replace('https://', '')}/media/"

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")  

ENABLE_ADMIN = config('DJANGO_ENABLE_ADMIN', default="False", cast=bool)