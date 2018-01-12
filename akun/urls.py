from django.conf.urls import url

from . import views

urlpatterns = [
    # akun dashboard
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^profile/$', views.update_profile, name='profile'),
    url(r'^guru/$', views.guru_detail, name='guru_detail'),
    url(r'^siswa/$', views.siswa_detail, name='siswa_detail'),
]
