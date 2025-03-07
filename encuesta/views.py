from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'titulo': "FormularIto",
    }
    return render(request, 'encuesta/formulario.html', context)


def enviar(request):
    context ={
        'titulo' : "Respuesta del formulario ☆*: .｡. o(≧▽≦)o .｡.:*☆",
        'nombre' : request.POST['nombre'],
        'clave' : request.POST['password'],
        'educacion' : request.POST['educacion'],
        'nacionalidad': request.POST['nacionalidad'],
        'idiomas' : request.POST.getlist('idiomas'),
        'correo' : request.POST['email'],
        'website' : request.POST['sitioweb'],

    }
    return render(request,'encuesta/respuesta.html', context)
