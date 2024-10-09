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

streamers_list = ["Abby", "Ache", "AdriContreras4", "agustin51", "alexby11", "ampeterby7" , "AriGameplays", "Arigeli_",
                 "auronplay","axozer", "beniju03", "bycalitos", "byViruZz" ,"Carreraaa" , "celopan", "crystalmolly",
                 "darioemehache","dheylo", "djmariio", "doble", "elvisayomastercard", "elxokas", "elyas360" , "FolagorLives", 
                 "guanyar", "hika","hiperop", "ibai", "ibelky_", "IlloJuan" ,"imantado" , "irinaisasia", "jesskiu",
                 "jopa","jordiwild", "kenaisouza", "keroro", "TheKiddKeo95" ,"kikorivera" , "knekro", "kokorok", "kronnozomber",
                 "leviathan", "littleragergirl", "lola_lolita", "lolito" ,"lolkilla" , "luzu", "mangel", "mayichi",
                 "meelo", "MissaSinfonia", "mixwell", "mrjagger" ,"NateGentile7" , "nexxuz", "nissaxter", "NoSoyPlex", "OllieGamerz",
                 "orslok", "outconsumer", "papigavi", "paracetamor" ,"patica" , "paulagonu", "pausenpaii", "perxitaa",
                 "polispol1", "quackity", "recuerdop" ,"reven" , "rivers_gg", "robertpg", "roier",
                 "rojuu", "Rubius", "shadoune", "silithur" ,"ElSpreen" , "Spursito", "srcheeto", "staxx",
                 "suzyrox", "TheGrefg", "tvandeR", "Vicens" ,"vitu" , "werlyb", "Xavi", "xcrystal",
                  "zarcort", "Zeling", "ZormanWorld"]
dev_streamers_list = ["afor_digital", "altaskur", "AppleCoding", "CarlosAzaustre", "CarlosGameDeveloper",
                     "CursosDeDesarrollo", "dimaspython", "ElPinguinoDeMario","Guinxu", 
                     "ManzDev", "MelenitasDev", "midudev", "MoureDev", "programacion_es",
                     "r2d2_Coder", "RafaLagoon", "RothioTome", "todocode", "vamoacodear"]


client_id = credentials.client_id_v3
secret_id = credentials.secret_id_v3

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
    
    return result.get("access_token")

async def get_user_data(channel:str):
    client = await Twitch(client_id,secret_id)
    user = await first(client.get_users(logins=channel))
    if user == None:
        return None, None, None
    return user.id, user.display_name, user.created_at


def get_followers(id, token, client_id):
    url = f'https://api.twitch.tv/helix/channels/followers'
    response = requests.get(url, headers = {
        'Client-ID': client_id,
        'Authorization': f'Bearer {token}'
    }, params={"broadcaster_id":id})

    if response.status_code == 200:
        return response.json().get('total')
        
    else:
        return f"Error data: {response.json()}"
    
token = get_token(client_id, secret_id) 
for index, streamer in enumerate(dev_streamers_list):
    id, name, since = asyncio.run(get_user_data(streamer))
    followers = get_followers(id, token, client_id)
    if id == None or name == None or since == None:
        print(f"{index}- Usuario {streamer} no encontrado")
        continue
    print(f"{index+1}- {name}, Antiguedad: {since.day}/{since.month}/{since.year}, followers: {followers}")










