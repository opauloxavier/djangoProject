from django.shortcuts import HttpResponse,render,get_object_or_404

from .models import Artista,Musica,Album,Genero


def index(request):
    artistas = Artista.objects.order_by('name')
    musicas = Musica.objects.order_by('name')
    generos = Genero.objects.order_by('name')
    context = {'artistas': artistas,'musicas':musicas,'generos':generos}
    return render(request, 'recommendations/index.html', context)

def artist(request, artist_id):
    artista =get_object_or_404(Artista, pk=artist_id)
    musicas =Musica.objects.filter(artist=artista.name)
    albums = Album.objects.filter(artist=artista.name)
    return render(request, 'recommendations/detail.html', {'artista': artista,'musicas':musicas,'albums':albums})

def allArtist(request):
    artistas = Artista.objects.order_by('name')
    context = {'artistas': artistas}
    return render(request, 'recommendations/artistas.html', context)

def album(request, album_id):
    return HttpResponse("Album %s." % album_id)

def genero(request, genero_id):
    return HttpResponse("Genero %s." % genero_id)

def music(request, music_id):
    return HttpResponse("Musica %s." % music_id)

def sobre(request):
    return render(request, 'recommendations/sobre.html')