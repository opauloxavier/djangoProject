from django.conf.urls import url,include
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^artist/(?P<artist_id>[0-9]+)/$', views.artist, name='Detalhes do Artista'),
]