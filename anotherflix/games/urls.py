from django.urls import path
from . import views  # Importe suas views

urlpatterns = [
    path('', views.index, name='index'),  # Um exemplo de URL
    # Adicione mais padrões de URL conforme necessário
]
