from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard, name="dashboard"),  #widok konta
    path('login', views.login, name="login"),  #widok logowania
    path('register', views.register, name="register"),  #widok rejestracji
    path('logout', views.logout, name="logout"),  #widok logout
    path('request_list', views.request_list, name="request_list"), #widok zgloszen uzytkownika
    path('make_request', views.make_request, name="make_request"), #widok formularza zgłoszen
]