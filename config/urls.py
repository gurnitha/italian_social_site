# config/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # admin app
    path('admin/', admin.site.urls),
    
    # core app
    path('', include('app.core.urls')),

    # accounts app
    path('accounts/', include('app.accounts.urls')),
    
    # django user auth
    path('accounts/', include('django.contrib.auth.urls')),
]
