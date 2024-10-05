import os, platform, credentials,asyncio, requests
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


client_id = credentials.client_id
secret_id = credentials.secret_id

def get_token(client_id, client_secret):
    url = 'https://id.twitch.tv/oauth2/token'
    
    data = {
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': 'client_credentials'
    }

    response = requests.post(url, data=data)

    if response.status_code != 200:
        raise Exception('Error al obtener el token OAuth')

    result = response.json()
    return result['access_token']

token = get_token(client_id, secret_id)
print (token)
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
                 "xokas", "zarcort", "zeling", "zorman"]



async def get_id(channel:str):
    client = await Twitch(client_id,secret_id)
    user = await first(client.get_users(logins=channel))
    return user.id
id = asyncio.run(get_id(streamers_list[1]))

print(id)



url = f'https://api.twitch.tv/helix/users/follows?broadcaster_id={id}'

response = requests.get(url, headers=client)

data = response.json()
print(data)

#follower_count = data['total']


#print(f'Follower count: {follower_count}')



