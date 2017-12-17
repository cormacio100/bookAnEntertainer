from base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

INSTALLED_APPS.append('debug_toolbar')
MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': 'bookAnEntertainer.settings.show_toolbar',
}

#   PAYPAL SETTINGS
SITE_URL = 'http://bookanentertainer.herokuapp.com'
PAYPAL_NOTIFY_URL = 'https://aac1c9ee.ngrok.io/to-ngrok-or-not-to-ngrok/'   #   ON LOCALHOST NEED TO RUN ngrok AND COPY
                                                                            #  URL AS <NGROK-ADDRESS>/<URL FROM URL.PY>
                                                                            #    HERE
PAYPAL_RECEIVER_EMAIL = 'cormac.music-facilitator@gmail.com'


#   DEBUG TOOLBAR
def show_toolbar(request):
    if not request.is_ajax(): # and request.user: # and request.user.username == "cormacio":
        return True
    return True

