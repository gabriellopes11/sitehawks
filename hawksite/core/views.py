from django.shortcuts import render
from .models import Player

def home(request):
    return render(request, 'core/home.html')

def elenco(request):
    jogadores = Player.objects.all()
    return render(request, 'core/elenco.html', {'jogadores': jogadores})

def home(request):
    jogadores = Player.objects.all()[:4]  # pega apenas 4 jogadores
    return render(request, 'core/home.html', {'jogadores': jogadores})


def elenco(request):
    jogadores = Player.objects.all()
    return render(request, 'core/elenco.html', {'jogadores': jogadores})