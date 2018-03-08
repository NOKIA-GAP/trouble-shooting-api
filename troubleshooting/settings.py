# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
Django settings for troubleshooting project.

Generated by 'django-admin startproject' using Django 1.11.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users.apps.UsersConfig',
    'actividades.apps.ActividadesConfig',
    'solicitudeshw.apps.SolicitudeshwConfig',
    'estaciones.apps.EstacionesConfig',
    'asignaciones.apps.AsignacionesConfig',
    'conceptos.apps.ConceptosConfig',
    'reportes.apps.ReportesConfig',
    'notificaciones.apps.NotificacionesConfig',
    'fallas.apps.FallasConfig',
    'incidentes.apps.IncidentesConfig',
    'comentarios.apps.ComentariosConfig',
    'alertas.apps.AlertasConfig',
    'nokiagi',
    'django_filters',
    'import_export',
    'crispy_forms',
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

ROOT_URLCONF = 'troubleshooting.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ os.path.join(BASE_DIR, 'templates') ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'incidentes.context_processors.notificacion_incidentes_npo',
                'incidentes.context_processors.notificacion_incidentes_ni',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'troubleshooting.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

class NokiaGiRouter(object):

    def db_for_read(model, **hints):
        if model._meta.app_label == 'nokiagi':
            return 'nokiagi_db'
        return None

DATABASE_ROUTERS = [ NokiaGiRouter, ]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USERNAME'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'PORT': '3306',
        'HOST': os.getenv('DB_HOST'),
    },
    'nokiagi_db': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('NOKIAGI_DB_NAME'),
        'USER': os.getenv('NOKIAGI_DB_USERNAME'),
        'PASSWORD': os.getenv('NOKIAGI_DB_PASSWORD'),
        'PORT': '3306',
        'HOST': os.getenv('NOKIAGI_DB_HOST'),
        'OPTIONS': {
            'sql_mode':'STRICT_TRANS_TABLES',
        },
    }
}
# DATABASES['default']['HOST'] = os.getenv('HOST')
# if os.getenv('GAE_INSTANCE'):
#     pass
# else:
#     DATABASES['default']['HOST'] = '127.0.0.1'

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'es-CO'

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
if os.getenv('GAE_INSTANCE'):
    STATIC_URL = os.getenv('STATIC_URL')
else:
    STATIC_URL = '/static/'

STATIC_ROOT = 'static/'
IMPORT_EXPORT_USE_TRANSACTIONS = True
IMPORT_EXPORT_TMP_STORAGE_CLASS = 'import_export.tmp_storages.CacheStorage'
DATA_UPLOAD_MAX_NUMBER_FIELDS = None
CRISPY_TEMPLATE_PACK = 'bootstrap4'
DATE_INPUT_FORMATS = ('%d/%m/%y', '%d/%m/%Y', '%y-%m-%d', '%Y-%m-%d')
AUTH_PROFILE_MODULE = 'users.Perfil'
BUCKET_NAME = os.getenv('BUCKET_NAME')
EMAIL_BACKEND = 'sendgrid_backend.SendgridBackend'
SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')

CORS_REPLACE_HTTPS_REFERER      = True
HOST_SCHEME                     = "https://"
SECURE_PROXY_SSL_HEADER         = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT             = True
SESSION_COOKIE_SECURE           = True
CSRF_COOKIE_SECURE              = True
SECURE_HSTS_INCLUDE_SUBDOMAINS  = True
SECURE_HSTS_SECONDS             = 1000000
SECURE_FRAME_DENY               = True
SECURE_REDIRECT_EXEMPT = ["actualizacion", "creacion", "normalizacion"]
# SECURE_REDIRECT_EXEMPT = ["^actualizacion/", "^creacion/"]

try:
    from local_settings import *
except ImportError:
    pass
