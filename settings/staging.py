from base import *
import dj_database_url

DEBUG = False

DATABASES = {
    #'default': dj_database_url.config('mysql://b75ca10aad0726:fe49e080@eu-cdbr-west-01.cleardb.com/heroku_d28248eb1f8e96b?') # book-an-entertainer
    #'default': dj_database_url.config('mysql://b04dad47c09741:c839778c@eu-cdbr-west-01.cleardb.com/heroku_0ec0fc4d7ab16c5?') # bookanentertainer
    'default': dj_database_url.config('mysql://b14829df6b68b7:545112f9@eu-cdbr-west-01.cleardb.com/heroku_d3c5ad404e32217?') # bookanentertainer
}

ALLOWED_HOSTS.append('bookanentertainer.herokuapp.com')

#   PAYPAL SETTINGS
SITE_URL = 'http://bookanentertainer.herokuapp.com'
PAYPAL_NOTIFY_URL = 'https://bookanentertainer.herokuapp.com/to-ngrok-or-not-to-ngrok/'     #   URL taken from name of HEROKU App
PAYPAL_RECEIVER_EMAIL = 'cormac.music-facilitator@gmail.com'

# Since DEBUG = False, you can log DEBUG information to the HEROKU console
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
