from base import *
import dj_database_url

DEBUG = False

DATABASES = {
    'default': dj_database_url.config('mysql://b75ca10aad0726:fe49e080@eu-cdbr-west-01.cleardb.com/heroku_d28248eb1f8e96b?')
}

#   PAYPAL SETTINGS
SITE_URL = 'http://book-an-entertainer.herokuapp.com'
PAYPAL_NOTIFY_URL = 'https://book-an-entertainer.herokuapp.com/to-ngrok-or-not-to-ngrok/'   #   ON LOCALHOST NEED TO RUN ngrok AND COPY
                                                                            #  URL AS <NGROK-ADDRESS>/<URL FROM URL.PY>
                                                                            #    HERE
PAYPAL_RECEIVER_EMAIL = 'cormac.music-facilitator@gmail.com'
ALLOWED_HOSTS.append('book-an-entertainer.herokuapp.com')

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
