from django.contrib import admin
from .models import CadastroPokemon

class DisplayPokemon(admin.ModelAdmin):
    list_display = ('numero_pokedex', 'nome', 'tipo_1', 'tipo_2', 'publicado',)
    list_display_links = ('numero_pokedex', 'nome',)
    search_fields = ('nome',)
    list_per_page = 20
    list_editable = ('publicado',)

admin.site.register(CadastroPokemon, DisplayPokemon)