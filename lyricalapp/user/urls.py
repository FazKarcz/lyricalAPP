from django.urls import path
from rest_framework.routers import SimpleRouter
from . import views

login_router = SimpleRouter()
register_router = SimpleRouter()
dashboard_router = SimpleRouter()

login_router.register('', views.login, basename='login')
register_router.register('', views.register, basename='register')
dashboard_router.register('', views.dashboard, basename='dashboard')

urlpatterns = [
    path('', views.dashboard, name="dashboard"),  #widok konta
    path('login', views.login, name="login"),  #widok logowania
    path('register', views.register, name="register"),  #widok rejestracji
    path('logout', views.logout, name="logout"),  #widok logout
    path('request_list', views.request_list, name="request_list"), #widok zgloszen uzytkownika
    path('make_request', views.make_request, name="make_request"), #widok formularza zgłoszen
    path('favorite_list', views.favorite_list, name="favorite_list")
]