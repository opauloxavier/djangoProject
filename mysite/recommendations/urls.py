from django.conf.urls import url,include
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^artistas/(?P<artist_id>[0-9]+)/$', views.artist, name='detalhes'),
    url(r'^artistas/$', views.allArtist, name='artistas'),
    url(r'^sobre/$',views.sobre, name='Sobre'),
]