from django.urls import path
from rest_framework.routers import SimpleRouter

from . import views

app_name = 'request'

router = SimpleRouter()

router.register('', views.RequestViewSet, basename='Request')

urlpatterns = router.urls