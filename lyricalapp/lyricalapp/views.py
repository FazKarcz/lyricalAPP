from django.shortcuts import render
from song.models import Song

def startingPage(request):
    latest_songs = Song.objects.order_by('-update_date')[:6]
    popular_songs = Song.objects.order_by('-views')[:6]
    context = {
        'latest_songs': latest_songs,
        'popular_songs': popular_songs,
    }
    return render(request, 'index.html', context)
