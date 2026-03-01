from django.shortcuts import render
from .models import Player

def home(request):
    return render(request, 'core/home.html')

def elenco(request):
    jogadores = Player.objects.all()
    return render(request, 'core/elenco.html', {'jogadores': jogadores})