from django.conf.urls import url

from . import views
from berita.feeds import LatestPostsFeed

urlpatterns = [
    # display all posts (public)
    url(r'^$', views.post_list, name='homepage'),
    # display all posts (dashboard)
    url(r'^all-posts/$', views.all_posts, name='all_posts'),
    # latest posts feeds
    url(r'^feeds/$', LatestPostsFeed(), name='post_feed'),
    # post a news from staff dashboard
    url(r'^add/$', views.add_post, name='add_post'),
    url(r'^edit/(?P<pk>[-\w]+)/$', views.edit_post, name='edit_post'),
    url(r'^delete/(?P<pk>\d+)/$', views.del_post, name='del_post'),
    # view post
    url(r'^(?P<post>[-\w]+)/$', views.post_detail, name='post_detail'),
    url(r'^tag/(?P<tag_slug>[-\w]+)/$',
        views.post_list, name='post_list_by_tag'),
]
