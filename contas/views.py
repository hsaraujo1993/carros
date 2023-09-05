from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout


# Create your views here.


def registro_view(request):
    if request.method == "POST":
        formulario_usuario = UserCreationForm(request.POST)
        if formulario_usuario.is_valid():
            formulario_usuario.save()
            return redirect("login")
    else:
        formulario_usuario = UserCreationForm()
    return render(request, "registro.html", {"formulario_usuario": formulario_usuario})


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect("carros_lista")
        else:
            login_usuario = AuthenticationForm()
    else:
        login_usuario = AuthenticationForm()
    return render(request, "login.html", {"login_usuario": login_usuario})


def logout_view(request):
    logout(request)
    return redirect("login")


