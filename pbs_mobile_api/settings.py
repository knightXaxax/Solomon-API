"""
Django settings for pbs_mobile_api project.

Generated by 'django-admin startproject' using Django 3.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'gd&p&7wzp5hqs-6ve9pfg!y92(e7z-rpci7z^hq718hdr6yjje'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["192.168.43.61", "127.0.0.1", "192.168.0.17", "192.168.43.10", "192.168.43.11"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'login',
    'so_list'
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

ROOT_URLCONF = 'pbs_mobile_api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'pbs_mobile_api.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'employees',
        # Development Laptop
        # 'HOST': '127.0.0.1',
        # 'PORT': '3306',
        # 'USER': 'than',
        # 'PASSWORD': '467612',
        
        # Development Desktop
        'HOST': 'localhost',
        'PORT': '3306',
        'USER': 'root',
        'PASSWORD': '',

        # Production Server
        # 'HOST': '192.168.43.61',
        # 'PORT': '3306',
        # 'USER': 'than',
        # 'PASSWORD': '467612',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    },
    'employees': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'employees',
        # Development Laptop
        # 'HOST': '127.0.0.1',
        # 'PORT': '3306',
        # 'USER': 'than',
        # 'PASSWORD': '467612',
        
        # Development Desktop
        'HOST': 'localhost',
        'PORT': '3306',
        'USER': 'root',
        'PASSWORD': '',

        # Production Server
        # 'HOST': '192.168.43.61',
        # 'PORT': '3306',
        # 'USER': 'than',
        # 'PASSWORD': '467612',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    },
    'orders': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'orders',
        # Development Laptop
        # 'HOST': '127.0.0.1',
        # 'PORT': '3306',
        # 'USER': 'than',
        # 'PASSWORD': '467612',
        
        # Development Desktop
        'HOST': 'localhost',
        'PORT': '3306',
        'USER': 'root',
        'PASSWORD': '',

        # Production Server
        # 'HOST': '192.168.43.61',
        # 'PORT': '3306',
        # 'USER': 'than',
        # 'PASSWORD': '467612',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    },
    'items': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'items',
        # Development Laptop
        # 'HOST': '127.0.0.1',
        # 'PORT': '3306',
        # 'USER': 'than',
        # 'PASSWORD': '467612',
        
        # Development Desktop
        'HOST': 'localhost',
        'PORT': '3306',
        'USER': 'root',
        'PASSWORD': '',

        # Production Server
        # 'HOST': '192.168.43.61',
        # 'PORT': '3306',
        # 'USER': 'than',
        # 'PASSWORD': '467612',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    },
    'customers': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'customers',
        # Development Laptop
        # 'HOST': '127.0.0.1',
        # 'PORT': '3306',
        # 'USER': 'than',
        # 'PASSWORD': '467612',
        
        # Development Desktop
        'HOST': 'localhost',
        'PORT': '3306',
        'USER': 'root',
        'PASSWORD': '',

        # Production Server
        # 'HOST': '192.168.43.61',
        # 'PORT': '3306',
        # 'USER': 'than',
        # 'PASSWORD': '467612',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')