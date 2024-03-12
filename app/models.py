from django.db import models

# Create your models here.

class Empleado(models.Model):
    horas_laboradas = models.FloatField()
    tarifa_por_hora = models.FloatField()

    def calcular_planilla(self):
        return self.horas_laboradas * self.tarifa_por_hora
