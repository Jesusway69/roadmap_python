import requests, os
os.system('cls')

""" * EJERCICIO:
 * Utilizando un mecanismo de peticiones HTTP de tu lenguaje, realiza
 * una petición a la web que tú quieras, verifica que dicha petición
 * fue exitosa y muestra por consola el contenido de la web.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la PokéAPI (https://pokeapi.co), crea un programa por
 * terminal al que le puedas solicitar información de un Pokémon concreto
 * utilizando su nombre o número.
 * - Muestra el nombre, id, peso, altura y tipo(s) del Pokémon
 * - Muestra el nombre de su cadena de evoluciones
 * - Muestra los juegos en los que aparece
 * - Controla posibles errores"""


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


url = "https://pokeapi.co/api/v2/pokemon?limit=151"

response = requests.get(url)

for index, pokemon in enumerate(response.json()["results"]):
    pokemon_name = pokemon["name"]
    print(f"#{index + 1} {pokemon_name}")