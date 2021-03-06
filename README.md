# BUILDING SOCIAL SITE 'FORUM' USING DJANGO 2.2

## 0. INTRODUZIONE AL PROGETTO

## 1. PARTE I - APPLICAZIONE ACCOUNTS

### 1.1 Part I - Create virtual environment
### 1.2 Part I - Create django project 'config' and django app 'accounts'
### 1.3 Part I - Create app 'accounts'

## 2. PARTE II - TEMPLATES

### 2.1 Setting up templates

        modified:   README.md
        modified:   app/accounts/__pycache__/apps.cpython-39.pyc
        modified:   app/accounts/__pycache__/views.cpython-39.pyc
        new file:   app/accounts/templates/accounts/registrazione.html
        modified:   config/__pycache__/settings.cpython-39.pyc
        modified:   config/settings.py
        new file:   templates/base.html

### 2.2 Install django_crispy_forms

		> pip install django_crispy_forms
        modified:   README.md
        modified:   app/accounts/templates/accounts/registrazione.html
        modified:   config/__pycache__/settings.cpython-39.pyc
        modified:   config/settings.py
        modified:   templates/base.html

### 2.3 Adding bootstrap4 pack

        modified:   README.md
        modified:   config/__pycache__/settings.cpython-39.pyc
        modified:   config/settings.py

### 2.4 Testing by registering users

        modified:   README.md
        modified:   app/accounts/templates/accounts/registrazione.html
        modified:   db.sqlite3

### 2.5 Adding navbar

        modified:   app/accounts/templates/accounts/registrazione.html
        modified:   templates/base.html

### Modified README.md

### Modified README.md

### Modified README.md

## 3. PARTE III - TEMPLATES E AUTENTICAZIONE

### 3.1 Adding django auth

	# open: config/urls and add this
    path('accounts/', include('django.contrib.auth.urls')),

	# run server and access this
	http://127.0.0.1:8000/accounts/

	# it returns these
	Using the URLconf defined in config.urls, Django tried these URL patterns, in this order:

	1. admin/
	2. accounts/ registrazione/ [name='registrazione_view']
	3. accounts/ login/ [name='login']
	4. accounts/ logout/ [name='logout']
	5. accounts/ password_change/ [name='password_change']
	6. accounts/ password_change/done/ [name='password_change_done']
	7. accounts/ password_reset/ [name='password_reset']
	8. accounts/ password_reset/done/ [name='password_reset_done']
	9. accounts/ reset/<uidb64>/<token>/ [name='password_reset_confirm']
	10. accounts/ reset/done/ [name='password_reset_complete']

### 3.2 Create login page

	> create: templates/registration/login.html
	> create: templates/registration/logout.html
	> add login template

        modified:   README.md
        modified:   db.sqlite3
        new file:   templates/registration/login.html
        new file:   templates/registration/logout.html

### 3.3 Create logged out page

        modified:   README.md
        modified:   config/__pycache__/settings.cpython-39.pyc
        modified:   config/settings.py
        modified:   db.sqlite3
        new file:   templates/registration/logged_out.html
        new file:   templates/registration/login.html

### 3.4 Adding conditional to login and logout and show the logged in username

		# after logged in, go to : http://127.0.0.1:8000/accounts/registrazione/

        modified:   README.md
        modified:   db.sqlite3
        modified:   templates/base.html

### 3.5 Password change

		# Steps:
		> 1. Create : templates/registration/password_change_done.html
		> 2. Create: templates/registration/password_change_form.html
		> 3. Add template to each of them
		> 4. Login, use the old credentials (admin, admin)
		> 5. After login, go to: http://127.0.0.1:8000/accounts/password_change/
		> 6. Change the password: 
			current password: admin
			new password    : password123~`
		> 7. Result :)
			
        modified:   README.md
        modified:   db.sqlite3
        new file:   templates/registration/password_change_done.html
        new file:   templates/registration/password_change_form.html        

### 3.6 Password reset

        modified:   config/__pycache__/settings.cpython-39.pyc
        modified:   config/settings.py
        modified:   db.sqlite3
        modified:   templates/base.html
        new file:   templates/registration/password_reset_complete.html
        new file:   templates/registration/password_reset_confirm.html
        new file:   templates/registration/password_reset_done.html
        new file:   templates/registration/password_reset_email.html
        new file:   templates/registration/password_reset_form.html        

## 5. PARTE IV - APPLICATZINE CORE E APPLICAZIONE FORUM

### 5.1 Create new apps called 'core' and 'forum'

        > src
        > mkdir core
        > mkdir forum
        > python manage.py startapp core app\core
        > python manage.py startapp forum app\forum 

### 5.2 Create and register templates for core's and forum's apps

        modified:   README.md
        modified:   config/__pycache__/settings.cpython-39.pyc
        modified:   config/settings.py        

### 5.3 Create homepage (redirect to homepage after logging in)        

        modified:   README.md
        new file:   app/core/__pycache__/urls.cpython-39.pyc
        new file:   app/core/__pycache__/views.cpython-39.pyc
        new file:   app/core/templates/core/homepage.html
        new file:   app/core/urls.py
        modified:   app/core/views.py
        modified:   config/__pycache__/urls.cpython-39.pyc
        modified:   config/urls.py
        modified:   db.sqlite3
        modified:   templates/registration/login.html

### 5.4 Creating User profile page

        modified:   README.md
        modified:   app/core/__pycache__/urls.cpython-39.pyc
        modified:   app/core/__pycache__/views.cpython-39.pyc
        new file:   app/core/templates/core/user_profile.html
        modified:   app/core/urls.py
        modified:   app/core/views.py
        modified:   db.sqlite3

### 5.5 Add link to Profile page and conditional to distinguished Your User Profile and User Profile

        modified:   README.md
        modified:   app/core/__pycache__/urls.cpython-39.pyc
        modified:   app/core/__pycache__/views.cpython-39.pyc
        modified:   app/core/templates/core/user_profile.html
        modified:   app/core/urls.py
        modified:   app/core/views.py
        modified:   db.sqlite3
        modified:   templates/base.html