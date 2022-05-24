import json
from math import ceil
from posixpath import split
import functions

poke_json = open('./pokemon.data.json')

pokemon_data = json.load(poke_json)


def see_pokemon_menu():
    """
    Menu de opções para filtro de pokemon.
    Feito por Rafael Dagostim.
    """
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
    """
    Menu de busca dos pokemons.
    Feito por Rafael Dagostim.
    """
    value = 1
    while value != 0:
        functions.cls()
        print('1 - Buscar Pokemon por Id')
        print('2 - Buscar Pokemon por Nome')
        print('3 - Buscar Pokemons por tipo')
        print('4 - Buscar Pokemons por tamanho do nome')
        print('0 - Voltar')
        value = int(input('Escolha uma opção: '))
        if value == 1:
            pokemon_id = int(input('Digite o ID do pokemon: '))
            try: functions.print_pretty_pokemon(functions.binary_search_by_pokemon_id(pokemon_data, pokemon_id))
            except Exception as e:print(e)
        if value == 2:
            pokemon_name = input('Digite o nome do pokemon: ')
            try: functions.print_pretty_pokemon(functions.find_pokemon_by_name(pokemon_data, pokemon_name))
            except Exception as e:print(e)
        if value == 3:
            pokemon_type = input('Digite o tipo do pokemon: ')
            for pokemon in functions.get_pokemon_by_type(pokemon_type, pokemon_data):
                functions.print_pretty_pokemon(pokemon)
        if value == 4:
            pokemon_name_size = int(input('Digite o tamanho do nome do pokemon: '))
            for pokemon in functions.get_pokemon_by_name_size(pokemon_name_size, pokemon_data):
                functions.print_pretty_pokemon(pokemon)
        value = int(input('\n 1 - Pesquisar outro pokemon\n 0 - Voltar\n>> '))

def add_pokemon():
    value = 1
    while value != 0:
        functions.cls()
        name = input('Informe um nome: ')
        type = input('Informe o tipo (separado por virgula): ')
        pokemon_data.append({'id': len(pokemon_data) +1, 'name': name, 'type': type.split(',')})
        json.dump(pokemon_data, open('./pokemon.data.json', 'w', encoding='utf-8'))
        functions.cls()
        print('Pokemon adicionado!\n')
        functions.print_pretty_pokemon(pokemon_data[-1])
        value = int(input('\n1 - Inserir novo pokemon\n0 - Sair\n>>'))

def main_menu():
    """
    Função menu recursiva, fecha apenas quando digitado zero 0.
    Criado por Rafael Dagostim.
    """
    value = 1
    functions.cls()
    print('POKEDATA')
    print('________')
    print('1 - Ver Pokemons')
    print('2 - Buscar Pokemons')
    print('3 - Adicionar Pokemon')
    print('0 - Sair')
    try: value = int(input('Escolha uma opção: '))
    except: main_menu()
    if value == 1:
        see_pokemon_menu()
    if value == 2:
        find_pokemon_menu()
    if value == 3:
        add_pokemon()
    if value == 0:
        return
    else: main_menu()

main_menu()


