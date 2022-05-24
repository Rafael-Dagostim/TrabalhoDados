import os
from logging import exception

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def print_pretty_pokemon(pokemon):
  """
  Deixa o nome dos pokemons bonitos.
  Criado por Rafael Dagostim.
  """
  print('id: %s\tnome: %s\t\ttipo: %s' %(pokemon['id'], pokemon['name'], ' '.join(pokemon['type'])))

def sort_pokemon_by_name_asc(pokemon_list):
    """
    Retorna a lista de pokemons em ordem alfabetica, utilizando o algoritimo de ordenação por troca.
    Feito por Rafael Dagostim.
    """
    for k in range(0, len(pokemon_list)):
        for i in range(0, len(pokemon_list) - 1):
            if(pokemon_list[i]['name'] > pokemon_list[i + 1]['name']):
                pokemon_list[i], pokemon_list[i + 1]  = [pokemon_list[i + 1], pokemon_list[i]]

    return pokemon_list

def find_pokemon_by_id(pokemon_list, id):
    """
    Busca o pokemons pelo id, utilizando o algoritimo de busca linear 
    Feito por Rafael Dagostim.
    """
    for pokemon in pokemon_list:
        if pokemon['id'] == id: return pokemon 
            
    raise exception('Pokemon não encontrado')
