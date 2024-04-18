from django.urls import path
from rest_framework.routers import SimpleRouter

from . import views

app_name = 'artist'

router = SimpleRouter()

router.register('', views.ArtistViewSet, basename='Artist')

urlpatterns = [
    path('', views.artistList, name='artist_list'),
    path('detail/<int:artist_id>/', views.artistDetail, name='artist_detail')
]
