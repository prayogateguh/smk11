from django.conf.urls import url

from . import views
from berita.feeds import LatestPostsFeed

urlpatterns = [
    # akun dashboard
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^profile/$', views.update_profile, name='profile'),
]