"""smk URL Configuration

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
# add url mapping to serve static files during development (only)
from django.conf import settings
# add URLs from akun application
from django.conf.urls import include, url
from django.conf.urls.static import static
# include admin app
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.views.generic import TemplateView

from berita.sitemaps import PostSitemap

sitemaps = {
    'posts': PostSitemap,
}
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # site authentication urls
    url(r'^accounts/', include('django.contrib.auth.urls')),
    # posts sitemaps
    url(r'^sitemap\.xml$',
        sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'),
    # static pages
    url(r'^about/$',
        TemplateView.as_view(template_name='static/about_us.html'),
        name='about'),
    url(r'^contact/$',
        TemplateView.as_view(template_name='static/contact_us.html'),
        name='contact'),
    # akun apps
    url(r'', include('akun.urls', namespace='akun', app_name='akun')),
    # kbm apps
    url(r'', include('kbm.urls', namespace='kbm', app_name='kbm')),
    # berita apps
    url(r'', include('berita.urls', namespace='berita', app_name='berita')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
