<<<<<<< Updated upstream:lyricalAPP/lyricalapp/artist/urls.py
from django.urls import path
from rest_framework.routers import SimpleRouter

from . import views

app_name = 'artist'

router = SimpleRouter()

router.register('', views.ArtistViewSet, basename='Artist')

urlpatterns = [
    path('', views.artistList, name='artist_list')
]
=======
from django.urls import path
from rest_framework.routers import SimpleRouter

from . import views

app_name = 'artist'

router = SimpleRouter()

router.register('', views.ArtistViewSet, basename='Artist')

urlpatterns = [
    path('', views.artistList, name='artist_list')
]
>>>>>>> Stashed changes:lyricalapp/artist/urls.py
