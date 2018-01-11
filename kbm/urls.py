from django.conf.urls import url

from . import views

urlpatterns = [
    # kelas
    url(r'^kelas/$', views.semua_kelas, name='list_kelas'),
    url(r'^kelas/(?P<slug>[-\w]+)$', views.kelas_detail, name='kelas_detail'),
    # mapel
    url(r'^mapel/$', views.semua_mapel, name='list_mapel'),
    url(r'^mapel/(?P<pk>\d+)$', views.mapel_detail, name='mapel_detail'),
    # # siswa
    # url(r'^siswa/$', views.semua_siswa, name='list_siswa'),
    # url(r'^siswa/(?P<pk>\d+)$', views.siswa_detail, name='siswa_detail'),
]
