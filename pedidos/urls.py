from django.urls import path
from . import views
from pacientes.views import *

app_name = "pedidos"
urlpatterns = [
    path("", views.index, name="index"),
    path("inicio/", views.inicio, name="inicio"),
    path("pedidos/", views.pedidos, name="pedidos"),
    path("pedido/<int:pedido_id>", views.pedido_completo, name="pedido_completo"),
    path("productos/", views.productos, name="productos"),
    path("tags/", views.tags, name="tags"),
    path("hacer_pedido/<int:pk>", views.hacerPedido, name="hacer_pedido"),
    path("nuevo_producto/", views.nuevoProducto, name="nuevo_producto"),
    path("panel_paciente/<int:pk>", views.panel_paciente, name="panel_paciente"),
    path("vendedores/", views.vendedores, name="vendedores"),
    path("vendedor/<int:pk>", views.vendedor, name="vendedor"),
    path("actualizar_pedido/<int:pk>", views.actualizarPedido, name="actualizar_pedido"),
    path("borrar_pedido/<int:pk>", views.borrarPedido, name="borrar_pedido"),
    path("pedidos_taller", views.pedidosTaller, name="pedidos_taller"),
    path("pedido_taller_form/<int:pk>", views.actualizarPedidoTaller, name="pedido_taller_form"),
    path("inicio_gerencia/", views.inicioGerencia, name="inicio_gerencia"),
]
