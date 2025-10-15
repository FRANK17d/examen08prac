from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Vehiculo, TipoVehiculo

def home(request):
    return render(request, 'inventario_vehiculos/home.html')

# Vistas para Vehículos
def vehiculo_list(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'inventario_vehiculos/vehiculo_list.html', {'vehiculos': vehiculos})

def vehiculo_detail(request, pk):
    vehiculo = get_object_or_404(Vehiculo, pk=pk)
    return render(request, 'inventario_vehiculos/vehiculo_detail.html', {'vehiculo': vehiculo})

def vehiculo_create(request):
    tipos = TipoVehiculo.objects.all()
    if request.method == 'POST':
        marca = request.POST.get('marca')
        modelo = request.POST.get('modelo')
        año = request.POST.get('año')
        id_tipo = request.POST.get('id_tipo')
        imagen = request.FILES.get('imagen')
        
        if marca and modelo and año and id_tipo:
            tipo = get_object_or_404(TipoVehiculo, pk=id_tipo)
            vehiculo = Vehiculo.objects.create(
                marca=marca,
                modelo=modelo,
                año=int(año),
                id_tipo=tipo,
                imagen=imagen
            )
            messages.success(request, f'Vehículo {vehiculo.marca} {vehiculo.modelo} creado exitosamente.')
            return redirect('inventario:vehiculo_detail', pk=vehiculo.pk)
        else:
            messages.error(request, 'Todos los campos obligatorios deben ser completados.')
    
    return render(request, 'inventario_vehiculos/vehiculo_form.html', {'tipos': tipos})

def vehiculo_edit(request, pk):
    vehiculo = get_object_or_404(Vehiculo, pk=pk)
    tipos = TipoVehiculo.objects.all()
    
    if request.method == 'POST':
        vehiculo.marca = request.POST.get('marca')
        vehiculo.modelo = request.POST.get('modelo')
        vehiculo.año = int(request.POST.get('año'))
        vehiculo.id_tipo = get_object_or_404(TipoVehiculo, pk=request.POST.get('id_tipo'))
        
        if request.FILES.get('imagen'):
            vehiculo.imagen = request.FILES.get('imagen')
        
        vehiculo.save()
        messages.success(request, f'Vehículo {vehiculo.marca} {vehiculo.modelo} actualizado exitosamente.')
        return redirect('inventario:vehiculo_detail', pk=vehiculo.pk)
    
    return render(request, 'inventario_vehiculos/vehiculo_form.html', {'vehiculo': vehiculo, 'tipos': tipos})

def vehiculo_delete(request, pk):
    vehiculo = get_object_or_404(Vehiculo, pk=pk)
    
    if request.method == 'POST':
        vehiculo.delete()
        messages.success(request, f'Vehículo {vehiculo.marca} {vehiculo.modelo} eliminado exitosamente.')
        return redirect('inventario:vehiculo_list')
    
    return render(request, 'inventario_vehiculos/vehiculo_confirm_delete.html', {'vehiculo': vehiculo})

# Vistas para Tipos de Vehículos
def tipo_list(request):
    tipos = TipoVehiculo.objects.all()
    return render(request, 'inventario_vehiculos/tipo_list.html', {'tipos': tipos})

def tipo_create(request):
    if request.method == 'POST':
        tipo = request.POST.get('tipo')
        descripcion = request.POST.get('descripcion')
        
        if tipo:
            nuevo_tipo = TipoVehiculo.objects.create(
                tipo=tipo,
                descripcion=descripcion
            )
            messages.success(request, f'Tipo {nuevo_tipo.tipo} creado exitosamente.')
            return redirect('inventario:tipo_list')
        else:
            messages.error(request, 'El campo tipo es obligatorio.')
    
    return render(request, 'inventario_vehiculos/tipo_form.html')

def tipo_edit(request, pk):
    tipo = get_object_or_404(TipoVehiculo, pk=pk)
    
    if request.method == 'POST':
        tipo.tipo = request.POST.get('tipo')
        tipo.descripcion = request.POST.get('descripcion')
        tipo.save()
        messages.success(request, f'Tipo {tipo.tipo} actualizado exitosamente.')
        return redirect('inventario:tipo_list')
    
    return render(request, 'inventario_vehiculos/tipo_form.html', {'tipo': tipo})

def tipo_delete(request, pk):
    tipo = get_object_or_404(TipoVehiculo, pk=pk)
    
    if request.method == 'POST':
        tipo.delete()
        messages.success(request, f'Tipo {tipo.tipo} eliminado exitosamente.')
        return redirect('inventario:tipo_list')
    
    return render(request, 'inventario_vehiculos/tipo_confirm_delete.html', {'tipo': tipo})
