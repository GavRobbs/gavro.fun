from .base import *

DEBUG = False
ALLOWED_HOSTS = ['gavro.fun', 'api.gavro.fun', '127.0.0.1']
CORS_ALLOWED_ORIGINS = [
    'http://localhost:5173',
    'https://gavro.fun'
]

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
SESSION_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_HSTS_SECONDS = 31536000  # Enable HSTS
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True