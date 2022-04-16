from django.shortcuts import render
from .models import CadastroPokemon

def index (request):
    lista_pokemon_completa = CadastroPokemon.objects.order_by('numero_pokedex').filter(publicado=True)
    print('lista completa:', lista_pokemon_completa)
    primeiro_pokemon = lista_pokemon_completa.first()
    print('primeiro pokemon:', primeiro_pokemon)
    lista_pokemon = lista_pokemon_completa.exclude(id = primeiro_pokemon.id)
    print('resto dos pokemons:', lista_pokemon)
    tipos_formatados = {
        'normal' : 'Normal', 
        'fogo' : 'Fogo',
        'agua' : 'Água',
        'grama' : 'Grama',
        'voador' : 'Voador',
        'lutador' : 'Lutador',
        'veneno' : 'Veneno',
        'eletrico': 'Elétrico',
        'terra' : 'Terra',
        'pedra' : 'Pedra',
        'psiquico' : 'Psíquico',
        'gelo' : 'Gelo',
        'inseto' : 'Inseto',
        'fantasma' : 'Fantasma',
        'ferro' : 'Ferro',
        'dragao' : 'Dragão',
        'sombrio' : 'Sombrio',
        'fada' : 'Fada'
    }
    dados = {
        'lista_pokemon' : lista_pokemon,
        'tipos_formatados' : tipos_formatados,
        'primeiro_pokemon' : primeiro_pokemon
    }

    return render(request, 'index.html', dados)
