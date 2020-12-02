from django.urls import path
from . import views

app_name = 'turnos'
urlpatterns = [
    path("", views.turnos, name="turnos"),
    path("medicos/", views.medicos, name="medicos"),
    path("medico/<int:medico_id>", views.medico, name="medico"),
    path("nuevo_turno/", views.nuevoTurno, name="nuevo_turno"),
    path("actualizar_turno/<int:pk>", views.actualizarTurno, name="actualizar_turno"),
    path("borrar_turno/<int:pk>", views.borrarTurno, name="borrar_turno"),
]
