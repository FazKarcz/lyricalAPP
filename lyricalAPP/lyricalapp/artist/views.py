from django.shortcuts import render
import django_filters
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Artist
from .serializers import ArtistSerializer


class ArtistViewSet(viewsets.ModelViewSet):
    serializer_class = ArtistSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Artist.objects.all()
    search_fields = ['surname', 'origin']
    ordering_fields = ['nickname']
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, SearchFilter, OrderingFilter)


def artistList(request):
    artists = Artist.objects.all()
    return render(request, 'artist_list.html', {'artists': artists})