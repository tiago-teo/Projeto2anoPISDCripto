from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from django.shortcuts import render,  get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from perfis.models import Perfil
from .models import Hashing
from django.contrib.auth.models import User
from .encrypt import hash_pass, hash_login


# Create your views here.

def index(request):
    return render(request, 'index.html')


@login_required(login_url='index')
def dashboard(request, pk):
    perfil = get_object_or_404(Perfil, pk=pk)
    perfis = Perfil.objects.all()
    return render(request, 'dashboard.html', {'user': request.user, 'perfil': perfil})


def cadastrar_usuario(request):
    if request.method == "POST":
        form_usuario = CustomUserCreationForm(request.POST)
        if form_usuario.is_valid():                        
            form_usuario.save()
            return redirect('logar_usuario')
    else:
        form_usuario = CustomUserCreationForm()
    return render(request, 'usuarios/form_usuario.html', {"form_usuario": form_usuario})


def logar_usuario(request):
    if request.method == "POST":
        username = request.POST["username"]
        password_requested = request.POST["password"]
        user = get_object_or_404(User, username=username)
        user_id = user.id        
        password = hash_login(password_requested, user_id)
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('dashboard', pk=usuario.id)
        else:
            messages.error(request, 'As credenciais estão incorretas')
            return redirect('logar_usuario')
    else:
        form_login = AuthenticationForm()
    return render(request, 'usuarios/login.html', {"form_login": form_login})


def deslogar_usuario(request):
    logout(request)
    return redirect('index')

def service(request):
    return render(request, 'service.html')

def about(request):
    return render(request, 'about.html')