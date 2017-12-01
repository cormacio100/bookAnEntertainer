from django.conf.urls import url
from . import views

# specific app URL pointable from template
app_name = 'entertainers'

urlpatterns = [
    url(r'^listings/', views.listings, name="listings"),
    url(r'^profile/(?P<entertainer_id>[0-9]+)/$', views.display_entertainer_profile, name="profile"),
]

