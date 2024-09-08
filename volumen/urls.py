from django.urls import path

from . import views


app_name ='volumen'

urlpatterns = [
    path('volumenCilindro/',views.calcularVolumen, name="c"),
]
