"""bookAnEntertainer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from home import views as home_views
from django.conf.urls.static import static
from django.conf import settings
#import settings
#from settings import base

#   PAYPAL SETTINGS
from paypal.standard.ipn import urls as paypal_urls
from paypal_store import views as paypal_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',home_views.get_index, name="home"),

    #   ENTERTAINERS APP URLS
    url(r'^entertainers/', include('entertainers.urls')),

    #   USER_ACCOUNTS APP URLS
    url(r'^user_accounts/',include('user_accounts.urls')),

    #   ACCOUNTS APP URLS
    url(r'^accounts/',include('accounts.urls')),

    #   PAYPAL APP URLS
    url(r'^to-ngrok-or-not-to-ngrok/', include(paypal_urls)),
    url(r'^paypal-return',paypal_views.paypal_return),          #   handles the return of a customer after payment
    url(r'^paypal-cancel',paypal_views.paypal_cancel),          #   handles what happens when a customer cancels at the Paypal site
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


#   CODE FOR DJANGO DEBUG TOOLBAR
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

