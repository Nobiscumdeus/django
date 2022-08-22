"""
Django settings for websiteapp project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import django_heroku
from pathlib import Path
import os
#We just allowed importing of heroku


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'aan3opke99(i!dsrdrzlu!je!wqf&4yos9%@f%#^f7=&qpu&*a'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
#The * here is to alllow all hosts
ALLOWED_HOSTS = ['127.0.0.1','nobiscumdeus2022.herokuapp.com']
#ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'dictionary.apps.DictionaryConfig',
    'accounts.apps.AccountsConfig',
    'music.apps.MusicConfig',
    'love.apps.LoveConfig',
    'vote.apps.VoteConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'polls.apps.PollsConfig',
    'Todo.apps.TodoConfig',
    'tutorial.apps.TutorialConfig',
    
    'rest_framework',
    #'base.apps.BaseConfig',
    'base',
    
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'websiteapp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'websiteapp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

''' THIS IS THE DEFAULT DATABASE THAT CAME WITH DJANGO SO YOU CAN RETURN TO IT WHEN DONE WITH MYSQL
#Database I added to connect to mysql, it can be later removed --meanwhile it won't work since i don't 
# have mysql installed on this system 
DATABASES={
   'default':{
       'ENGINE':'django.db.backends.mysql',
       'NAME':'djangodb',
       'USER':'root',
       'PASSWORD':'',
       'HOST':'localhost',
       'PORT':'3306'
   }
}
'''



# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


#Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

STATIC_URL = '/static/'
#STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
STATIC_ROOT=os.path.join(BASE_DIR,'root')

STATICFILES_DIRS=[
    os.path.join(BASE_DIR,'static'),
    os.path.join(BASE_DIR,'bootstrap'),
]
MEDIA_URL='/images/'

#LOGIN_REDIRECT_URL="home" #return to this when you are done
#LOGOUT_REDIRECT_URL="login" # return to this when done with the code below 
LOGIN_REDIRECT_URL='accounts/dashboard'

#We are just adding this configuration below for heroku
django_heroku.settings(locals())

#We may later add this to the procfile app
#web: gunicorn websiteapp.wsgi:application--log-file-