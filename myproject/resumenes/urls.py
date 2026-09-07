from django.urls import path
from . import views
from django.db.models import Q

urlpatterns = [
    path('', views.mostrar_resumenes, name='index'),
    path('search/', views.busqueda_producto, name="busqueda"),
    path('review/<int:libro_id>/<int:x>/', views.puntuar_libro, name="puntuar"),
    path('review/<int:libro_id>/', views.agregar_favoritos, name="favoritos"),
    path('buscar/', views.buscar_libros_google_books, name="search_books"),
    path('perfil/favoritos/',views.mostrar_libros_favoritos, name='mostrar_favoritos'),
]

