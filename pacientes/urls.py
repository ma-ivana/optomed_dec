from django.urls import path
from . import views

app_name = 'pacientes'
urlpatterns = [
    path("", views.index, name="index"),
    path("paciente/<int:paciente_id>", views.paciente, name="paciente"),
    path("panel_paciente/<str:pk>", views.panel_paciente, name="panel_paciente"),

    
]