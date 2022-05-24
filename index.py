import os
from functions import sort_pokemon_by_name_asc, find_pokemon_by_id

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

title = ' ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄   ▄ ▄▄▄▄▄▄▄ ▄▄   ▄▄ ▄▄▄▄▄▄▄ ▄▄    ▄ \n█       █       █   █ █ █       █  █▄█  █       █  █  █ █\n█    ▄  █   ▄   █   █▄█ █    ▄▄▄█       █   ▄   █   █▄█ █\n█   █▄█ █  █ █  █      ▄█   █▄▄▄█       █  █ █  █       █\n█    ▄▄▄█  █▄█  █     █▄█    ▄▄▄█       █  █▄█  █  ▄    █\n█   █   █       █    ▄  █   █▄▄▄█ ██▄██ █       █ █ █   █\n█▄▄▄█   █▄▄▄▄▄▄▄█▄▄▄█ █▄█▄▄▄▄▄▄▄█▄█   █▄█▄▄▄▄▄▄▄█▄█  █▄▄█'

print(title)
print('_________________________________________________________')

async def see_pokemon_menu():
    pokemon_list = sort_pokemon_by_name_asc()
    

async def main_menu():
    print('1 - Ver Pokemons\n2 - Criar Time\n3 - Ver Times\n4 - Deletar Time\n5 - Sair')
    value = int(input('Escolha uma opção: '))
    if value == 1: await see_pokemon_menu()

main_menu()


