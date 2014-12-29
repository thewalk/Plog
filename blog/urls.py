from django.conf.urls import patterns, url
from blog import views

urlpatterns = patterns('',
    url(r'^home/$', views.home, name='home'),
    url(r'^article_base/$',views.artilce_base,name='article_base'),
    url(r'^article_list/$',views.article_list,name='article_list'),
    url(r'^article_detail/$',views.article_detail,name='article_detail'),
    url(r'^qrcode$', views.qrcode, name='qrcode'),
)
