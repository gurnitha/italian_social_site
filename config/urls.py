# config/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('app.accounts.urls')),
    # django auth
    path('accounts/', include('django.contrib.auth.urls')),
]
