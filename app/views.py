# views.py
from .models import Empleado
from django.shortcuts import render
from django.http import JsonResponse

    
def crear_empleado(request):
    if request.method == 'POST':
        horas_laboradas = float(request.POST.get('horas_laboradas', 0))
        tarifa_por_hora = float(request.POST.get('tarifa_por_hora', 0))

        if horas_laboradas > 0 and tarifa_por_hora > 0:
            empleado = Empleado(horas_laboradas=horas_laboradas, tarifa_por_hora=tarifa_por_hora)
            salario = empleado.calcular_planilla()
            return JsonResponse({'salario': salario})
        else:
            return JsonResponse({'error': 'Debe proporcionar horas laboradas y tarifa por hora válidas.'}, status=400)
    else:
        return render(request, 'empleados.html')



def calcular_puntaje_total(request):
    partidos_ganados = int(request.POST.get('partidos_ganados', 0))
    partidos_perdidos = int(request.POST.get('partidos_perdidos', 0))
    partidos_empatados = int(request.POST.get('partidos_empatados', 0))

    puntaje_total = partidos_ganados * 3 + partidos_empatados * 1 + partidos_perdidos * 0
    return render(request, 'calcular_puntaje_total.html', {'puntaje_total': puntaje_total})

