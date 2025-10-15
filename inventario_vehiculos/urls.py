from django.urls import path
from . import views

app_name = 'inventario'

urlpatterns = [
    # Home
    path('', views.home, name='home'),
    
    # URLs para Vehículos
    path('vehiculos/', views.vehiculo_list, name='vehiculo_list'),
    path('vehiculos/crear/', views.vehiculo_create, name='vehiculo_create'),
    path('vehiculos/<int:pk>/', views.vehiculo_detail, name='vehiculo_detail'),
    path('vehiculos/<int:pk>/editar/', views.vehiculo_edit, name='vehiculo_edit'),
    path('vehiculos/<int:pk>/eliminar/', views.vehiculo_delete, name='vehiculo_delete'),
    
    # URLs para Tipos de Vehículos
    path('tipos/', views.tipo_list, name='tipo_list'),
    path('tipos/crear/', views.tipo_create, name='tipo_create'),
    path('tipos/<int:pk>/editar/', views.tipo_edit, name='tipo_edit'),
    path('tipos/<int:pk>/eliminar/', views.tipo_delete, name='tipo_delete'),
]
