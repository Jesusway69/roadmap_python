import requests, os
os.system('cls')

""" * EJERCICIO:
 * Utilizando un mecanismo de peticiones HTTP de tu lenguaje, realiza
 * una petición a la web que tú quieras, verifica que dicha petición
 * fue exitosa y muestra por consola el contenido de la web.
 *
"""

try:
    response = requests.get('https://moure.dev', timeout=1.00) 
    print(response.text)
except requests.exceptions.RequestException:
    print("No se ha podido obtener la información")
except ConnectionError:
    print("Error de conexión")
except TimeoutError:
    print("Seha agotado el tiempo de espera")

""" * DIFICULTAD EXTRA (opcional):
 * Utilizando la PokéAPI (https://pokeapi.co), crea un programa por
 * terminal al que le puedas solicitar información de un Pokémon concreto
 * utilizando su nombre o número.
 * - Muestra el nombre, id, peso, altura y tipo(s) del Pokémon
 * - Muestra el nombre de su cadena de evoluciones
 * - Muestra los juegos en los que aparece
 * - Controla posibles errores"""

def find():
    pokemon_name = input("Escriba el nombre o número del pokemon a buscar: ")
    try:
        pokedata = get_data('https://pokeapi.co/api/v2/pokemon/'+ pokemon_name)
    except requests.RequestException as ex:
        print ("URL NO ENCONTRADA:  ",ex)
    except Exception as name:
        print("No se ha introducido ningún parámetro",name)
    else:
        pokemon_types = [types['type']['name'] for types in pokedata['types']]
        pokemon_games = [game_indices['version']['name'] for game_indices in pokedata['game_indices']]
        
        print('Nombre: ',pokedata['name'].capitalize())
        print('ID:     ',pokedata['id'])
        print('Peso:   ',pokedata['weight'])
        print('Altura: ',pokedata['height'])
        print('Tipo/s:  ',', '.join(pokemon_types).title())
        print('Juegos: ',', '.join(pokemon_games).title())
        get_evolve('https://pokeapi.co/api/v2/evolution-chain/'+ str(pokedata['id']))

def get_data(url=''):
    pokemon_data = {
    'name': '',
    'id':'',
    'weight':'',
    'height':'',
    'types':'',
    'game_indices':'' 
    }
  
    response = requests.get(url)
    data = response.json()
    
    pokemon_data['name'] = data['name']
    pokemon_data['id'] = data['id']
    pokemon_data['weight'] = data['weight']
    pokemon_data['height'] = data['height']
    pokemon_data['types'] = data['types']
    pokemon_data['game_indices'] = data['game_indices']
    return pokemon_data

def get_evolve(url):

    response = requests.get(url)

    data = response.json()['chain'] #diccionario

    evolve = data['evolves_to'] #lista de 1 elemento

    if (len(evolve)<1):
        return
    else: 
        print("Evoluciones: ",end=' ')
        for i in range (len(evolve)):
            evo1 = evolve[i]['species']['name']
            print('\b',evo1.capitalize(), end=', ')

    if (len(evolve[0]['evolves_to']))<1:
        return
    else:
            
        for j in range (len(evolve[0]['evolves_to'])):
            evo2 = evolve[0]['evolves_to'][j]['species']['name']
            print('\b',evo2.capitalize(), end=' ')
print()
find()




