from argparse import HelpFormatter
from itertools import tee
from django.db import models
from django.core.validators import RegexValidator
from .pokeapi import PokemonAPI

class CadastroPokemon(models.Model):

    tipos_dos_pokemons =(
        ('normal', 'Normal'), ('fogo', 'Fogo'),
        ('agua', 'Água'), ('grama', 'Grama'),
        ('voador', 'Voador'), ('lutador', 'Lutador'),
        ('veneno', 'Veneno'), ('eletrico', 'Elétrico'),
        ('terra', 'Terra'), ('pedra', 'Pedra'),
        ('psiquico', 'Psíquico'), ('gelo', 'Gelo'),
        ('inseto', 'Inseto'), ('fantasma', 'Fantasma'),
        ('ferro', 'Ferro'), ('dragao', 'Dragão'),
        ('sombrio', 'Sombrio'), ('fada', 'Fada')
    )

    nome = models.CharField(
        verbose_name = 'Nome do Pokémon',
        max_length = 100,
        help_text = 'Ex: Blaziken',
        error_messages = {'required' : 'Por favor, insira o nome do Pokémon.'},
        )

    numero_pokedex = models.IntegerField(
        verbose_name = 'Número da Pokédex',
        help_text = 'Ex: 1, 10, 100',
        error_messages = {'required' : 'É necessário escolher o número da pokedex.'},
    )

    tipo_1 = models.CharField(
        verbose_name = 'Primeiro tipo',
        help_text = 'Escolha um tipo para o pokémon',
        choices = tipos_dos_pokemons,
        error_messages = {'required' : 'É necessário escolher o primeiro tipo.'},
        max_length = 50
    )

    tipo_2 = models.CharField(
        verbose_name = 'Segundo tipo',
        help_text = 'Escolha o segundo tipo para o pokémon, se necessário',
        choices = tipos_dos_pokemons,
        null = True,
        blank = True,
        max_length = 50
    )

    hp = models.IntegerField(
        verbose_name = 'Valor da vida do pokémon',
        help_text = 'Ex: 87',
        default = 50,
        editable = False
    )

    ataque = models.IntegerField(
        verbose_name = 'Valor de ataque do pokémon',
        help_text = 'Ex: 55',
        default = 50,
        editable = False
    )

    defesa = models.IntegerField(
        verbose_name = 'Valor de defesa do pokémon',
        help_text = 'Ex: 76',
        default = 50,
        editable = False
    )

    ataque_especial = models.IntegerField(
        verbose_name = 'Valor do Sp.Atk (ataque especial) do pokémon',
        help_text = 'Ex: 34',
        default = 50,
        editable = False
    )

    defesa_especial = models.IntegerField(
        verbose_name = 'Valor do Sp.Def (defesa especial) do pokémon',
        help_text = 'Ex: 45',
        default = 50,
        editable = False
    )

    velocidade = models.IntegerField(
        verbose_name = 'Velocidade',
        help_text = 'Ex: 75',
        default = 50,
        editable = False
    )

    total = models.IntegerField(
        verbose_name = 'Total',
        default = 300,
        editable = False
    )

    habilidade_1 = models.CharField(
        verbose_name = 'Primeira habilidade',
        help_text = 'Ex: Calda de ferro',
        max_length = 50,
        error_messages = {'required' : 'Por favor, insira essa habilidade do pokémon.'},
    )

    habilidade_2 = models.CharField(
        verbose_name = 'Segunda habilidade',
        help_text = 'Ex: Chute duplo',
        max_length = 50,
        error_messages = {'required' : 'Por favor, insira essa habilidade do pokémon.'},
    )

    habilidade_3 = models.CharField(
        verbose_name = 'Terceira habilidade',
        help_text = 'Ex: Endurecer',
        max_length = 50,
        error_messages = {'required' : 'Por favor, insira essa habilidade do pokémon.'},
    )

    habilidade_4 = models.CharField(
        verbose_name = 'Quarta habilidade',
        help_text = 'Ex: Investida',
        max_length = 50,
        error_messages = {'required' : 'Por favor, insira essa habilidade do pokémon.'},
    )

    publicado = models.BooleanField(
        default = False,
        verbose_name = 'Publicado',
        help_text = 'Marque a opção se quer que o pokémon seja exibido no site.',
        
    )

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        try:
            hp_api = PokemonAPI().get_status('hp', self.numero_pokedex)
            ataque_api = PokemonAPI().get_status('ataque', self.numero_pokedex)
            defesa_api = PokemonAPI().get_status('defesa', self.numero_pokedex)
            ataque_especial_api = PokemonAPI().get_status('ataque_especial', self.numero_pokedex)
            defesa_especial_api = PokemonAPI().get_status('defesa_especial', self.numero_pokedex)
            velocidade_api = PokemonAPI().get_status('velocidade', self.numero_pokedex)

            self.hp = hp_api
            self.ataque = ataque_api
            self.defesa = defesa_api
            self.ataque_especial = ataque_especial_api
            self.defesa_especial = defesa_especial_api
            self.velocidade = velocidade_api
            self.total = hp_api + ataque_api + defesa_api + ataque_especial_api + defesa_especial_api + velocidade_api

            super().save(*args, **kwargs)
        except:
            super().save(*args, **kwargs)


