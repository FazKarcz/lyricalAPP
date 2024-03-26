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
    path('song/', include(song_router.urls)),  # Dodajemy URL-e dla SongViewSet
    path('album/', include(album_router.urls)),  # Dodajemy URL-e dla AlbumViewSet
]