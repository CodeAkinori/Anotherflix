from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import game_list, GameViewSet

router = DefaultRouter()
router.register(r'api/games', GameViewSet)

urlpatterns = [
    path('', views.game_list, name='game_list'),
    # Adicione mais padrões de URL conforme necessário

    path('', include(router.urls)),
]
