from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from pacientes.models import *
from pacientes.views import *
from pacientes.forms import PacienteForm, TurnoForm
from .filters import FiltroMedico
# from django.forms import modelformset_factory
# from .forms import ProductoForm, PedidoForm

# Create your views here.
turnos = Turno.objects.all()
medicos = Medico.objects.all()
pacientes = Paciente.objects.all()
context = {'turnos': turnos, 'medicos': medicos, 'pacientes': pacientes}

def turnos(request):
  return render(request, "turnos/turnos.html", context)

def nuevoTurno(request):
  form = TurnoForm()
  if request.method == "POST":
    form = TurnoForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('turnos:turnos')
  context = { 'form': form }
  return render(request, "turnos/nuevo_turno.html", context)

def actualizarTurno(request, pk):
  turno = Turno.objects.get(id=pk)
  form = TurnoForm(instance=turno)
    
  if request.method == 'POST':
    form = TurnoForm(request.POST, instance=turno)
    if form.is_valid():
      form.save()
      # context_paciente = {'paciente_id': paciente_id}
      return redirect('turnos:turnos')
  context= {'form': form}
  return render(request, 'turnos/nuevo_turno.html', context)

def borrarTurno(request, pk):
  turno = Turno.objects.get(id=pk)
  if request.method == "POST":
    turno.delete()
    return redirect('turnos:turnos')
  context = {'item': turno}
  return render(request, 'turnos/borrar.html', context)

def medicos(request):
  return render(request, "turnos/medicos.html", context)

# def parametro_es_valido(param):
#   return param != '' and param is not None
def busqueda(request, medico_id):
  turnos = Turno.objects.all()
  filtro_medico = FiltroMedico()
  medico = Medico.objects.get(pk=medico_id)
  pacientes = Paciente.objects.all()
  context_medico = {'turnos': turnos, 'medico': medico, 'pacientes': pacientes, 'filtro_medico': filtro_medico}
  return render(request, "turnos/medico.html", context_medico)

def medico(request, medico_id):
  medico = Medico.objects.get(pk=medico_id)
  turnos = Turno.objects.filter(médico__pk=medico_id)
  pacientes = Paciente.objects.all()
  # filtro_por_dia = request.GET.get('filtro_por_dia')

  # if parametro_es_valido(filtro_por_dia):
  #   turnos = turnos.filter(turno_dia=filtro_por_dia)


  context_medico = {'turnos': turnos, 'medico': medico, 'pacientes': pacientes}
  return render(request, "turnos/medico.html", context_medico)




