from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Perfil, Gusto, SubcategoriaGusto, CategoriaGusto

from .forms import UserForm, PerfilForm
from django.contrib.auth.models import User


def home(request):
    return render(request, 'usuarios/home.html')

def registro_paso1(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            # Guardar en sesión temporalmente
            request.session['registro_data'] = user_form.cleaned_data
            request.session['registro_password'] = user_form.cleaned_data['password1']
            return redirect('registro_paso2')
    else:
        user_form = UserForm()
    return render(request, 'usuarios/registro_paso1.html', {'form': user_form})

def registro_paso2(request):
    if 'registro_data' not in request.session:
        return redirect('registro_paso1')

    if request.method == 'POST':
        perfil_form = PerfilForm(request.POST, request.FILES)
        if perfil_form.is_valid():
            # Crear usuario
            data = request.session['registro_data']
            user = User.objects.create_user(
                username=data['username'],
                email=data['email'],
                password=request.session['registro_password']
            )

            # Crear perfil
            perfil = perfil_form.save(commit=False)
            perfil.user = user
            perfil.save()
            perfil.gustos.set(perfil_form.cleaned_data['gustos'])

            # Autologin (opcional)
            login(request, user)

            # Limpiar sesión
            del request.session['registro_data']
            del request.session['registro_password']

            return redirect('home')  # Ajusta según tu ruta
    else:
        perfil_form = PerfilForm()
    return render(request, 'usuarios/registro_paso2.html', {'form': perfil_form})


def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('home')
        else:
            messages.error(request, 'Credenciales incorrectas.')
    return render(request, 'usuarios/login.html')

def cerrar_sesion(request):
    logout(request)
    return redirect('home')
