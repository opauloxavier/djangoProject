from django.contrib import admin

from .models import Artista,Genero,Album,Musica

admin.site.register(Artista)
admin.site.register(Genero)
admin.site.register(Album)
admin.site.register(Musica)