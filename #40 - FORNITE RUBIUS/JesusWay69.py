import os, platform, credentials, asyncio, requests
from twitch import TwitchClient
from twitchAPI.twitch import Twitch
from twitchAPI.helper import first

if (platform.platform().startswith("macOS") or platform.platform().startswith("Linux")):
    os.system('clear')
else:
    os.system('cls')

""" * EJERCICIO:
 * ¡Rubius tiene su propia skin en Fortnite!
 * Y va a organizar una competición para celebrarlo.
 * Esta es la lista de participantes:
 * https://x.com/Rubiu5/status/1840161450154692876
 *
 * Desarrolla un programa que obtenga el número de seguidores en
 * Twitch de cada participante, la fecha de creación de la cuenta 
 * y ordene los resultados en dos listados.
 * - Usa el API de Twitch: https://dev.twitch.tv/docs/api/reference
 *   (NO subas las credenciales de autenticación)
 * - Crea un ranking por número de seguidores y por antigüedad.
 * - Si algún participante no tiene usuario en Twitch, debe reflejarlo."""

streamers_list = ["AdriContreras4", "ache", "agustin51", "alexby11" ,"ampeterby7" , "arigameplays", "arigeli_",
                 "auronplay","axozer", "beniju03", "bycalitos", "byviruzz" ,"carreraaa" , "celopan", "crystalmolly",
                 "darioemehache","dheylo", "djmariio", "doble", "elvisayomastercard" ,"elyas360" , "folagorlives", 
                 "guanyar", "hika","hiperop", "ibai", "ibelky_", "illojuan" ,"imantado" , "irinaisasia", "jesskiu",
                 "jopa","jordiwild", "kenaisouza", "keroro", "kiddkeo" ,"kikorivera" , "knekro", "kokorok", "kronnozomber",
                 "leviathan", "littleragergirl", "lola_lolita", "lolito" ,"lolkilla" , "luzu", "mangel", "mayichi",
                 "meelo", "missasofia", "mixwell", "mrjagger" ,"nategentile" , "nexxuz", "nissaxter", "ollie",
                 "orslok", "outconsumer", "papigavi", "paracetamor" ,"patica" , "paulagonu", "pausenpaii", "perxita",
                 "plex", "polispol", "quackity", "recuerdop" ,"reven" , "rivers", "robertpg", "roier",
                 "rojuu", "rubius", "shadoune", "silithur" ,"spreen" , "spursito", "srcheeto", "staxx",
                 "suzyrox", "thegrefg", "tvandeR", "vicens" ,"vituber" , "werlyb", "xavi", "xcrystal",
                 "elxokas", "zarcort", "zeling", "zorman"]


client_id = credentials.client_id_v2
secret_id = credentials.secret_id_v2

def get_token(client_id, client_secret):
    url = 'https://id.twitch.tv/oauth2/token'

    response = requests.post(url, data = {
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': 'client_credentials'
    })

    if response.status_code != 200:
        return f"Error token: {response.status_code}"
        
    result = response.json()
    if result['token_type'] != "bearer":
        raise Exception("Unexpected token type")
    return f"Token:{result["access_token"]}, Expira en:{result["expires_in"]}segundos, tipo:{result['token_type']}"


token = get_token(client_id, secret_id)
print (token)

async def get_id(channel:str):
    client = await Twitch(client_id,secret_id)
    user = await first(client.get_users(logins=channel))
    return user.id
id = asyncio.run(get_id(streamers_list[88]))
print(id) 


def get_followers(id, token):
    url = f'https://api.twitch.tv/helix/users/follows?to_id={id}'
    response = requests.get(url, headers = {
        'Client-ID': client_id,
        'Authorization': f'Bearer {token}'
    })

    if response.status_code == 200:
        return response.json()['total']
        
    else:
        return f"Error data: {response.json()}"

print(get_followers(id, token))



# response = requests.get(url, headers=client)

# data = response.json()
# print(data)

#follower_count = data['total']


#print(f'Follower count: {follower_count}')



