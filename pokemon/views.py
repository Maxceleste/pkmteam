from django.shortcuts import render
from .models import CadastroPokemon

def index (request):
    lista_pokemon_completa = CadastroPokemon.objects.order_by('numero_pokedex').filter(publicado=True)
    
    primeiro_pokemon = lista_pokemon_completa.first()
    
    lista_pokemon = lista_pokemon_completa.exclude(id = primeiro_pokemon.id)
    

    

    dados = {
        'lista_pokemon' : lista_pokemon,
        'primeiro_pokemon' : primeiro_pokemon
    }

    return render(request, 'index.html', dados)
