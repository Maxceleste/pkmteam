import pokepy

class PokemonAPI :
    client = pokepy.V2Client()

    poke_status = {
        'hp' : 0,
        'ataque' : 1,
        'defesa' : 2,
        'ataque_especial' : 3,
        'defesa_especial' : 4,
        'velocidade' : 5
    }

    def get_status(self, status : str, pokedex):
        """
        Função que retorna algum status do pokémon, com fonte da API.

        Essa função leva dois argumentos, o primeiro é o nome do status que você quer obter em forma de string,
        de acordo com os models, e o segundo argumento é o número da pokedex do pokémon que você deseja obter
        o status. 
        """
        pokemon = self.client.get_pokemon(pokedex)[0].stats[self.poke_status[status]].base_stat
        return pokemon
    


