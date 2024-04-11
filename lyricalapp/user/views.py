import django.contrib.auth.forms
from django.shortcuts import render, redirect
from . forms import CreateUserForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from request.models import Request
from request.forms import RequestForm
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
