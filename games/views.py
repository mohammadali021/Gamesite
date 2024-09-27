from django.shortcuts import render

from games import models
from games.models import Game, GameDetails


def index(request):
    AllGames = Game.objects.all()
    return render(request, 'games/index.html', {'AllGames': AllGames})


def AboutUs(request):
    return render(request, 'games/about-us.html')


def Aboutschool(request):
    return render(request, 'games/about-school.html')


def GameDetail(request, s):
    Gamedetail = Game.objects.get(slug=s)
    return render(request, 'games/game-details.html', {'Game': Gamedetail})

# Create your views here.
