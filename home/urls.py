from django.urls import path
from home import views



urlpatterns = [
    path("hola/", views.hola),
    path("fecha/", views.fecha),
    path("fecha-nacimiento/<int:edad>", views.calcular_fecha),
    # path("mi-template/", views.mi_template),
    # path("mi-template/<str:nombre>", views.tu_template),
    path("prueba-template/", views.prueba_template),
    path("ver-persona/", views.ver_personas),
    path("crear-persona/<str:nombre>/<str:apellido>/", views.crear_persona),
    path("index/",views.index),
]
