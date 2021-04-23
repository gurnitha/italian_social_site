# app/core/urls.py

from django.urls import path

from app.core.views import homepage

urlpatterns = [
	path('', homepage, name='homepage'),
]