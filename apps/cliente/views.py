from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm



def home(request):
    
    return render(request, "home.html")


def create_user(request):
    form = UserForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        User.objects.create_user(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
        return redirect('entrar')
    return render(request, "create_user.html", {'form': form})


def entrar(request):
    form = UserForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return ('')
        else:
            form.add_error(None, 'email ou senha incorretos')
    return render(request, "home.html", {'form': form})


@login_required(login_url='/entrar')
def sair(request):
    logout(request)
    return redirect('')