from django.core.management.base import BaseCommand
from inventario_vehiculos.models import Vehiculo
import cloudinary
import cloudinary.uploader
import os
from django.conf import settings

class Command(BaseCommand):
    help = 'Migra imágenes existentes a Cloudinary'

    def handle(self, *args, **options):
        # Configurar Cloudinary
        cloudinary.config(
            cloud_name=settings.CLOUDINARY_STORAGE['CLOUD_NAME'],
            api_key=settings.CLOUDINARY_STORAGE['API_KEY'],
            api_secret=settings.CLOUDINARY_STORAGE['API_SECRET']
        )
        
        vehiculos = Vehiculo.objects.filter(imagen__isnull=False).exclude(imagen='')
        
        for vehiculo in vehiculos:
            if vehiculo.imagen and not vehiculo.imagen.name.startswith('http'):
                try:
                    # Ruta local de la imagen
                    image_path = os.path.join(settings.MEDIA_ROOT, vehiculo.imagen.name)
                    
                    if os.path.exists(image_path):
                        # Subir a Cloudinary
                        result = cloudinary.uploader.upload(
                            image_path,
                            folder="vehiculos",
                            public_id=f"vehiculo_{vehiculo.id}"
                        )
                        
                        # Actualizar el modelo con la nueva URL
                        vehiculo.imagen = result['secure_url']
                        vehiculo.save()
                        
                        self.stdout.write(
                            self.style.SUCCESS(f'Imagen migrada para vehículo {vehiculo.id}: {vehiculo.marca} {vehiculo.modelo}')
                        )
                    else:
                        self.stdout.write(
                            self.style.WARNING(f'Imagen no encontrada para vehículo {vehiculo.id}: {image_path}')
                        )
                        
                except Exception as e:
                    self.stdout.write(
                        self.style.ERROR(f'Error migrando imagen para vehículo {vehiculo.id}: {str(e)}')
                    )
        
        self.stdout.write(
            self.style.SUCCESS('Migración de imágenes completada')
        )
