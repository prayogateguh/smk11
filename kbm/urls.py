from django.conf.urls import url

from . import views

urlpatterns = [
    # kelas
    url(r'^kelas/$', views.semua_kelas, name='list_kelas'),
    url(r'^kelas/(?P<slug>[-\w]+)$', views.kelas_detail, name='kelas_detail'),
    # mapel
    url(r'^mapel/$', views.semua_mapel, name='list_mapel'),
    url(r'^mapel/(?P<slug>[-\w]+)$', views.mapel_detail, name='mapel_detail'),
]
