from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("personas", views.personas_listar, name="personas"),
    path("nuevo_paciente", views.nuevo_paciente, name="nuevo_paciente"),
    path("modificar_personas/<int:pk>", views.modificar_persona, name='modificar_personas'),
    path("eliminar_persona/<int:pk>", views.eliminar_persona, name="eliminar_persona")


]