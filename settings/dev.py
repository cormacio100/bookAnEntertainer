from base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

ALLOWED_HOSTS.append('4ae16e54.ngrok.io')

#   DEBUG TOOLBAR SETTINGS

INSTALLED_APPS.append('debug_toolbar')
MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')
DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': 'bookAnEntertainer.settings.show_toolbar',
}

#   PAYPAL SETTINGS
SITE_URL = 'https://127.0.0.1:8000'
PAYPAL_NOTIFY_URL = 'https://aac1c9ee.ngrok.io/to-ngrok-or-not-to-ngrok/'   #   ON LOCALHOST NEED TO RUN ngrok AND COPY
                                                                            #  URL AS <NGROK-ADDRESS>/<URL FROM URL.PY> HERE
PAYPAL_RECEIVER_EMAIL = 'cormac.music-facilitator@gmail.com'

################################################################
#   LOGGING
################################################################
"""
SITE_ROOT = 'https://127.0.0.1:8000'
"""
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}

#   DEBUG TOOLBAR - needs to go at bottom
def show_toolbar(request):
    if not request.is_ajax(): # and request.user: # and request.user.username == "cormacio":
        return True
    return True


