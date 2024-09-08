from django.urls import path


from . import views

app_name = 'calculator'

urlpatterns = [
    path('enviarOperacion/', views.processData, name="processData" ),
]
