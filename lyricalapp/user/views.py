import django.contrib.auth.forms
from django.shortcuts import render, redirect
from . forms import CreateUserForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
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
                return redirect('dashboard')

    context = {'loginform':form}

    return render(request,'user/login.html', context=context)

def logout(request):

    auth.logout(request)

    return redirect("login")

@login_required(login_url='login')
def dashboard(request):

    return render(request,'user/dashboard.html')

