from django.urls import path
from . import views
from django.db.models import Q

urlpatterns = [
    path('', views.mostrar_resumenes, name='index'),
    path('search/', views.busqueda_producto, name="busqueda"),
    path('review/<int:libro_id>/<int:x>/', views.puntuar_libro, name="puntuar"),
]
