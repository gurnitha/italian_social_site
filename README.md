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