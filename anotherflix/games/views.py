from django.shortcuts import render
from rest_framework import viewsets
from .models import Game
from .serializers import GameSerializer

def game_list(request):
    games = Game.objects.all()
    return render(request, 'games/game_list.html', {'games': games})

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer