from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from turnos.models import *
from pedidos.models import *
from .forms import PacienteForm, TurnoForm

# Create your views here.

pacientes = Paciente.objects.all()
pedidos = Pedido.objects.all()  
context = {'pacientes': pacientes, 'pedidos': pedidos}

def index(request):  
  return render(request, "pacientes/index.html", context)

def paciente(request, paciente_id): 
  paciente = Paciente.objects.get(id=paciente_id)
  pedido = paciente.pedido_set.all()
  pedidos_paciente = paciente.pedido_set.all().count()
  turnos_paciente = paciente.turno_set.all().count()
  context_paciente = { 'paciente': paciente, 'pedido': pedido, 'pedidos_paciente': pedidos_paciente, 'turnos_paciente': turnos_paciente }
  return render(request, "pacientes/paciente.html", context_paciente)


def panel_paciente(request, pk):
  paciente = Paciente.objects.get(pk=pk)  
  pedido = paciente.pedido_set.all()
  pedidos_paciente = paciente.pedido_set.all().count()
  context_paciente = { 'paciente': paciente, 'pedido': pedido, 'pedidos_paciente': pedidos_paciente }
  return render(request, "pacientes/panel_paciente.html", context_paciente)

def nuevoPaciente(request):
  form = PacienteForm()
  if request.method == "POST":
    form = PacienteForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('pacientes:index')
  context = { 'form': form }
  return render(request, "pacientes/nuevo_paciente.html", context)

def actualizarPaciente(request, pk):
  paciente = Paciente.objects.get(id=pk)
  form = PacienteForm(instance=paciente)
    
  if request.method == 'POST':
    form = PacienteForm(request.POST, instance=paciente)
    if form.is_valid():
      form.save()
      # context_paciente = {'paciente_id': paciente_id}
      return redirect('pacientes:index')
  context= {'form': form}
  return render(request, 'pacientes/nuevo_paciente.html', context)

def borrarPaciente(request, pk):
  paciente = Paciente.objects.get(id=pk)
  if request.method == "POST":
    paciente.delete()
    return redirect('pacientes:index')
  context = {'item': paciente}
  return render(request, 'pacientes/borrar.html', context)

def paciente_medico(request, pk): 
  paciente = Paciente.objects.get(id=pk)
  turnos_paciente = paciente.turno_set.all().count()
  
  form = PacienteForm(instance=paciente)
    
  if request.method == 'POST':
    form = PacienteForm(request.POST, instance=paciente)
    if form.is_valid():
      form.save()
      # context_turno = {'pk': paciente.pk}
      return redirect('pacientes:paciente_medico', pk)
  
  context_paciente = { 'paciente': paciente, 'turnos_paciente': turnos_paciente, 'form': form }
  return render(request, "pacientes/paciente_medico.html", context_paciente)