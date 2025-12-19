from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from accounts.models import Account
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie
from django.views.decorators.http import require_POST, require_http_methods
from django.http import HttpResponse
from django.middleware.csrf import get_token

def registro(request):
        
    if request.method == 'POST':

        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Tu cuenta ha sido creada exitosamente")
            return redirect('inicio')
        else:
             messages.error(request, "No ha sido posible crear la cuenta")
    else:
        form = RegistrationForm()
    
    return render(request, 'registro.html', {'form':form})

def inicio_sesion(request):
        
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(username=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Inicio de sesión exitoso")
                return redirect('index')
            else:
                 messages.error(request, "Email o contraseña incorrectos")
    else:
        form = LoginForm()
        
    return render(request, 'login.html', {'form':form})

#mostrar los datos del perfil
@login_required  
def mostrar_perfil(request):
    perfil = request.user  
    context = {
        'perfil': perfil  
    }
    return render(request, 'perfil.html', context)

@csrf_protect  # Asegura que Django bloquee peticiones sin CSRF
@require_http_methods(["GET", "POST"])
@ensure_csrf_cookie
#@require_POST    Solo permite solicitudes POST
def formulario_csrf(request):
    if request.method == "GET":
        get_token(request)
        return render(request,"formulario_csrf.html")
    elif request.method == "POST":
        return HttpResponse("Solicitud POST válida con CSRF", status=200)
