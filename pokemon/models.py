from itertools import tee
from django.db import models
from django.core.validators import RegexValidator

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

    numero_pokedex = models.CharField(
        verbose_name = 'Número da Pokédex',
        max_length = 3,
        help_text = 'Ex: 001',
        validators=[ RegexValidator(r'^\d\d\d$', message = 'Insira um número válido.')  ],
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
        help_text = 'Ex: 87'
    )

    ataque = models.IntegerField(
        verbose_name = 'Valor de ataque do pokémon',
        help_text = 'Ex: 55'
    )

    defesa = models.IntegerField(
        verbose_name = 'Valor de defesa do pokémon',
        help_text = 'Ex: 76'
    )

    ataque_especial = models.IntegerField(
        verbose_name = 'Valor do Sp.Atk (ataque especial) do pokémon',
        help_text = 'Ex: 34'
    )

    defesa_especial = models.IntegerField(
        verbose_name = 'Valor do Sp.Def (defesa especial) do pokémon',
        help_text = 'Ex: 45'
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


