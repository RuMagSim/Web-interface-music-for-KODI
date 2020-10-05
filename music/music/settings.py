"""
Django settings for music project.

"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: don't run with debug turned on in production!
SECRET_KEY = 'music'

DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'music.folder'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'music.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
				'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'music.wsgi.application'


# Database default login/password in mySQL from confuration setting KODI 
#(advancedsettings.xml https://kodi.wiki/view/MySQL/Setting_up_MySQL). 
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    
	'default': {
	    'ENGINE': 'django.db.backends.mysql',
		'NAME': 'MyMusic60',
		'USER': 'kodi',
		'PASSWORD': 'kodi',
		'HOST': 'localhost',
		'PORT': '3306',
		
   }		
}



# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, favicon in file detault.conf Syntax:alias Apache Module mod_alias )

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
REPOSITORY_ROOT = os.path.dirname(BASE_DIR)

#  Virtualhost in apache2 from open link media 
MEDIA_URL = 'You_ip_address:port'
