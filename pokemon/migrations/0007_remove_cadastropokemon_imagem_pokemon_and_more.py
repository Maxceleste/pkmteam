# Generated by Django 4.0.3 on 2022-04-20 20:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0006_alter_cadastropokemon_numero_pokedex'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cadastropokemon',
            name='imagem_pokemon',
        ),
        migrations.RemoveField(
            model_name='cadastropokemon',
            name='pixel_pokemon',
        ),
    ]
