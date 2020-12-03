from django.forms import ModelForm, ModelChoiceField, DecimalField, inlineformset_factory, CharField
from django import forms
from .models import Pedido, Producto

# class PedidoProductoForm(ModelForm):
#   productos = Producto.objects.all()
#   class Meta:
       
#     def __init__(self, *args, **kwargs):
#       super(PedidoProductoForm, self)._init_(*args, **kwargs)
      # for producto in productos:
      #   precio = self.producto.precio
      # self.fields['precio'].widget.attrs['readonly'] = True
    #   self.fields['precio']=forms.ModelChoiceField(queryset=Producto.objects.filter(producto=self.producto))
    #   print(precio)

    # model = PedidoProducto
    # fields = ['producto', 'cantidad']
      

class ProductoForm(ModelForm):

  class Meta:
    model = Producto
    fields = '__all__'

# class PedidoForm(ModelForm):
#   class Meta:
#     model = Pedido  
#     fields = '__all__'
#     # fields = [list]

# class PedidoProductoForm(ModelForm):
#   class Meta:
#     model = PedidoProducto
#     fields = ['producto', 'cantidad']
    
#   def __init__(self, *args, **kwargs):
#     super(PedidoProductoForm, self).__init__(*args, **kwargs)
#     self.fields['precio'].queryset=Producto.objects.all(producto=1)

# PedidoProductoFormSet = inlineformset_factory(Producto, PedidoProducto, fields=('cantidad', 'producto'))

# class PedidoProductoForm(ModelForm):
#   class Meta:
#     model = PedidoProducto
#     fields = ['paciente', 'producto', 'cantidad']

class PedidoForm(ModelForm):
  class Meta:
    model = Pedido
    fields = ['paciente', 'producto', 'cantidad', 'estado']

class PedidoFormTaller(ModelForm):
  class Meta:
    model = Pedido  
    fields = ['estado']

