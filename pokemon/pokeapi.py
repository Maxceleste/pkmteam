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

    def get_status(self, status : str, pokedex : int):
        """
        Função que retorna algum status do pokémon, com fonte da API.

        Essa função leva dois argumentos, o primeiro é o nome do status que você quer obter em forma de string,
        de acordo com os models, e o segundo argumento é o número da pokedex do pokémon que você deseja obter
        o status. 
        """
        pokemon = self.client.get_pokemon(pokedex)[0].stats[self.poke_status[status]].base_stat
        return pokemon
    
    def get_types(self, pokedex : int):
        """
        Função que retorna os tipos do pokémon, seja se for apenas um ou dois.

        A função pega como parâmetro o número da pokedex do pokémon e retorna os tipos do pokémon.
        É retornado uma tupla com os dois tipos, caso o pokémon tenha apenas um tipo, ele retorna 
        uma tupla com apenas um tipo.
        """
        type_1 = self.client.get_pokemon(pokedex)[0].types[0].type.name
        try:
            type_2 = self.client.get_pokemon(pokedex)[0].types[1].type.name
        except: 
            return (type_1,)
        
        return (type_1, type_2)

    def get_name(self, pokedex : int):
        """
        Função que retorna o nome do pokémon.

        Essa função leva como parâmetro o número da pokedex do pokémon e retorna
        o nome do mesmo.
        """
        name = self.client.get_pokemon(pokedex)[0].name
        return name



    


