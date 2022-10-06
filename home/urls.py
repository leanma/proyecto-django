from django.urls import path
from home import views



urlpatterns = [
    path("hola/", views.hola,name="hola"),
    path("fecha/", views.fecha,name="fecha"),
    path("fecha-nacimiento/<int:edad>", views.calcular_fecha,name="fecha"),
    # path("mi-template/", views.mi_template),
    #  path("mi-template/<str:nombre>", views.tu_template,name="mi_template"),
    path("prueba-template/", views.prueba_template),
    path("ver-persona/", views.ver_personas,name="ver_persona"),
    path("crear-persona/<str:nombre>/<str:apellido>/", views.crear_persona),
    path("",views.index, name="index"),
]
