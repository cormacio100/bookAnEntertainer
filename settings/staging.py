from base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

#   PAYPAL SETTINGS
PAYPAL_NOTIFY_URL = 'https://aac1c9ee.ngrok.io/to-ngrok-or-not-to-ngrok/'   #   ON LOCALHOST NEED TO RUN ngrok AND COPY
                                                                            #  URL AS <NGROK-ADDRESS>/<URL FROM URL.PY>
                                                                            #    HERE
PAYPAL_RECEIVER_EMAIL = 'cormac.music-facilitator@gmail.com'
SITE_URL = 'http://your-heroku-app.herokuapp.com'
ALLOWED_HOSTS.append('your-heroku-app.herokuapp.com')

# Log DEBUG information to the console
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
