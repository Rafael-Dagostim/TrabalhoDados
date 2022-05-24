import json
from math import ceil
import functions

poke_json = open('./pokemon.data.json')

pokemon_data = json.load(poke_json)


def see_pokemon_menu():
    functions.cls()
    order_by = int(input(
        '1 - Ordenar por nome\n2 - Ordenar por ID\n3 - Ver todos os nomes\nOutro - Voltar\nEscolha uma opção: '))
    if order_by == 1: pokemon_list = functions.sort_pokemon_by_name_asc(pokemon_data)
    elif order_by == 2: pokemon_list = functions.sort_pokemon_by_id_asc(pokemon_data)
    elif order_by == 3: pokemon_list = functions.get_all_pokemons_names(pokemon_data)
    else: 
        return
    total_pages = ceil(len(pokemon_list) / 10)
    page_index = 0
    value = 1
    while value != 0:
        functions.cls()
        for pokemon in pokemon_list[page_index * 10: (page_index + 1) * 10]:
            functions.print_pretty_pokemon(pokemon) if order_by != 3 else print(pokemon)
        print('\nPágina %s de %s' % (page_index + 1, total_pages))
        value = int(input('\n1 - Próxima página\n2 - Voltar\n0 - Sair\n>> '))
        if value == 1:
            page_index += 1
            if page_index >= total_pages - 1:
                page_index = 0
        elif value == 2:
            page_index -= 1
            if page_index < 0:
                page_index = total_pages - 1


def find_pokemon_menu():
    value = 1
    while value != 0:
        functions.cls()
        pokemon_id = int(input('Digite o ID do pokemon: '))
        try:
            functions.print_pretty_pokemon(functions.find_pokemon_by_id(pokemon_data, pokemon_id))
        except Exception as e:
            print(e)
        value = int(input('\n 1 - Pesquisar outro pokemon\n 0 - Voltar\n>> '))


def main_menu():
    value = 1
    while value != 0:
        functions.cls()
        print('POKEDATA')
        print('_________________________________________________________')
        print('1 - Ver Pokemons')
        print('2 - Buscar Pokemon')
        print('0 - Sair')
        value = int(input('Escolha uma opção: '))
        if value == 1:
            see_pokemon_menu()
        if value == 2:
            find_pokemon_menu()

main_menu()

