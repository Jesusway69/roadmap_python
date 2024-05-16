import requests

response = requests.get('https://pokeapi.co/api/v2/evolution-chain/200/')
data = response.json()['chain'] #diccionario

evolve = data['evolves_to'] #lista de 1 elemento


if (len(evolve)<1):
     pass #break o return
else: 
    for i in range (len(evolve)):
        print(evolve[i]['species']['name'])



if (len(evolve[0]['evolves_to']))<1:
        pass
else:
        
    for j in range (len(evolve[0]['evolves_to'])):
        print(evolve[0]['evolves_to'][j]['species']['name'])




        #print(evolve[0]['evolves_to'][0]['species']['name'])


#url_pokemon = "https://pokeapi.co/api/v2/pokemon?limit=151"

# response = requests.get(url_pokemon)

# for index, pokemon in enumerate(response.json()["results"]):
#     pokemon_name = pokemon["name"]
#     print(f"#{index + 1} {pokemon_name}")

#https://jsonviewer.stack.hu/