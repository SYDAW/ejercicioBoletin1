from django.urls import path
from  ejercicio1 import views

urlpatterns = [
    path('', views.crearFormulario, name='crearFormulario'),
]