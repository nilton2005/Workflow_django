import math

from django.shortcuts import render

# Create your views here.
def calcularVolumen(request):
    if(request.method == "POST"):
        a = float(request.POST['diametro'])
        b = float( request.POST['altura'])
        r = (a / 2)**2
        vT = math.pi * r * b
        context = {
            'volumenTotal' : vT
        }

        return render(request, 'calc/respuesta.html', context)
    return render(request, 'calc/volumen.html')