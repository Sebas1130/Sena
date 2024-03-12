from django.urls import path
from . import views

urlpatterns = [
    path('empleados/', views.crear_empleado, name='empleados'),
    path('calcularPuntaje/', views.calcular_puntaje_total, name='calcularPuntaje'),
]