from django.urls import path
from . import views

app_name = 'pacientes'
urlpatterns = [
    path("", views.index, name="index"),
    path("paciente/<int:paciente_id>", views.paciente, name="paciente"),
    path("panel_paciente/<int:pk>", views.panel_paciente, name="panel_paciente"),
    path("nuevo_paciente/", views.nuevoPaciente, name="nuevo_paciente"),
    # path("nuevo_turno/", views.nuevoTurno, name="nuevo_turno"),
    path("actualizar_paciente/<int:pk>", views.actualizarPaciente, name="actualizar_paciente"),
    path("borrar_paciente/<int:pk>", views.borrarPaciente, name="borrar_paciente"),
    # path("actualizar_turno/<int:pk>", views.actualizarTurno, name="actualizar_turno"),
    # path("borrar_turno/<int:pk>", views.borrarTurno, name="borrar_turno"),
]