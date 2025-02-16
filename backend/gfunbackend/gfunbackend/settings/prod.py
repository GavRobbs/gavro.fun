from .base import *

DEBUG = False
ALLOWED_HOSTS = ['api.gavro.fun', 'gavro.fun']
CORS_ALLOWED_ORIGINS = [
    'https://gavro.fun'
]
CORS_ALLOW_METHODS = ["GET", "POST", "PUT", "DELETE", "OPTIONS"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),  # e.g., '127.0.0.1' or 'your-host.com'
        'PORT': config('DB_PORT'),  # Default MySQL port
        'OPTIONS': {
            'ssl': {
                'ca': config('DB_CA_CERT_PATH')
            },
        },
    }
}

# Security settings
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = False
SESSION_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_HSTS_SECONDS = 31536000  # Enable HSTS
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

CSRF_TRUSTED_ORIGINS = [
    "https://gavro.fun",
    "https://api.gavro.fun"
]