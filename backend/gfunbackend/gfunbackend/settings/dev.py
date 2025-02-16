from .base import *

DEBUG = True
ALLOWED_HOSTS = ['*']
CORS_ALLOWED_ORIGINS = [
    "http://localhost",
    "http://api.localhost"
]
CORS_ALLOW_METHODS = ["GET", "POST", "PUT", "DELETE", "OPTIONS"]
CORS_ALLOW_HEADERS = ["*"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'grf',
        'USER': 'root',
        'PASSWORD': 'password1',
        'HOST': 'db', 
        'PORT': 3306
    }
}