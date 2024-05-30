from django.shortcuts import render
from song.models import Song
from hitcount.models import HitCount


def startingPage(request):
    latest_songs = Song.objects.order_by('-update_date')[:6]
    popular_songs = Song.objects.filter(hit_count_generic_relation__hits__gt=0).order_by('-hit_count_generic_relation__hits')[:6]
    context = {
        'latest_songs': latest_songs,
        'popular_songs': popular_songs,
    }
    return render(request, 'index.html', context)
