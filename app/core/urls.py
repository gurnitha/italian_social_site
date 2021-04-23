# app/core/urls.py

from django.urls import path

from app.core.views import (
	homepage,
	userProfileView)

urlpatterns = [
	path('', homepage, name='homepage'),
	# http://127.0.0.1:8000/user/1/
	path('user/<int:user_id>/', userProfileView, name='user_profile'),
]