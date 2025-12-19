from django.urls import path
from . import views

urlpatterns = [
    path('', views.politica_cookies, name='politica_cookies'),
]