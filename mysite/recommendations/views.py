from django.shortcuts import HttpResponse,render,get_object_or_404

from .models import Artista


def index(request):
    artistas = Artista.objects.order_by('name')
    context = {'artistas': artistas}
    return render(request, 'recommendations/index.html', context)

def artist(request, artist_id):
    artista =get_object_or_404(Artista, pk=artist_id)

    return render(request, 'recommendations/detail.html', {'artista': artista})

def album(request, album_id):
    return HttpResponse("Album %s." % album_id)

def genero(request, genero_id):
    return HttpResponse("Genero %s." % genero_id)

def music(request, music_id):
    return HttpResponse("Musica %s." % music_id)