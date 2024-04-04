import django_filters
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Song,Album
from .serializers import SongSerializer, AlbumSerializer


class SongViewSet(viewsets.ModelViewSet):
    serializer_class = SongSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Song.objects.all()
    search_fields = ['artist', 'song_name', 'genre','album']
    ordering_fields = ['song_name', 'release_date','album']
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, SearchFilter, OrderingFilter)


def songList(request):
    songs = Song.objects.all()
    return render(request, 'song_list.html', {'songs': songs})


class AlbumViewSet(viewsets.ModelViewSet):
    serializer_class = AlbumSerializer
    authentication_classes = (SessionAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Album.objects.all()
    search_fields = ['album_name','genre']
    ordering_fields = ['release_date']
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, SearchFilter, OrderingFilter)


def albumList(request):
    albums = Album.objects.all()
    return render(request, 'album_list.html', {'albums': albums})
