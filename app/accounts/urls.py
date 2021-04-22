# app/accounts/urls.py

from django.urls import path
from app.accounts.views import registrazioneView

urlpatterns = [
    path('registrazione/', 
    	registrazioneView,
    	name='registrazione_view'),
]
