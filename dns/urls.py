from django.conf.urls import url, patterns

from dns import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pk>[0-9]+)/preview/$', views.preview, name='preview'),
    url(r'^(?P<pk>[0-9]+)/show/$', views.show, name='show'),
]
