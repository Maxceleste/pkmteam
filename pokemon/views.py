from django.shortcuts import render
from .models import CadastroPokemon

def index (request):
    lista_pokemon = CadastroPokemon.objects.order_by('numero_pokedex').filter(publicado=True)

    dados = {
        'lista_pokemon' : lista_pokemon
    }

    return render(request, 'index.html', dados)
