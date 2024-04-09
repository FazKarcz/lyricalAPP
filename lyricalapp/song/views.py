import django_filters
from django.shortcuts import render, redirect
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Song, Album, Comment
from .serializers import SongSerializer, AlbumSerializer
from .forms import CommentForm


class SongViewSet(viewsets.ModelViewSet):
    serializer_class = SongSerializer
    authentication_classes = (SessionAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Song.objects.all()
    search_fields = ['artist', 'song_name', 'genre','album']
    ordering_fields = ['song_name', 'release_date','album']
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, SearchFilter, OrderingFilter)


def songList(request):
    songs = Song.objects.all()
    return render(request, 'song/song_list.html', {'songs': songs})


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
    return render(request, 'song/album_list.html', {'albums': albums})


def song_detail(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    comments = Comment.objects.filter(song=song)
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.song = song
                comment.user = request.user
                comment.save()
                form = CommentForm()
        else:
            return redirect('login')
    else:
            form = CommentForm()
    return render(request, 'song/song_detail.html', {'song': song, 'comments': comments, 'form': form, 'song_id': song_id})

