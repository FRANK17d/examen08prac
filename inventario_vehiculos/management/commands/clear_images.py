from django.core.management.base import BaseCommand
from inventario_vehiculos.models import Vehiculo

class Command(BaseCommand):
    help = 'Limpia todas las imágenes de vehículos para empezar de cero con Cloudinary'

    def handle(self, *args, **options):
        vehiculos = Vehiculo.objects.filter(imagen__isnull=False).exclude(imagen='')
        
        for vehiculo in vehiculos:
            vehiculo.imagen = ''
            vehiculo.save()
            self.stdout.write(
                self.style.SUCCESS(f'Imagen limpiada para vehículo {vehiculo.id}: {vehiculo.marca} {vehiculo.modelo}')
            )
        
        self.stdout.write(
            self.style.SUCCESS('Todas las imágenes han sido limpiadas. Ahora puedes subir nuevas imágenes que se guardarán en Cloudinary.')
        )
