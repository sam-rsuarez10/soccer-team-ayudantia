from unicodedata import name
from django.urls import path, include
from . import views

""" Aquí se definirán las urls para
    cada una de las páginas del registro del equipo 
    como en el archivo externo de urls.py se definió 
    el conjunto de urls de team_resgister como team/;
    el acceso de estas urls serán de la forma 
    team/url-definidad (ver archivo urls.py en 
    directorio soccer_team_ayudantia) """

urlpatterns = [
    # url para la home page
    path('', views.index, name='index'),
    # url para añadir un miembro del equipo
    path('nuevo-miembro/', views.agregar, name='nuevo-miembro'),
    # lista del equipo
    path('list/', views.listar, name='list')
]

