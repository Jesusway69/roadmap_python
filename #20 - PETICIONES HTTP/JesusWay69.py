import requests, os
os.system('cls')

""" * EJERCICIO:
 * Utilizando un mecanismo de peticiones HTTP de tu lenguaje, realiza
 * una petición a la web que tú quieras, verifica que dicha petición
 * fue exitosa y muestra por consola el contenido de la web.
 *
"""


# try:
#     response = requests.get('https://moure.dev', timeout=1.00)
#     print(response.text)
# except requests.exceptions.RequestException:
#     print("No se ha podido obtener la información")
# except ConnectionError:
#     print("Error de conexión")
# except TimeoutError:
#     print("Seha agotado el tiempo de espera")



""" * DIFICULTAD EXTRA (opcional):
 * Utilizando la PokéAPI (https://pokeapi.co), crea un programa por
 * terminal al que le puedas solicitar información de un Pokémon concreto
 * utilizando su nombre o número.
 * - Muestra el nombre, id, peso, altura y tipo(s) del Pokémon
 * - Muestra el nombre de su cadena de evoluciones
 * - Muestra los juegos en los que aparece
 * - Controla posibles errores"""


url_pokemon = "https://pokeapi.co/api/v2/pokemon?limit=151"

# response = requests.get(url_pokemon)

# for index, pokemon in enumerate(response.json()["results"]):
#     pokemon_name = pokemon["name"]
#     print(f"#{index + 1} {pokemon_name}")

def find ():
    pokemon_name = input("Escriba el nombre o número del pokemon a buscar: ")
    pokedata = get_data('https://pokeapi.co/api/v2/pokemon/' + pokemon_name)
    pokevolve = get_data('https://pokeapi.co/api/v2/evolution-chain/' + pokemon_name)

    pokemon_types = [types['type']['name'] for types in pokedata['types']]
    pokemon_games = [game_indices['version']['name'] for game_indices in pokedata['game_indices']]
    
    pokemon_chain = pokevolve['chain']
    pokemon_evolution = [chain['species']['name'] for chain in pokemon_chain['evolves_to']]
    print('Nombre: ',pokedata['name'].capitalize())
    print('ID:     ',pokedata['id'])
    print('Peso:   ',pokedata['weight'])
    print('Altura: ',pokedata['height'])
    print('Tipos:  ',', '.join(pokemon_types).title())
    print('Juegos: ',', '.join(pokemon_games).title())
    print(pokemon_evolution)

def get_data(url=''):
    pokemon_data = {
     'name': '',
     'id':'',
     'weight':'',
     'height':'',
     'types':'',
     'game_indices':'',
     
    }
    pokemon_evo = {
        'evolves_to':''
    }
    response = requests.get(url)
    data = response.json()
    pokemon_data['name'] = data['name']
    pokemon_data['id'] = data['id']
    pokemon_data['weight'] = data['weight']
    pokemon_data['height'] = data['height']
    pokemon_data['types'] = data['types']
    pokemon_data['game_indices'] = data['game_indices']
    pokemon_evo['chain'] = data['chain']

    return pokemon_data
find()