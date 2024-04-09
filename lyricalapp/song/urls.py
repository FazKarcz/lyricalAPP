from django.urls import path, include
from rest_framework.routers import SimpleRouter
from . import views

app_name = 'song'

# Tworzymy oddzielne routery dla SongViewSet i AlbumViewSet
song_router = SimpleRouter()
album_router = SimpleRouter()

# Rejestrujemy widoki dla SongViewSet
song_router.register('', views.SongViewSet, basename='song')

# Rejestrujemy widoki dla AlbumViewSet
album_router.register('', views.AlbumViewSet, basename='album')

# Dodajemy ścieżki do listy urlpatterns
urlpatterns = [
    path('song/', views.songList, name='song_list'),  # Dodajemy URL-e dla SongViewSet
    path('album/', views.albumList, name='album_list'),  # Dodajemy URL-e dla AlbumViewSet
    path('song/detail/<int:song_id>/', views.song_detail, name='song_detail'),
]