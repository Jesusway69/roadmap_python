import requests

response = requests.get('https://pokeapi.co/api/v2/evolution-chain/1/')
if response.status_code == 200:
    new_url = response.json()["evolution_chain"]["url"]

    new_response = requests.get(new_url)

 
    if new_response.status_code == 200:
        data = new_response.json()

        def get_evolves(data):
                        print(data["species"]["name"])
                        if "evolves_to" in data:
                            for evolve in data["evolves_to"]:
                                get_evolves(evolve)

        get_evolves(data["chain"])


    else:
        print(f"Error {response.status_code} obteniendo las evoluciones.")
else:
    print(f"Error {response.status_code} obteniendo las evoluciones.")















# if (len(evolve)<1):
#      pass #break o return
# else: 
#     for i in range (len(evolve)):
#         print(evolve[i]['species']['name'])



# if (len(evolve[0]['evolves_to']))<1:
#         pass
# else:
        
#     for j in range (len(evolve[0]['evolves_to'])):
#         print(evolve[0]['evolves_to'][j]['species']['name'])




 