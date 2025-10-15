from django.contrib import admin
from .models import TipoVehiculo, Vehiculo

@admin.register(TipoVehiculo)
class TipoVehiculoAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'descripcion')
    search_fields = ('tipo',)

@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'año', 'id_tipo')
    list_filter = ('id_tipo', 'año', 'marca')
    search_fields = ('marca', 'modelo')
    list_per_page = 20
