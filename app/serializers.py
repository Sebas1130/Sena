# serializers.py
from rest_framework import serializers
from .models import Empleado

class EmpleadoSerializer(serializers.ModelSerializer):
    salario = serializers.SerializerMethodField()

    class Meta:
        model = Empleado
        fields = ['horas_laboradas', 'tarifa_por_hora', 'salario']

    def get_salario(self, obj):
        return obj.calcular_planilla()
