from django.forms import ModelForm, DateTimeField, CharField, Textarea

from django import forms
from .models import Paciente
from turnos.models import Turno


class PacienteForm(ModelForm):

  class Meta:
    model = Paciente
    fields = ['nombre', 'teléfono', 'email', 'historial']
    # historial = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20, "style": "resize: none"}))
    widgets = {    
      'historial': Textarea(attrs={'cols': 50, 'rows': 5})
    }

class TurnoForm(ModelForm):

  class Meta:
    model = Turno
    fields = ['paciente', 'turno_dia', 'turno_hora', 'estado_turno', 'médico']
    # widgets = {
    # 'turno': forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])
    # }
    # widgets = {
    # 'turno': forms.DateInput(format='%d/%m/%Y')
    # }

    # turno = forms.DateField(forms.DateField(
    #     widget=DateTimePickerInput(format='%m/%d/%Y')))

    # widgets = {'turno': DateTimePickerInput(format='%m/%d/%Y')}
    # turno = forms.DateTimeField(input_formats=['%d/%m/%y %H:%M'])