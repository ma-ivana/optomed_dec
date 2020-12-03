from .models import *
import django_filters

class FiltroMedico(django_filters.FilterSet):
  class Meta:
    model = Turno 
    fields = ['turno_dia']