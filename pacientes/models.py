from django.db import models

# Create your models here.
class Paciente(models.Model):
  nombre = models.CharField(max_length=200, null=True)
  teléfono = models.CharField(max_length=200, null=True)
  email = models.CharField(max_length=200, null=True)
  fecha_creación = models.DateTimeField(auto_now_add=True, null=True)
  historial = models.CharField(max_length=1500, null=True)

  def __str__(self):
    return self.nombre