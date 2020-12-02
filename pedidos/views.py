from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from pacientes.models import *
from pacientes.views import *
from django.forms import modelformset_factory
from .forms import ProductoForm, PedidoForm

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
def index(request):
  return render(request, "pedidos/index.html", context)

def pedidos(request):
  return render(request, "pedidos/pedidos.html", context)

def productos(request):
  return render(request, "pedidos/productos.html", context)

def tags(request):
  return render(request, "pedidos/tags.html", context)

def pedido_completo(request, pedido_id):
  unPedido = Pedido.objects.get(pk=pedido_id)
  pedido_seleccionado = Pedido.objects.filter(pedido=unPedido)
  subtotal = 0
  total = 0
  for item in pedido_seleccionado:
    subtotal = item.producto.precio * item.cantidad
    total = total + subtotal
  
  contexto_pedido = {"unPedido": unPedido, "pedido_seleccionado": pedido_seleccionado, "total": total}
  
  return render(request, "pedidos/pedido_completo.html", contexto_pedido)

def crearPedido(request):
  context_crearPedido = {}
  return render(request, 'pedidos/formulario_pedido.html', context_crearPedido)

def inicio(request):
  return render(request, 'pedidos/inicio.html', context)

def estado(request):
  return render(request, 'pedidos/estado.html', context)

# def hacerPedido(request):
#   # form = PedidoProductoForm()
#   # if request.method == 'POST':
#   #   # print('Printing POST:', request.POST)
#   #   form = PedidoProductoForm(request.POST)
#   #   if form.is_valid():
#   #     form.save()
#   #     # form.save_m2m()
#   #     return redirect(inicio)

#   # context_pedido = {'form': form}
#   formset = PedidoProductoFormSet()
#   if request.method == "POST":
#     formset = PedidoProductoFormSet(request.POST)
#     if formset.is_valid():
#       formset.save()
#       return redirect(inicio)
#   context_pedido = {'form': formset }
#   return render(request, 'pedidos/hacer_pedido.html', context_pedido)


# def hacerPedido(request, pk):
#   paciente = Paciente.objects.get(id=pk)
#   PedidoProductoFormset = modelformset_factory(PedidoProducto, fields=('producto', 'cantidad'))
#   formset = PedidoProductoFormset(queryset=PedidoProducto.objects.all())
#   context_pedido = {'form': formset }
#   return render(request, 'pedidos/hacer_pedido.html', context_pedido)

def hacerPedido(request, pk):
  paciente = Paciente.objects.get(pk=pk)
  form = PedidoForm(initial={'paciente': paciente})
  if request.method == 'POST':
    form = PedidoForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('pacientes:panel_paciente', pk=pk)
  context_pedido = {'form': form, 'pk': pk }
  return render(request, 'pedidos/hacer_pedido.html', context_pedido)

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

def vendedores(request):
  return render(request, "pedidos/vendedores.html", context)

def vendedor(request, pk):
  vendedor = Vendedor.objects.get(pk=pk)  
  # pedido = paciente.pedido_set.all()
  pedidos_vendedor = vendedor.pedido_set.all().count()
  context_vendedor = { 'paciente': paciente, 'vendedor': vendedor, 'pedidos_vendedor': pedidos_vendedor }
  return render(request, "pedidos/vendedor.html", context_vendedor)

def actualizarPedido(request, pk):
  pedido = Pedido.objects.get(id=pk)
  form = PedidoForm(instance=pedido)
  paciente_id = pedido.paciente.pk
  
  if request.method == 'POST':
    form = PedidoForm(request.POST, instance=pedido)
    if form.is_valid():
      form.save()
      # context_paciente = {'paciente_id': paciente_id}
      return redirect('pacientes:panel_paciente', pk=paciente_id)
  context= {'form': form}
  return render(request, 'pedidos/hacer_pedido.html', context)

def borrarPedido(request, pk):
  pedido = Pedido.objects.get(id=pk)
  paciente_id = pedido.paciente.pk
  if request.method == "POST":
    pedido.delete()
    return redirect('pacientes:panel_paciente', pk=paciente_id)
  context = {'item': pedido}
  return render(request, 'pedidos/borrar.html', context)