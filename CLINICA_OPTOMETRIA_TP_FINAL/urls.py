"""CLINICA_OPTOMETRIA_TP_FINAL URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from pedidos import views as inicio_view
from pacientes import views as paciente_view
from accounts import views as account_view

urlpatterns = [
    path('', account_view.home, name="home"),
    path('admin/', admin.site.urls),
    path('pedidos/', include("pedidos.urls")),
    path('pacientes/', include("pacientes.urls")),
    path('inicio/', inicio_view.inicio, name="inicio"),
    path('productos/', inicio_view.productos, name="productos"),
    path('accounts/', include("accounts.urls")),
    path('panel_paciente', paciente_view.panel_paciente, name="panel_paciente"),
    path('home_new', account_view.home, name="home_new"),
]
