"""
Django settings for bookAnEntertainer project.

Generated by 'django-admin startproject' using Django 1.11.7.

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
SECRET_KEY = 'md517-*6s^q(z1$c@ik&*c)veq_s^q%luwar7b6*&g)k*ay7!r'

ALLOWED_HOSTS = ['localhost','127.0.0.1','bookanentertainer.herokuapp.com']    #   INCLUDE NGROK TO ALLOW PAYPAL TO WORK - this changes each time ngrok is run
SITE_ID =2

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home',
    'entertainers',
    'multiselectfield',
    'user_accounts',
    'django_forms_bootstrap',
    'accounts',
    'rest_framework',
    'paypal.standard.ipn',
    'paypal_store',
    'settings',
]

########################################################################################
#   CUSTOM USER AUTHENTICATION
#   Accounts app Files involved:
#   -   settings.py,
#   -   backends.py,
#   -   forms.py,
#   -   models.py,
#   -   views.py,
#   -   urls.py
#   -   templates

#   TELL DJANGO TO USE accounts.User instead of the default User class for authentication
AUTH_USER_MODEL = 'accounts.User'

#   TELL DJANGO TO OVERRIDE THE DEFAULT get_user AND authenticate METHODS
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'accounts.backends.EmailAuth',
)
########################################################################################

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware'
]

ROOT_URLCONF = 'bookAnEntertainer.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'bookAnEntertainer.wsgi.application'

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

"""
STATIC_URL should be the URL at which a user / client / browser can reach the static files
that have been aggregated by collectstatic.
"""
STATIC_URL = '/static/'

#   STATIC_ROOT should live outside of your Django project - it is the directory to where your static files
#   are collected
#   for use by a local webserver or similar; Djangos involvement with that directory should end once your static files
#   have been collected there
#   STATIC_ROOT IS FOR INPUTS and is where static files are stored

#SEE https://blog.doismellburning.co.uk/django-and-static-files/

STATIC_ROOT = os.path.join(BASE_DIR,'static')

"""
STATICFILES_DIRS IS FOR OUTPUTS
It is a set of places to look for static files
"""
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)
#STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
MEDIA_URL = '/pics/'    #   Can access images directly in browser with address <host>:<port>/pics/media/<folder>/<image>
MEDIA_ROOT = BASE_DIR

INTERNAL_IPS = ('127.0.0.1',)


###################################################
#   DEV SETTINGS FROM dep.py
###################################################
#   PAYPAL SETTINGS
SITE_URL = 'https://127.0.0.1:8000'
PAYPAL_NOTIFY_URL = 'https://4ae16e54.ngrok.io/to-ngrok-or-not-to-ngrok/'   #   ON LOCALHOST NEED TO RUN ngrok AND COPY
                                                                            #  URL AS <NGROK-ADDRESS>/<URL FROM URL.PY> HERE
PAYPAL_RECEIVER_EMAIL = 'cormac.music-facilitator@gmail.com'
ALLOWED_HOSTS.append('4ae16e54.ngrok.io')