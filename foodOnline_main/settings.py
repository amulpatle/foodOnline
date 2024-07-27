"""
Django settings for foodOnline_main project.

Generated by 'django-admin startproject' using Django 5.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
from decouple import config
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', cast=bool)

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'accounts',
    'vendor',
    'menu',
    'marketplace',
    'django.contrib.gis',
    'customers',
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

ROOT_URLCONF = 'foodOnline_main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'accounts.context_processors.get_vendor',
                'marketplace.context_processor.get_cart_counter',
                'marketplace.context_processor.get_cart_amounts',
                'accounts.context_processors.get_google_api',
                
            ],
        },
    },
]

WSGI_APPLICATION = 'foodOnline_main.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.postgresql',
        'ENGINE':'django.contrib.gis.db.backends.postgis',
        'NAME': config('DB_NAME'),
        'USER':config('DB_USER'),
        'PASSWORD':config('DB_PASSWORD'),
        'HOST':config('DB_HOST'),
    }
}

AUTH_USER_MODEL = 'accounts.user'

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'static'
STATICFILES_DIRS = [
    'foodOnline_main/static'
]

# Media files configuration

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.ERROR:'danger',
}

# Email configuration

# EMAIL_HOST = config('EMAIL_HOST')
# EMAIL_PORT = config('EMAIL_PORT',cast=int)
# EMAIL_HOST_USER = config('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
# EMAIL_USE_TLE = True
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = "tester.gml.69@gmail.com"
EMAIL_HOST_PASSWORD = "aebhuvbfegtjdmdm"
EMAIL_USE_TLS = True  # Corrected setting name
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL = 'foodOnline Marketplace <tester.gml.69@gmail.com'

GOOGLE_API_KEY = config('GOOGLE_API_KEY')

# authentication 

# AUTHENTICATION_BACKENDS = (
#     'aullauth.account_backends.AuthenticationBackend',

# )

# SITE_ID = 1
# LOGIN_REDIRECT_URL = '/'




# this is code from ratan kumar

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# # Path to GDAL library and related files
# os.environ['PATH'] = os.path.join(BASE_DIR, 'env/lib/python3.10/site-packages/osgeo') + ':' + os.environ['PATH']
# os.environ['PROJ_LIB'] = os.path.join(BASE_DIR, 'env/lib/python3.10/site-packages/osgeo/data/proj') + ':' + os.environ['PATH']

# # Path to the GDAL shared library file specific to Python
# GDAL_LIBRARY_PATH = os.path.join(BASE_DIR, 'env/lib/python3.10/site-packages/osgeo', '_gdal.cpython-310-x86_64-linux-gnu.so')



# this is  the correct path setup for gdal
# find path for --->PROJ_LIB and put here
# GDAL_LIBRARY_PATH ---> linux use libgdal.so file and window's os use different so find that file using terminal . by using this command--->  find /usr -name "libgdal.so*"
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.environ['PATH'] = os.path.join(BASE_DIR, 'env/lib/python3.10/site-packages/osgeo') + ':' + os.environ['PATH']
os.environ['PROJ_LIB'] = os.path.join(BASE_DIR, '/usr/share/proj/') + ':' + os.environ['PATH']
GDAL_LIBRARY_PATH = os.path.join(BASE_DIR, '/usr/lib/', 'libgdal.so')
