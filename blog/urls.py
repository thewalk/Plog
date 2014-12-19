from django.conf.urls import patterns, url
from blog import views

urlpatterns = patterns('',
    url(r'^(?P<category_type>\w+)/detail/article_id=(?P<article_id>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<category_type>\w+)/list/$', views.article_list_by_category_type, name='article_list_by_category_type'),
    url(r'^(?P<category_type>\w+)/list/category=(?P<category_name>.+)/$', views.article_list_by_category_name, name='article_list_by_category_name'),
    url(r'^(?P<category_type>\w+)/list/tag=(?P<tag_name>.+)$', views.article_list_by_tag_name, name='article_list_by_tag_name'),
)
