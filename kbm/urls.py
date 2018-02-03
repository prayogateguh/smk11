from django.conf.urls import url

from . import views

urlpatterns = [
    # guru
    url(r'^kelas/(?P<slug>[-\w]+)$', views.guru_kelas_detail, name='kelas_detail'),
    url(r'^guru-mapel/(?P<slug>[-\w]+)$', views.guru_mapel_detail, name='mapel_detail'),
]
