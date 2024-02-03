from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from .models import Game
from .serializers import GameSerializer


def game_list(request: HttpRequest) -> HttpResponse:
    games = Game.objects.all()
    context = {
        'games': games
    }
    return render(request, 'games/game_list.html', context)

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer