from django.conf.urls import url
from . import views

# specific app URL pointable from template
app_name = 'accounts'

urlpatterns = [
    url(r'^register/', views.auth_register, name="register"),
    url(r'^login/', views.auth_login, name="login"),
    url(r'^logout/', views.auth_logout, name="logout"),
    url(r'^profile/', views.auth_profile, name="profile"),
]

