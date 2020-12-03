from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from pacientes.models import *
from turnos.models import *
from pacientes.views import *
from django.forms import modelformset_factory
from .forms import ProductoForm, PedidoForm, PedidoFormTaller
from .filters import FiltroPedidos
from turnos.filters import FiltroMedico

from accounts.decorators import unauthenticated_user
from accounts.decorators import allowed_users
from accounts.decorators import admin_only
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
# Create your views here.
pedidos = Pedido.objects.all()
productos = Producto.objects.all()
tags = Tag.objects.all()
pacientes = Paciente.objects.all()
vendedores = Vendedor.objects.all()
pedidos_productos = Pedido.objects.all()
total_pedidos = pedidos.count()
finalizados = pedidos.filter(estado="Finalizado").count()
pendientes = pedidos.filter(estado="Pendiente").count()
ultimos_cinco = Pedido.objects.all().order_by('-id')[:5]

context = {'pedidos': pedidos, 'productos': productos, 'tags': tags, 'pacientes': pacientes, 'total_pedidos': total_pedidos, 'finalizados': finalizados, 'pendientes': pendientes, 'ultimos_cinco': ultimos_cinco}

# Create your views here.
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'ventas'])
def index(request):
  return render(request, "pedidos/index.html", context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'ventas'])
def pedidos(request):
  return render(request, "pedidos/pedidos.html", context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'ventas'])
def productos(request):
  return render(request, "pedidos/productos.html", context)

def tags(request):
  return render(request, "pedidos/tags.html", context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'ventas'])
def pedido_completo(request, pedido_id):
  unPedido = Pedido.objects.get(pk=pedido_id)
  pedido_seleccionado = Pedido.objects.filter(id=unPedido.pk)
  subtotal = 0
  total = 0
  for item in pedido_seleccionado:
    subtotal = item.producto.precio * item.cantidad
    total = total + subtotal
  
  contexto_pedido = {"unPedido": unPedido, "pedido_seleccionado": pedido_seleccionado, 'id': pedido_id, "total": total}
  
  return render(request, "pedidos/pedido_completo.html", contexto_pedido)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'ventas'])
def crearPedido(request):
  context_crearPedido = {}
  return render(request, 'pedidos/formulario_pedido.html', context_crearPedido)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'ventas'])
def nuevoProducto(request):
  form = ProductoForm()
  if request.method == 'POST':
    # print('Printing POST:', request.POST)
    form = ProductoForm(request.POST)
    if form.is_valid():
      form.save()
      # form.save_m2m()
      return redirect(productos)

  context_pedido = {'form': form}
  return render(request, 'pedidos/nuevo_producto.html', context_pedido)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'ventas'])
def inicio(request):
  pedidos=Pedido.objects.all()
  filtro_pedidos = FiltroPedidos(request.GET, queryset=pedidos)
  pedidos = filtro_pedidos.qs
  context = {'pedidos': pedidos, 'productos': productos, 'tags': tags, 'pacientes': pacientes, 'total_pedidos': total_pedidos, 'finalizados': finalizados, 'pendientes': pendientes, 'ultimos_cinco': ultimos_cinco, 'filtro_pedidos': filtro_pedidos}
  return render(request, 'pedidos/inicio.html', context)

def estado(request):
  return render(request, 'pedidos/estado.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'ventas'])
def hacerPedido(request, pk):
  paciente = Paciente.objects.get(pk=pk)
  form = PedidoForm(initial={'paciente': paciente})
  if request.method == 'POST':
    form = PedidoForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('pedidos:inicio')
  context_pedido = {'form': form, 'pk': pk }
  return render(request, 'pedidos/hacer_pedido.html', context_pedido)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'ventas'])
def vendedores(request):
  return render(request, "pedidos/vendedores.html", context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'ventas'])
def vendedor(request, pk):
  vendedor = Vendedor.objects.get(pk=pk)  
  # pedido = paciente.pedido_set.all()
  pedidos_vendedor = vendedor.pedido_set.all().count()
  context_vendedor = { 'paciente': paciente, 'vendedor': vendedor, 'pedidos_vendedor': pedidos_vendedor }
  return render(request, "pedidos/vendedor.html", context_vendedor)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'ventas'])
def actualizarPedido(request, pk):
  pedido = Pedido.objects.get(id=pk)
  form = PedidoForm(instance=pedido)
  paciente_id = pedido.paciente.pk
  
  if request.method == 'POST':
    form = PedidoForm(request.POST, instance=pedido)
    if form.is_valid():
      form.save()
      # context_paciente = {'paciente_id': paciente_id}
      return redirect('pedidos:inicio')
  context= {'form': form}
  return render(request, 'pedidos/hacer_pedido.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'ventas'])
def borrarPedido(request, pk):
  pedido = Pedido.objects.get(id=pk)
  paciente_id = pedido.paciente.pk
  if request.method == "POST":
    pedido.delete()
    return redirect('pedidos:inicio')
  context = {'item': pedido}
  return render(request, 'pedidos/borrar.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'ventas','taller'])
def actualizarPedidoTaller(request, pk):
  pedido = Pedido.objects.get(id=pk)
  form = PedidoFormTaller(instance=pedido)
   
  if request.method == 'POST':
    form = PedidoFormTaller(request.POST, instance=pedido)
    if form.is_valid():
      form.save()
      return redirect('pedidos:pedidos_taller')
  context_taller= {'form': form, 'pk': pk}
  return render(request, 'pedidos/pedido_taller_form.html', context_taller)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'ventas','taller'])
def pedidosTaller(request):
  return render(request, "pedidos/pedidos_taller.html", context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'gerencia'])
def inicioGerencia(request):
  pedidos=Pedido.objects.all()
  turnos=Turno.objects.all()
  filtro_pedidos = FiltroPedidos(request.GET, queryset=pedidos)
  filtro_turnos = FiltroMedico(request.GET, queryset=turnos)
  pedidos = filtro_pedidos.qs
  turnos = filtro_turnos.qs
  context = {'pedidos': pedidos, 'productos': productos, 'tags': tags, 'pacientes': pacientes, 'total_pedidos': total_pedidos, 'finalizados': finalizados, 'pendientes': pendientes, 'ultimos_cinco': ultimos_cinco, 'filtro_pedidos': filtro_pedidos, 'filtro_turnos': filtro_turnos, 'turnos': turnos}
  return render(request, 'pedidos/inicio_gerencia.html', context)