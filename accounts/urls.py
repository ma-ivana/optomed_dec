from django.urls import path
from . import views
from pedidos import views as v
from pacientes import views as v2
from turnos import views as v3
app_name = 'accounts'

urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('user/', views.userPage, name="user-page"),
    path('adm', views.adm, name="adm"),
    path('indexsecretaria/', v2.index, name="indexsecretaria"),
    path("indexprofmed/", v3.medicos, name="indexprofmed"),
    path("indexventas/", v.inicio, name="indexventas"),
    path('indextaller/', v.pedidosTaller, name="indextaller"),
    path('indexgerencia/', v.inicioGerencia, name="indexgerencia"),
]
