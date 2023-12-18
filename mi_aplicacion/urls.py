from django.urls import path
from .views import Pais1, RegistrarPais, Editoriales, CrearEditorial, index, eliminar_pais,registrar_pais

urlpatterns = [
    path('Paises/', Pais1, name='Paises'),
    path('RegistrarPais/',RegistrarPais, name='RegistrarPais'),
    path('Editoriales/', Editoriales, name='Editoriales'),
    path('CrearEditorial/',CrearEditorial, name='CrearEditorial'),
    path('', index, name='index'),  # Importa la función index
    # ... otras rutas de la aplicación ...
    path('eliminarpais/<int:idpais>/',eliminar_pais, name='eliminar_pais'),
    path('registrarPais/', registrar_pais, name='registrar_pais'),
]
