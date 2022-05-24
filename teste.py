# import json
# from logging import exception

# poke_json = open('./pokemon.data.json')

# pokemon_data = json.load(poke_json)

# def achaPokemonPelaLetra(pokemon_list, letraParametro):
#   pokemonsEncontrados = [];
#   i = 1;
#   while i < len(pokemon_list):
#     if(pokemon_list['name'][0:1] == letraParametro):
#       pokemonsEncontrados.append(pokemon_list['name'])
#     i += 1

#     return pokemonsEncontrados

# letra = input('Informe a letra que deseja pesquisar: ');

# achaPokemonPelaLetra(letra);

title = '▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄   ▄ ▄▄▄▄▄▄▄ ▄▄   ▄▄ ▄▄▄▄▄▄▄ ▄▄    ▄ \n█       █       █   █ █ █       █  █▄█  █       █  █  █ █\n█    ▄  █   ▄   █   █▄█ █    ▄▄▄█       █   ▄   █   █▄█ █\n█   █▄█ █  █ █  █      ▄█   █▄▄▄█       █  █ █  █       █\n█    ▄▄▄█  █▄█  █     █▄█    ▄▄▄█       █  █▄█  █  ▄    █\n█   █   █       █    ▄  █   █▄▄▄█ ██▄██ █       █ █ █   █\n█▄▄▄█   █▄▄▄▄▄▄▄█▄▄▄█ █▄█▄▄▄▄▄▄▄█▄█   █▄█▄▄▄▄▄▄▄█▄█  █▄▄█'

print(title)