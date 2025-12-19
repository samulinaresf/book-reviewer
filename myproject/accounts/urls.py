from django.urls import path
from .views import registro, inicio_sesion, mostrar_perfil, formulario_csrf
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('registro/', registro, name='registro'),
    path('inicio-sesion/', inicio_sesion, name='inicio-sesion'),
    path('cierre-sesion/', LogoutView.as_view(next_page='inicio-sesion'), name='cerrar-sesion'),
    path('mi-perfil/', login_required(mostrar_perfil), name='mi-perfil'),  
    path('ruta-protegida/', formulario_csrf, name='ruta-protegida'),
]