from django.shortcuts import render
from .models import CadastroPokemon

def index (request):
    lista_pokemon = CadastroPokemon.objects.order_by('numero_pokedex').filter(publicado=True)
    
    primeiro_pokemon = lista_pokemon.first()

    if primeiro_pokemon != None:
        lista_pokemon = lista_pokemon.exclude(id = primeiro_pokemon.id)
    

    dados = {
        'lista_pokemon' : lista_pokemon,
        'primeiro_pokemon' : primeiro_pokemon
    }

    return render(request, 'index.html', dados)
