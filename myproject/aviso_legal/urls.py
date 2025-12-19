from django.urls import path
from . import views

urlpatterns = [
    path('', views.aviso_legal, name='aviso_legal'),
]