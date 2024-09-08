from django.shortcuts import render

# Create your views here.
def processData(request):
    if request.method == "POST":    
        print("hellos ")
        operacion = request.POST['operations']
        a = int(request.POST['a'])
        b = int(request.POST['b'])
        if operacion == "plus":
            result = a + b
        elif(operacion == "substraction"):
            result =  a - b
        elif(operacion == "multiplication"):
            result =  a * b
        elif(operacion == "divi"):
            result =  a / b
        context = {
            'result' : result
        }
        return render(request, 'calculator/respuesta.html', context)
    return render(request, 'calculator/operacion.html')
