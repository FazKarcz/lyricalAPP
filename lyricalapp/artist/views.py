from django.shortcuts import render, get_object_or_404
import django_filters
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from song import models

from .models import Artist
from .serializers import ArtistSerializer


class ArtistViewSet(viewsets.ModelViewSet):
    serializer_class = ArtistSerializer
    authentication_classes = (SessionAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Artist.objects.all()
    search_fields = ['surname', 'origin']
    ordering_fields = ['nickname']
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, SearchFilter, OrderingFilter)


def artistList(request):
    artists = Artist.objects.all()
    return render(request, 'artist/artist_list.html', {'artists': artists})


def artistDetail(request, artist_id):
    artist = get_object_or_404(Artist, pk=artist_id)
    songs = models.Song.objects.filter(artist=artist)
    albums = models.Album.objects.filter(artist=artist)
    return render(request, 'artist/artist_detail.html',
                  {'artist': artist, 'artist_id': artist_id, 'songs': songs, 'albums': albums})
