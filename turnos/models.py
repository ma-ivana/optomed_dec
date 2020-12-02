from django.db import models
from datetime import datetime, date, time

# Create your models here.
class Turno(models.Model):
  ESTADO = (
            ('Solicitado', 'Solicitado'),
            ('Cumplido', 'Cumplido'),
            ('No cumplido', 'No cumplido')
            )
  paciente = models.ForeignKey('pacientes.Paciente', null=True, on_delete=models.SET_NULL)
  turno_dia = models.DateField()
  turno_hora = models.TimeField()
  estado_turno = models.CharField(max_length=20, null=True, choices=ESTADO)
  médico = models.ForeignKey('turnos.Medico', null=True, on_delete=models.SET_NULL)

  def __str__(self):
    return f'Turno {self.turno_dia.date}-{self.turno_dia.month}-{self.turno_dia.year} a las {self.turno_hora} h'

class Medico(models.Model):
  nombre = models.CharField(max_length=200, null=True)
  especialidad = models.CharField(max_length=200, null=True)
  fecha_creación = models.DateTimeField(auto_now_add=True, null=True)

  def __str__(self):
    return f'Méd. {self.nombre} - {self.especialidad}'


