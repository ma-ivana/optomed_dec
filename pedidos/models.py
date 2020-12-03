from django.db import models
from django.db.models import Case, CharField, Value, When
from pacientes.models import Paciente

# Create your models here.

class Tag(models.Model):
  nombre = models.CharField(max_length=200, null=True)
  
  def __str__(self):
    return self.nombre

class Producto(models.Model):
  CATEGORÍA = (
            ('Lente', 'Lente'),
            ('Otro', 'Otro'),
            )
  DISTANCIA = (
              ('Lejos', 'Lejos'),
              ('Cerca', 'Cerca'),
              )
  LADO = (
          ('Izquierdo', 'Izquierdo'),
          ('Derecho', 'Derecho'),
          ('Ambos', 'Ambos'),
        )
  ARMAZÓN = (
              ('Sí', 'Sí'),
              ('No', 'No'),
            )
  nombre = models.CharField(max_length=100, null=True)
  precio = models.DecimalField(null=True, max_digits=20, decimal_places=2, default=0.00)
  categoría = models.CharField(max_length=50, null=True, choices=CATEGORÍA, default="Otro")
  distancia = models.CharField(max_length=15, null=True, blank=True, choices=DISTANCIA)
  lado = models.CharField(max_length=15, null=True, blank=True, choices=LADO)
  armazón = models.CharField(max_length=15, null=True, blank=True, choices=ARMAZÓN)
  descripción = models.CharField(max_length=100, null=True, blank=True)
  fecha_creación =  models.DateTimeField(auto_now_add=True, null=True)
  tags = models.ManyToManyField(Tag)
  stock = models.IntegerField(null=True, blank=True, default=0)
  
  def __str__(self):
    return self.nombre

  def tiene_stock(self):
    return self.stock > 0


class Pedido(models.Model):
  ESTADO = (
            ('Pendiente', 'Pendiente'),
            ('Pedido', 'Pedido'),
            ('Enviar a taller', 'Enviar a taller'),
            ('Finalizado', 'Finalizado')
            )
  PAGO = (
            ('Tarjeta de crédito', 'Tarjeta de crédito'),
            ('Tarjeta de débito', 'Tarjeta de débito'),
            ('Billetera virtual', 'Billetera virtual'),
            ('Efectivo', 'Efectivo'),
            )
  paciente = models.ForeignKey('pacientes.Paciente', null=True, on_delete=models.CASCADE)
  fecha_creación =  models.DateTimeField(auto_now_add=True, null=True)
  # precio_total = models.DecimalField(default=0.00, decimal_places=2, max_digits=20)
  estado = models.CharField(max_length=20, null=True, choices=ESTADO)
  producto = models.ForeignKey(Producto, null=True, on_delete=models.CASCADE)
  cantidad = models.PositiveIntegerField(default=1)
  pago = models.CharField(max_length=20, null=True, choices=PAGO)
  vendedor = models.ForeignKey('pedidos.Vendedor', null=True, on_delete=models.CASCADE)

  # class Meta:
  #   unique_together = ('pedido', 'producto')

  def __str__(self):
    return f"Pedido N.º {self.id}, creado el: {self.fecha_creación.month}-{self.fecha_creación.day}-{self.fecha_creación.year}"

  # def save(self, *args, **kwargs):
  #   self.precio_subtotal = self.precio_unitario * self.cantidad
  #   self.pedido.save()

  # def precio_final(self):
  #   return f'{self.precio_final}'


# class PedidoProducto(models.Model):
#   producto = models.ForeignKey(Producto, null=True, on_delete=models.CASCADE)
#   cantidad = models.PositiveIntegerField(default=1)
#   pedido = models.ForeignKey(Pedido, null=True, on_delete=models.CASCADE)
#   paciente = models.ForeignKey('pacientes.Paciente', null=True, on_delete=models.CASCADE)

#   class Meta:
#     unique_together = ('pedido', 'producto')

  # def __str__(self):
  #   return f'{self.producto__nombre}

class Vendedor(models.Model):
  nombre = models.CharField(max_length=200, null=True)
  fecha_creación = models.DateTimeField(auto_now_add=True, null=True)

  def __str__(self):
    return self.nombre