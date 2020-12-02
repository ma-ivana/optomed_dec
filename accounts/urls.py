from django.urls import path
from . import views
from pedidos import views as v
app_name = 'accounts'

urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('user/', views.userPage, name="user-page"),

    #path('home/', v.pedidos, name="home"),
    path('adm', views.adm, name="adm"),
    path('indexsecretaria/', views.indexsecretaria, name="indexsecretaria"),
    path('indexprofmed/', views.indexprofmed, name="indexprofmed"),
    path('indexventas/', views.indexventas, name="indexventas"),
    path('indextaller/', views.indextaller, name="indextaller"),
    path('indexgerencia/', views.indexgerencia, name="indexgerencia"),
]
