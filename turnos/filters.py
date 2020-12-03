from .models import *
import django_filters 
from django_filters import DateFilter

class FiltroMedico(django_filters.FilterSet):
  dia = django_filters.NumberFilter(field_name='turno_dia', lookup_expr='day')
  mes = django_filters.NumberFilter(field_name='turno_dia', lookup_expr='month')
  año = django_filters.NumberFilter(field_name='turno_dia', lookup_expr='year')
  class Meta:
    model = Turno 
    fields = ['paciente']