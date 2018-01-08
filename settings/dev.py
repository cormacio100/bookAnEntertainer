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
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
    },
    'handlers': {
        'null': {
            'level':'DEBUG',
            'class':'django.utils.log.NullHandler',
        },
        'logfile': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': SITE_ROOT + "/logfile",
            'maxBytes': 50000,
            'backupCount': 2,
            'formatter': 'standard',
        },
        'console':{
            'level':'INFO',
            'class':'logging.StreamHandler',
            'formatter': 'standard'
        },
    },
    'loggers': {
        'django': {
            'handlers':['console'],
            'propagate': True,
            'level':'WARN',
        },
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'MYAPP': {
            'handlers': ['console', 'logfile'],
            'level': 'DEBUG',
        },
    }
}
"""


#   DEBUG TOOLBAR - needs to go at bottom
def show_toolbar(request):
    if not request.is_ajax(): # and request.user: # and request.user.username == "cormacio":
        return True
    return True


