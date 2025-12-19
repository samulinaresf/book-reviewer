from django.urls import path
from . import views

urlpatterns = [
    path('', views.sobre_nosotros, name='sobre_nosotros'),
]