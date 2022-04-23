# Pkm Team

Pkm Team é um site que exibe uma lista de pokémon adicionados no banco de dados pelos administradores do site. Quando é selecionado um pokémon, um card se abre com as informações do mesmo, exibindo seu nome, número da pokédex, seus tipos, status e habilidades. O administrador do site apenas precisa inserir no admin o número da pokédex e as habilidades. O resto é tudo obtido sozinho consumindo a API [Pokéapi](https://pokeapi.co/) de forma automática com o save do banco de dados customizado.

## Acessando o site

Pkm Team está disponível para seu acesso nesse link:
https://pkmteam.herokuapp.com/

O deploy foi feito por mim mesmo no heroku.

## Visual do site

![image](https://user-images.githubusercontent.com/89614438/164946019-6c8bbb7b-082b-410b-bdf8-4f6f5a96211d.png)


![image](https://user-images.githubusercontent.com/89614438/164946032-6bd4b884-77f8-4216-b045-5c226b31ab35.png)


![image](https://user-images.githubusercontent.com/89614438/164946081-87706659-5853-40c3-abe0-b08146bf6e91.png)

Esse design e todo o front-end foi feito pelo [Wesley](https://github.com/Zarps), que é responsivo, simples e bem bonito.
O site exibe os pokémon em ordem de número da pokedex, e o primeiro começa já com o card aberto. É um sistema simples que foi realizado com o Django.
Além disso, as cores dos cards variam dependendo do primeiro tipo do pokémon, tornando a aparência dos cards muito mais interessante.

## Banco de dados

![image](https://user-images.githubusercontent.com/89614438/164946380-d7be1674-0750-4af6-ac13-4085025fcded.png)

Acima, algumas colunas do banco de dados.

O banco de dados utilizado para trabalhar no projeto localmente foi o SQLite, mas em produção no heroku foi o PostgreSQL.
No banco, é guardado todas as informações de cada um dos pokémons, menos suas imagens, que são obtidas pelas imagens da API no próprio front-end.

## Metas para futuras atualizações

- Adicionar uma forma de cadastro e login
- Possibilitar o usuário cadastrado criar seus diferentes times pokémons
- Possibilitar uma forma de publicar seus diferentes times, com uma descrição sobre o mesmo para que outros possam ver.

# Autores:

### Front-end
Nome: Wesley Rios

LinkedIn : https://www.linkedin.com/in/wesleyrioos/

Github : https://github.com/Zarps

### Back-end

Nome: Max Paulo

LinkedIn: https://www.linkedin.com/in/max-paulo-sim%C3%A3o-teixeira-278a4a212/

Github : https://github.com/Maxceleste
  
  
  
  
