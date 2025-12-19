from django.urls import path
from . import views

urlpatterns = [
    path('', views.politica_privacidad, name='politica_privacidad'),  # Ruta para la vista política de privacidad
]