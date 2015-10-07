"""
Django settings for pvsat project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'c*&!z_lk3in@$!4*k(3*%7ogz))9%3v_w16)9$6#j7ht9k8y%3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# TEMPLATES

TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates/')
TEMPLATE_DIRS = ('',
        TEMPLATE_PATH,
		os.path.join(BASE_DIR, 'authors/templates/'),
                os.path.join(BASE_DIR, 'blog/templates/'),
                os.path.join(BASE_DIR, 'bursary/templates/'),
        )

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sponsors',
    'programme',
    'committee',
    'exhibitors',
    'blog',
    'authors',
    'message',
    'forms',
    'venue',
    'bursary',

    'sorl.thumbnail'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'pvsat.urls'

WSGI_APPLICATION = 'pvsat.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATIC_PATH = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = (
        STATIC_PATH,
        )
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

LOGIN_URL = '/authors/login/'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'rob.pvsat@gmail.com'
EMAIL_HOST_PASSWORD = 'm8ly4CeL30{95QA'
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

THUMBNAIL_DEBUG = True
