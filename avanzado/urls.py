from django.urls import path
from avanzado import views

urlpatterns = [
    # VERSION CON VISTAS COMUNES
    # path('mascotas/', views.ver_mascotas, name='ver_mascotas'),
    # path('mascotas/crear/', views.crear_mascota, name='crear_mascota'),
    # path('mascotas/editar/<int:id>', views.editar_mascota, name='editar_mascota'),
    # path('mascotas/eliminar/<int:id>', views.eliminar_mascota, name='eliminar_mascota')
    
    #VERSION CON CALSES BASADAS EN VISTAS
    path('mascotas/', views.ListaMascotas.as_view(), name='ver_mascotas'),
    path('mascotas/crear/', views.CrearMascota.as_view(), name='crear_mascota'),
    path('mascotas/editar/<int:pk>', views.EditarMascota.as_view(), name='editar_mascota'),
    path('mascotas/eliminar/<int:id>', views.EliminarMascotas.as_view(), name='eliminar_mascota')
]
