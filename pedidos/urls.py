from django.urls import path
from . import views

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

]
