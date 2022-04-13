// javascrip para trocar os pokemons, esconder o cartão aberto e mostrar apenas o selecionado.

// para isso vamos trabalhar com dois elementos
// 1 - listagem
// 2 - cartão pokemon

// precisa criar duas variaveis no js para trabalhar com os elementos na tela.



const listaSelecaoPokemons = document.querySelectorAll('.pokemon')
const pokemonsCard = document.querySelectorAll('.cartao-pokemon')

listaSelecaoPokemons.forEach(pokemon => {
    // vamos precisar trabalhar com o evento de clique feito pelo usuario na listagem de pokémons


    pokemon.addEventListener('click', () => {
        // -remover classe aberto só do cartão aberto
        const cartaoPokemonAberto = document.querySelector('.aberto')
        cartaoPokemonAberto.classList.remove('aberto')

    // ao clicar em um pokémon da listagem pegamos o id desse pokémon para saber qual cartão mostrar

        const idPokemonSelecionado = pokemon.attributes.id.value

        const idDoCartaoPokemonParaAbrir = 'cartao-' + idPokemonSelecionado

        const cartaoPokemonParaAbrir = document.getElementById(idDoCartaoPokemonParaAbrir)
        cartaoPokemonParaAbrir.classList.add('aberto')

        // remover a classe ativo que marca o pokémon selecionado.
        const pokemonAtivoNaListagem = document.querySelector('.ativo')
        pokemonAtivoNaListagem.classList.remove('ativo')

        // adicionar a classe ativo no item da lista selecionado.
        const pokemonSelecionadoNaListagem = document.getElementById(idPokemonSelecionado)
        pokemonSelecionadoNaListagem.classList.add('ativo')

    })
})