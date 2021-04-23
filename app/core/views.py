# app/core/views.py

from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404

# Create your views here.

def homepage(request):
	"""User will redirect to login before seeing the homepage"""
	return render(request, 'core/homepage.html')


# Render User profile  after logging in
# based-on its user_id
# http://127.0.0.1:8000/user/1/	
def userProfileView(request, user_id):
	user = 	get_object_or_404(User, pk=user_id)
	context = {'user':user}
	return render(
		request, 
		'core/user_profile.html',
		context)