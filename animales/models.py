from django.db import models

# Create your models here.
#Tabla para productos para animales
class AnimalProducto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.CharField(max_length=50)
    stock = models.IntegerField()
    imagen = models.ImageField(upload_to='productos/')
    minutos = models.IntegerField(default=0)
    
    def __str__(self):
        return f'{self.nombre} - ${self.precio}'
    
    
#Tabla para productos para perros
class ProductoPerros(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.CharField(max_length=50)
    stock = models.IntegerField()
    imagen = models.ImageField(upload_to='productos/')
    minutos = models.IntegerField(default=0)
    
    def __str__(self):
        return f'{self.nombre} - ${self.precio}'
    
    
#Tabla para productos para gatos
class ProductoGatos(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.CharField(max_length=50)
    stock = models.IntegerField()
    imagen = models.ImageField(upload_to='productos/')
    minutos = models.IntegerField(default=0)
    
    
    def __str__(self):
        return f'{self.nombre} - ${self.precio}'
    

#Tabla para productos en el carro    
class Carrito(models.Model):
    producto = models.ForeignKey(AnimalProducto, on_delete=models.CASCADE, null=True, blank=True)
    producto_perros = models.ForeignKey(ProductoPerros, on_delete=models.CASCADE, null=True, blank=True)
    producto_gatos = models.ForeignKey(ProductoGatos, on_delete=models.CASCADE, null=True, blank=True)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.cantidad} x {self.producto.nombre}'
    
    
    def get_product_name(self):
        if self.producto:
            return self.producto.nombre
        elif self.producto_perros:
            return self.producto_perros.nombre
        elif self.producto_gatos:
            return self.producto_gatos.nombre
        return 'Sin producto'