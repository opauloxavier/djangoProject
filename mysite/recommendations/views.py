from django.shortcuts import HttpResponse,render

from .models import Artista


def index(request):
    artistas = Artista.objects.order_by('name')
    context = {'artistas': artistas}
    return render(request, 'recommendations/index.html', context)

def artist(request, artist_id):
    return HttpResponse("Artista %s." % artist_id)

def album(request, album_id):
    return HttpResponse("Album %s." % album_id)

def genero(request, genero_id):
    return HttpResponse("Genero %s." % genero_id)

def music(request, music_id):
    return HttpResponse("Musica %s." % music_id)