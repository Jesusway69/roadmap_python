
import os, platform, spotipy
from spotipy.oauth2 import SpotifyClientCredentials


if (platform.platform().startswith("macOS") or platform.platform().startswith("Linux")):
    os.system('clear')
else:
    os.system('cls')

"""* EJERCICIO:
 * Oasis y Linkin Park han anunciado nueva gira, pero, ¿quién es más popular?
 * ¡Dos de las bandas más grandes de la historia están de vuelta!
 * Desarrolla un programa que se conecte al API de Spotify y los compare.
 * Requisitos:
 * 1. Crea una cuenta de desarrollo en https://developer.spotify.com.
 * 2. Conéctate al API utilizando tu lenguaje de programación.
 * 3. Recupera datos de los endpoint que tú quieras.
 * Acciones:
 * 1. Accede a las estadísticas de las dos bandas.
 *    Por ejemplo: número total de seguidores, escuchas mensuales,
 *    canción con más reproducciones...
 * 2. Compara los resultados de, por lo menos, 3 endpoint.
 * 3. Muestra todos los resultados por consola para notificar al usuario.
 * 4. Desarrolla un criterio para seleccionar qué banda es más popular."""


client_ID = "********************************"
secret_ID = "********************************"


ccm = SpotifyClientCredentials(client_id=client_ID, client_secret=secret_ID)
sp = spotipy.Spotify(client_credentials_manager=ccm)


# artist = sp.search(q="queen", limit=1, type="artist")
# artist_ID = artist["artists"]["items"][0]["id"]
# artist_urn = "spotify:artist:" + artist_ID
# artist_name = artist["artists"]["items"][0]["name"]
# artist_followers = artist["artists"]["items"][0]["followers"]["total"]
# popularity_level = artist["artists"]["items"][0]["popularity"]

# print(artist_name, artist_followers, popularity_level)
# albums = sp.artist_albums(artist_ID, album_type="album",offset=0)
# print(sp.artist_top_tracks(artist_ID))
#[print(album["name"]) for album in albums["items"]]



def get_artist(artist_name:str)->str:
    artist = sp.search(q=artist_name, limit=1, type="artist")
    if artist == None:
        return f"El artista {artist_name} no existe"

    return artist

oasis = get_artist("oasis")
linkin_park = get_artist("Linkin park")


def get_artist_stats(artist):
    artist_followers = artist["artists"]["items"][0]["followers"]["total"]
    popularity_level = artist["artists"]["items"][0]["popularity"]
    return artist_followers, popularity_level

def print_top_songs(artist):
    top_songs = sp.artist_top_tracks(artist["artists"]["items"][0]["id"])
    #for song in top_songs["tracks"]:
    print(top_songs["tracks"][0]["name"], top_songs["tracks"][0]["popularity"])

def print_artist_stats(artist:str):
    print (f"""Nombre del artista: {artist["artists"]["items"][0]["name"]}
    Número de followers: {artist["artists"]["items"][0]["followers"]["total"]}
    Nivel de popularidad: {artist["artists"]["items"][0]["popularity"]}""")

print_artist_stats(oasis)
print_artist_stats(linkin_park)
print_top_songs(oasis)


def print_albums(artist):
    artist_id = artist["artists"]["items"][0]["id"]
    albums = sp.artist_albums(artist_id, album_type="album",offset=0)
    for album in albums["items"]:
        print(f"Album: {album["name"]}, Año de lanzamiento: {album["release_date"][:4]}")




def compare(artist1, artist2):
    followers1, popularity1 = get_artist_stats(artist1)
    followers2, popularity2 = get_artist_stats(artist2)

    print(f"{artist1} tiene {followers1} seguidores y su índice de popularidad es de {popularity1} puntos")
    print(f"{artist2} tiene {followers2} seguidores y su índice de popularidad es de {popularity2} puntos")

    print()
