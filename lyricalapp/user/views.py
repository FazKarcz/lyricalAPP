import django.contrib.auth.forms
from django.shortcuts import render, redirect
from . forms import CreateUserForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from request.models import Request
from request.forms import RequestForm
from .models import Favorite
from song.models import Song
from django.core.paginator import Paginator
from django.db.models import Q
# Create your views here.

def register(request):

    form = CreateUserForm()

    #sprawdź czy pola w formularzu są prawidłowe i przeslij je do bazy danych, nastepnie przenies do dashboard
    if request.method == "POST":

        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")

    context = {'registerform':form}

    return render(request,'user/register.html', context=context)


def login(request):

    if request.user.is_authenticated:
        return redirect('dashboard')

    form = LoginForm()

    # wyciągamy z formularza logowania login i hasło
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password) #czy użytkownik istnieje?

            if user is not None:
                auth.login(request, user)
                return redirect('../')

    context = {'loginform':form}

    return render(request,'user/login.html', context=context)

def logout(request):

    auth.logout(request)
    previous_url = request.META.get('HTTP_REFERER', '/')

    return redirect(previous_url)

@login_required(login_url='login')
def dashboard(request):

    return render(request,'user/dashboard.html')

@login_required(login_url='login')
def request_list(request):
    requests = Request.objects.filter(user=request.user)
    return render(request, 'user/request_list.html', {'requests': requests})

@login_required(login_url='login')
def make_request(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            new_request = form.save(commit=False)
            new_request.user = request.user
            new_request.save()
            return redirect('request_list')
    else:
        form = RequestForm()
    return render(request, 'user/make_request.html', {'form': form})

@login_required(login_url='login')
def favorite_list(request):
    favorites = Favorite.objects.filter(user=request.user)
    order_by = request.GET.get('order_by')
    search_query = request.GET.get('search_query')


    if order_by == 'release_date':
        favorites = favorites.order_by('song__release_date')
    elif order_by == 'alphabetical':
        favorites = favorites.order_by('song__song_name')
    elif order_by == 'artist':
        favorites = favorites.order_by('song__artist__nickname')

    if search_query:
        favorites = favorites.filter(Q(song__song_name__icontains=search_query))

    paginator = Paginator(favorites, 10)  # 10 ulubionych piosenek na stronę
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'favorites': page_obj.object_list,
        'page_obj': page_obj,
        'order_by': order_by,
        'search_query': search_query,
    }
    return render(request, 'user/favorite_list.html', context)
