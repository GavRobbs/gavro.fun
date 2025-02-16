from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path("", include("api.urls")),
]

if settings.ENABLE_ADMIN:
    urlpatterns.append(path('admin/', admin.site.urls))

