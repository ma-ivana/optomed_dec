from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from pedidos.models import *

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
    context_paciente = {'paciente': paciente,
                        'pedido': pedido, 'pedidos_paciente': pedidos_paciente}
    return render(request, "pacientes/paciente.html", context_paciente)


def panel_paciente(request):
    return render(request, "pacientes/panel_paciente.html", context)



