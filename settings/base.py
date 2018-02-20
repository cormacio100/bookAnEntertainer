"""
Django settings for bookAnEntertainer project.

Generated by 'django-admin startproject' using Django 1.11.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import env     #   Needs to be added for DEV and commented out for Staging


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

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
    'storages',
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
                'django.template.context_processors.media'
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

STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')

"""
STATICFILES_DIRS IS FOR OUTPUTS
It is a set of places to look for static files
"""
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)
#STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

"""
MEDIA FILE STORAGE SETTINGS FOR LOCAL USE
"""
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
MEDIA_URL = '/media/'    #   Can access images directly in browser with address <host>:<port>/pics/media/<folder>/<image>

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

#############################################################
#   AWS (S3 BUCKET) SETTINGS
#   -   ENABLES MEDIA AND STATIC FILES TO BE STORED ON S3
#############################################################

AWS_S3_OBJECT_PARAMETERS = {
    'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
    'CacheControl': 'max-age=94608000',
}

AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME")
AWS_S3_REGION_NAME = os.environ.get("AWS_S3_REGION_NAME")
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")

#   TELL DJANGO-STORAGES THE DOMAIN TO USE TO REFER TO STATIC FILES
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

#   Tell the staticfiles app to use S3Boto3 storage when writing the collected static files
#   (when you run the command 'python manage.py collectstatic')
#DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

#   TELL THE STATICFILES APP TO USE S3BOTO3 STORAGE WHEN WRITING THE COLLECTED STATIC FILES
#   WHEN YOU RUN 'collectstatic'
#STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_LOCATION = 'static'
STATICFILES_STORAGE = 'custom_storages.StaticStorage'

#   WHEN A USER UPLOADS AN AVATAR, IT SHOULD GO INTO /MEDIA/ IN OUR S3 BUCKET
#   WHEN WE DISPLAY THE IMAGE ON A PAGE, THE IMAGE URL WILL INCLUDE '/MEDIA/'
MEDIAFILES_LOCATION = 'media'
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'

"""
UPLOAD AND URL LOCATIONS FOR ALL IMAGES USING DEFAULT_FILE_STORAGE AS THE DEFAULT LOCATION
"""
"""
FS_PROFILE_IMG_UPLOADS = os.path.join(DEFAULT_FILE_STORAGE,'profile/')
FS_PROFILE_IMG_URL = os.path.join(DEFAULT_FILE_STORAGE,'profile/')
FS_IMG1_UPLOADS = os.path.join(DEFAULT_FILE_STORAGE,'img1/')
FS_IMG1_URL = os.path.join(DEFAULT_FILE_STORAGE,'img1/')
"""
"""
FS_PROFILE_IMG_UPLOADS = 'profile/'
FS_PROFILE_IMG_URL = 'profile/'
FS_IMG1_UPLOADS = 'image1/'
FS_IMG1_URL = 'image1/'
"""
