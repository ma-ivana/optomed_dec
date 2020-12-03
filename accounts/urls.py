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

    #path('home/', v.pedidos, name="home"),
    path('adm', views.adm, name="adm"),
    #path('indexsecretaria/', views.indexsecretaria, name="indexsecretaria"),
    path('indexsecretaria/', v2.index, name="indexsecretaria"),
    #path('indexprofmed/', views.indexprofmed, name="indexprofmed"),
    path('indexprofmed/', v3.medico, name="indexprofmed"),
    #path('indexventas/', views.indexventas, name="indexventas"),
    path("indexventas/", v.inicio, name="indexventas"),
    #path('indextaller/', views.indextaller, name="indextaller"),
    path('indextaller/', v.pedidosTaller, name="indextaller"),
    path('indexgerencia/', views.indexgerencia, name="indexgerencia"),
]
