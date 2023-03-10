"""
Django settings for inventory_main project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os
from dotenv import load_dotenv
import boto3

load_dotenv()

AWS_REGION_NAME = str(os.getenv('AWS_REGION_NAME'))
boto3_logs_client = boto3.client("logs", region_name=AWS_REGION_NAME)
#
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'root': {
#         'level': 'DEBUG',
#         # Adding the watchtower handler here causes all loggers in the project that
#         # have propagate=True (the default) to send messages to watchtower. If you
#         # wish to send only from specific loggers instead, remove "watchtower" here
#         # and configure individual loggers below.
#         # 'handlers': ['watchtower', 'console'],
#         'handlers': ['console'],
#     },
#     'handlers': {
#         'console': {
#             'class': 'logging.StreamHandler',
#         },
#         # 'watchtower': {
#         #     'class': 'watchtower.CloudWatchLogHandler',
#         #     'boto3_client': boto3_logs_client,
#         #     'log_group_name': 'inventoryManagementApp',
#         #     # Decrease the verbosity level here to send only those logs to watchtower,
#         #     # but still see more verbose logs in the console. See the watchtower
#         #     # documentation for other parameters that can be set here.
#         #     'level': 'DEBUG'
#         # }
#     },
#     'loggers': {
#         # In the debug server (`manage.py runserver`), several Django system loggers cause
#         # deadlocks when using threading in the logging handler, and are not supported by
#         # watchtower. This limitation does not apply when running on production WSGI servers
#         # (gunicorn, uwsgi, etc.), so we recommend that you set `propagate=True` below in your
#         # production-specific Django settings file to receive Django system logs in CloudWatch.
#         'django': {
#             'level': 'DEBUG',
#             'handlers': ['console'],
#             'propagate': False
#         }
#         # Add any other logger-specific configuration here.
#     }
# }


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = str(os.getenv('SECRET_KEY'))

# SECURITY WARNING: don't run with debug turned on in production!
if  os.getenv('IS_DEVELOPMENT', 'False').lower() == 'true':
    DEBUG = True
else:
    DEBUG = False
ALLOWED_HOSTS = [os.getenv('APP_HOST')]


# Application definition

INSTALLED_APPS = [
    'products.apps.ProductsConfig',
    'orders.apps.OrdersConfig',
    'api.apps.ApiConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework'
]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'inventory_main.urls'

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

WSGI_APPLICATION = 'inventory_main.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

# STATIC_ROOT = BASE_DIR / "staticfiles"
STATIC_ROOT = "staticfiles"

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {}