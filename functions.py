
def sort_pokemon_by_name_asc(pokemon_list):
    """
    Retorna a lista de pokemos em ordem alfabetica.
    Feito por Rafael Dagostim
    """
    for index in range(0, len(pokemon_list) - 1):
        if(pokemon_list[index]['name'] > pokemon_list[index+1]['name']):
            res = pokemon_list[index]
            pokemon_list[index] = pokemon_list[index+1]
            pokemon_list[index+1] = res

    return pokemon_list

print(sort_pokemon_by_name_asc([
    {'id': 1, 'name': 'Bulbasaur'},
    {'id': 2, 'name': 'Ivysaur'},
    {'id': 3, 'name': 'Venusaur'},
    {'id': 4, 'name': 'Charmander'},
    {'id': 5, 'name': 'Charmeleon'},
    {'id': 6, 'name': 'Charizard'},
    {'id': 7, 'name': 'Squirtle'},
]))
