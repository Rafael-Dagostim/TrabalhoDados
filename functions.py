from math import ceil
import os
from logging import exception


def cls():
    """
    Limpa a tela.
    Feito por Rafael Dagostim.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def print_pretty_pokemon(pokemon):
    """
    Deixa o nome dos pokemons bonitos.
    Criado por Rafael Dagostim.
    """
    print('id: %s\tnome: %s\t\ttipo: %s' %
          (pokemon['id'], pokemon['name'], ' '.join(pokemon['type'])))

def sort_pokemon_by_name_asc(pokemon_list):
    """
    Retorna a lista de pokemons em ordem alfabetica, utilizando o algoritimo de ordenação por troca.
    Feito por Rafael Dagostim.
    """
    for k in range(0, len(pokemon_list)):
        for i in range(0, len(pokemon_list) - 1):
            if(pokemon_list[i]['name'] > pokemon_list[i + 1]['name']):
                pokemon_list[i], pokemon_list[i +
                                              1] = [pokemon_list[i + 1], pokemon_list[i]]

    return pokemon_list

def find_pokemon_by_name(pokemon_list, name):
    """
    Busca o pokemons pelo name, utilizando o algoritimo de busca linear
    Feito por Rafael Dagostim.
    """
    for pokemon in pokemon_list:
        if pokemon['name'] == name:
            return pokemon

    raise exception('Não encontrado ou fora dos limites')

def count_pokemons_by_letter(letter, pokemon_list):
    """
    Retorna quantos pokemons tem com a letra informada utilizando while.
    Feito por Yuri Boppre.
    """
    counter = 0
    i = 0
    while i < len(pokemon_list):
        if(pokemon_list[i]['name'][0] == letter.upper()):
            counter += 1
        i += 1

    return counter

def find_max(param_list):
    z = param_list[0]['id']
    index = 0
    """
    Acha  o maior número dentro da lista.
    Feito por Yuri Boppre.
    """
    for i in range(len(param_list)):
        if i > 0:
            if z < param_list[i]['id']:
                z = param_list[i]['id']
                index = i

    return z, index

def sort_pokemon_by_id_asc(pokemon_list):
    """
        Retorna a lista de pokemons em ordem ascendente.
        Feito por Yuri Boppre.
    """
    pokemon_list_copy = pokemon_list.copy()
    i = 1
    while len(pokemon_list_copy) > 0:
        max, index = find_max(pokemon_list_copy)
        pokemon_list[-i] = pokemon_list_copy[index]
        pokemon_list_copy.pop(index)
        i += 1

    return pokemon_list

def get_all_pokemons_names(pokemon_list):
    """
    Retorna o nome de cada Pokémon dentro da base de dados.
    Feito por Yuri Machado.
    """
    return [pokemon['name'] for pokemon in pokemon_list]

def binary_search_by_pokemon_id(pokemon_list, id):
    """
    Retorna o objeto de um Pokémon pesquisando com parâmetro o seu id.
    Feito por Yuri Machado.
    """
    new_pokemon_list = sort_pokemon_by_id_asc(pokemon_list)
    # Posição inicializada com -1, pois não existe nenhum pokemon com o id procurado até então.
    position_found = -1
    high_low = -1  # -1 Início, 0 Menor, 1 Maior
    i = 1
    add_odd = 0  # 0 Não andou, 1 Andou
    size_divider = 0
   
    while position_found == -1:

        if (size_divider == 1 and add_odd == 1):
            return 'Não encontrado'

        size_divider = round(len(new_pokemon_list)/(2**i))

        if len(new_pokemon_list)/(2**i) < 1:
            size_divider = 1
            add_odd = 1

        if high_low == -1:
            size = size_divider
        elif high_low == 0:
            size = size - size_divider
        else:
            size = size + size_divider

        if new_pokemon_list[size]['id'] == id:
            position_found = size
        elif new_pokemon_list[size]['id'] > id:
            high_low = 0
        else:
            high_low = 1

        i += 1

    return new_pokemon_list[position_found]

def get_pokemon_by_type(type_pokemon, pokemon_list):
    """
    Retorna todos os pokemons de um determinado tipo.
    Feito por Yuri Damin.
    """
    
    pokemon_by_type = []
    for pokemon in pokemon_list:
        if type_pokemon in pokemon['type']:
            pokemon_by_type.append(pokemon)

    return pokemon_by_type

def get_pokemon_by_name_size(size, pokemon_list):
    """
    Retorna o tamanho de um determinado nome de pokemon.
    Feito por Yuri Damin.
    """
    pokemon_by_name_size = []
    for pokemon in pokemon_list:
        if size == len(pokemon['name']):
            pokemon_by_name_size.append(pokemon)
    
    return pokemon_by_name_size

