
def sort_pokemon_by_name_asc(pokemon_list):
    """
    Retorna a lista de pokemos em ordem alfabetica.
    Feito por Rafael Dagostim
    """
    for i in range(0, len(pokemon_list)):
        for index in range(0, len(pokemon_list) - 1):
            if(pokemon_list[index]['name'] > pokemon_list[index+1]['name']):
                res = pokemon_list[index]
                pokemon_list[index] = pokemon_list[index+1]
                pokemon_list[index+1] = res

    return pokemon_list

def find_pokemon_by_name(pokemon_list, name, sorted):
    """
    Busca o id do pokemon pelo nome.
    Feito por Rafael Dagostim
    """
    pokemon_list = pokemon_list if sorted == True else sort_pokemon_by_name_asc(pokemon_list)
    index = len(pokemon_list) % 2
    if name == pokemon_list(index): return # TODO continuar



print(sort_pokemon_by_name_asc([
    {'id': 1, 'name': 'Bulbasaur'},
    {'id': 2, 'name': 'Ivysaur'},
    {'id': 3, 'name': 'Venusaur'},
    {'id': 4, 'name': 'Charmander'},
    {'id': 5, 'name': 'Charmeleon'},
    {'id': 6, 'name': 'Charizard'},
    {'id': 7, 'name': 'Squirtle'},
]))
