from django.db import models

class TipoVehiculo(models.Model):
    tipo = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.tipo

class Vehiculo(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    año = models.IntegerField()
    imagen = models.ImageField(upload_to='vehiculos/', blank=True, null=True)
    id_tipo = models.ForeignKey(TipoVehiculo, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.año})"
