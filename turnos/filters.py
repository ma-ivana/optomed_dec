from .models import *
import django_filters 
from django_filters import DateFilter, DateFromToRangeFilter


class FiltroMedico(django_filters.FilterSet):
  dia = django_filters.NumberFilter(field_name='turno_dia', lookup_expr='day')
  mes = django_filters.NumberFilter(field_name='turno_dia', lookup_expr='month')
  año = django_filters.NumberFilter(field_name='turno_dia', lookup_expr='year')
  semana = django_filters.DateFromToRangeFilter(field_name='turno_dia')
  
  class Meta:
    model = Turno 
    fields = ['paciente', 'turno_dia']

f = FiltroMedico({'date_after': '2016-01-01', 'date_before': '2016-02-01'})