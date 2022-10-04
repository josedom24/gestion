"""
Django settings for gestion project.

Generated by 'django-admin startproject' using Django 1.10.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'd$ug$)j1jhr2%z4gnpbc9^v^@4*sbu5we9nt_dtg72x7e+xq^('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['gestion.gonzalonazareno.org']


# Application definition

INSTALLED_APPS = [
    'centro.apps.CentroConfig',
    'convivencia.apps.ConvivenciaConfig',
    'pdf.apps.PdfConfig',
    'registro.apps.RegistroConfig',
    'correo.apps.CorreoConfig',
    'absentismo.apps.AbsentismoConfig',
#    'django_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'gestion.urls'

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

WSGI_APPLICATION = 'gestion.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'basededatos/db.sqlite3'),
    },
    'db2017': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'basededatos/db2017.sqlite3'),
    },
    'db2018': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'basededatos/db2018.sqlite3'),
    },
    'db2019': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'basededatos/db2019.sqlite3'),
    },
    'db2020': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'basededatos/db2020.sqlite3'),
    },
    'db2021': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'basededatos/db2021.sqlite3'),
    },
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'es-es'

TIME_ZONE = 'Europe/Madrid'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR,"static"),
)
import ConfigParser
configuracion = ConfigParser.ConfigParser()
configuracion.read(os.path.join(BASE_DIR, 'gestion.cfg'))
EMAIL_HOST = configuracion.get('bd','EMAIL_HOST')
EMAIL_HOST_USER = configuracion.get('bd','EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = configuracion.get('bd','EMAIL_HOST_PASSWORD')
EMAIL_PORT = configuracion.get('bd','EMAIL_PORT')
EMAIL_USE_TLS = configuracion.get('bd','EMAIL_USE_TLS')






















#import logging.config
#LOGGING = {
#    'version': 1,
#    'disable_existing_loggers': False,
#    'handlers': {
#        'file': {
#            'level': 'DEBUG',
#            'class': 'logging.FileHandler',
#            'filename': os.path.join(BASE_DIR, 'gestion.log')
#        }
#
#    },
#    'loggers': {
#        'django': {
#            'handlers': ['file'],
#            'level': 'CRITICAL',
#            'propagate': True,
#        },
#        
#        'xhtml2pdf': {
#            'handlers': ['file'],
#            'level': 'DEBUG'
#       },
#    },
#}






