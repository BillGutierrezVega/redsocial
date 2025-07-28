from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.iniciar_sesion , name='login'),
    path('logout/', views.cerrar_sesion , name='logout'),
    
    path('registro/', views.registro_paso1, name='registro_paso1'),
    path('registro/gustos/', views.registro_paso2, name='registro_paso2'),

    #path('perfil/', views.perfil_usuario, name='perfil_usuario'),
    #path('perfil/editar/', views.editar_perfil, name='editar_perfil'),
]
