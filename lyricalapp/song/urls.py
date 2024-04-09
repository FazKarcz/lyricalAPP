from django.urls import path
from rest_framework.routers import SimpleRouter

from . import views

app_name = 'song'

router = SimpleRouter()

router.register('', views.SongViewSet, basename='Song')

urlpatterns = router.urls