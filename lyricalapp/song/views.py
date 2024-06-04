import django_filters
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Song, Album, Comment
from .serializers import SongSerializer, AlbumSerializer
from .forms import CommentForm
from user.models import Favorite



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
    order_by = request.GET.get('order_by')
    search_query = request.GET.get('search_query')

    if order_by == 'release_date':
        songs = songs.order_by('release_date')
    elif order_by == 'alphabetical':
        songs = songs.order_by('song_name')

    if search_query:
        songs = songs.filter(Q(song_name__icontains=search_query))

    # Dodaj paginację
    paginator = Paginator(songs, 10)  # 10 piosenek na strone
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'songs': page_obj.object_list,
        'page_obj': page_obj,
        'order_by': order_by,
        'search_query': search_query,
    }

    return render(request, 'song/song_list.html', context)


class AlbumViewSet(viewsets.ModelViewSet):
    serializer_class = AlbumSerializer
    authentication_classes = (SessionAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Album.objects.all()
    search_fields = ['album_name','genre']
    ordering_fields = ['release_date']
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, SearchFilter, OrderingFilter)


def albumList(request):
    search_query = request.GET.get('search_query')
    albums = Album.objects.all()

    if search_query:
        albums = albums.filter(Q(album_name__icontains=search_query))

    paginator = Paginator(albums, 10)  # 10 albumów na stronę
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'albums': page_obj.object_list,
        'page_obj': page_obj,
        'search_query': search_query
    }

    return render(request, 'song/album_list.html', context)


def albumDetail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    songs = Song.objects.filter(album=album)
    return render(request, 'song/album_detail.html', {'album': album, 'album_id': album_id, 'songs': songs})


def song_detail(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    song.views += 1
    song.save()
    comments = Comment.objects.filter(song=song)
    favorite = None

    if request.user.is_authenticated:
        favorite = Favorite.objects.filter(user=request.user, song=song).first()

    if request.method == 'POST':
        if request.user.is_authenticated:
            if 'comment_form' in request.POST:
                form = CommentForm(request.POST)
                if form.is_valid():
                    comment = form.save(commit=False)
                    comment.song = song
                    comment.user = request.user
                    comment.save()
                    return redirect('song:song_detail', song_id=song_id)
            elif 'favorite_form' in request.POST:
                if favorite:
                    favorite.delete()
                else:
                    Favorite.objects.create(user=request.user, song=song)
        else:
            return redirect('login')

    form = CommentForm()
    return render(request, 'song/song_detail.html', {'song': song, 'comments': comments,
                                                     'form': form, 'song_id': song_id, 'favorite': favorite})


