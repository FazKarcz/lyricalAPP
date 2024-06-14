from django.shortcuts import render, get_object_or_404
import django_filters
from django.core.paginator import Paginator
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from song import models
from django.db.models import Q

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
    search_query = request.GET.get('search_query')
    order_by = request.GET.get('order_by')

    if order_by == 'date_of_birth':
        artists = artists.order_by('date_of_birth')
    elif order_by == 'alphabetical':
        artists = artists.order_by('nickname')
    elif order_by == 'origin':
        artists = artists.order_by('origin')

    if search_query:
        artists = artists.filter(Q(nickname__icontains=search_query))

    paginator = Paginator(artists, 16)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'artists': page_obj.object_list,
        'page_obj': page_obj,
        'search_query': search_query,
    }

    return render(request, 'artist/artist_list.html', context)


def artistDetail(request, artist_id):
    artist = get_object_or_404(Artist, pk=artist_id)
    songs = models.Song.objects.filter(artist=artist)
    albums = models.Album.objects.filter(artist=artist)
    return render(request, 'artist/artist_detail.html',
                  {'artist': artist, 'artist_id': artist_id, 'songs': songs, 'albums': albums})
