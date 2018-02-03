from django.conf.urls import url

from . import views

urlpatterns = [
    # akun dashboard
    url(r'^edit-profile/$', views.update_profile, name='profile'),
    url(r'^guru/$', views.guru_detail, name='guru_detail'),
    url(r'^nilai-siswa/$', views.siswa_nilai, name='siswa_nilai'),
    url(r'^profile-siswa/$', views.siswa_profile, name='siswa_profile'),
]
