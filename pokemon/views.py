from django.shortcuts import render
from .models import CadastroPokemon

def index (request):
    lista_pokemon_completa = CadastroPokemon.objects.order_by('numero_pokedex').filter(publicado=True)
    print('lista completa:', lista_pokemon_completa)
    primeiro_pokemon = lista_pokemon_completa.first()
    print('primeiro pokemon:', primeiro_pokemon)
    lista_pokemon = lista_pokemon_completa.exclude(id = primeiro_pokemon.id)
    print('resto dos pokemons:', lista_pokemon)

    

    dados = {
        'lista_pokemon' : lista_pokemon,
        'primeiro_pokemon' : primeiro_pokemon
    }

    return render(request, 'index.html', dados)
