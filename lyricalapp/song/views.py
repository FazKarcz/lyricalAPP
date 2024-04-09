import django_filters
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Song
from .serializers import SongSerializer


class SongViewSet(viewsets.ModelViewSet):
    serializer_class = SongSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Song.objects.all()
    search_fields = ['artist', 'song_name', 'genre','album']
    ordering_fields = ['song_name', 'release_date','album']
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, SearchFilter, OrderingFilter)
