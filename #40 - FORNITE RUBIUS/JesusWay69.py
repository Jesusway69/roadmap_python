import os, platform, credentials
from twitch import TwitchClient
from twitchAPI.twitch import Twitch
from twitchAPI.helper import first
import asyncio
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

async def get_id(channel:str):
    client = await Twitch(credentials.client_id,credentials.secret_id)
    user = await first(client.get_users(logins=channel))
    return user.id






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

print(asyncio.run(get_id(streamers_list[0])))


