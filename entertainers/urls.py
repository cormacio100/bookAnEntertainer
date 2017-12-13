from django.conf.urls import url
from . import views
from entertainers.views import EntertainerView

# specific app URL pointable from template
app_name = 'entertainers'

urlpatterns = [
    url(r'^listings/$', views.listings, name="listings"),
    url(r'^profile/(?P<entertainer_id>[0-9]+)/$', views.display_entertainer_profile, name="profile"),
    url(r'^create_profile/$', views.create_profile, name="create_profile"),
    url(r'^(?P<pk>[0-9]+)/like/', views.like, name="like"),
    url(r'^(?P<pk>[0-9]+)/dislike/', views.dislike, name="dislike"),

    #   URLS FOR CLASS BASED VIEWS
    url(r'^api/listings/$', EntertainerView.as_view(), name="list_entertainers_api"),
    url(r'^api/listings/(?P<pk>[0-9]+)/$', EntertainerView.as_view(), name="update_entertainers_api"),
]
