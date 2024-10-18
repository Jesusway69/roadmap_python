import os, platform, spotipy, credentials, JesusWay69
from spotipy.oauth2 import SpotifyClientCredentials



if (platform.platform().startswith("macOS") or platform.platform().startswith("Linux")):
    os.system('clear')
else:
    os.system('cls')

client_ID = credentials.client_ID #clave de cliente propia de 32 bits
secret_ID = credentials.secret_ID #clave secreta propia de 32 bits

ccm = SpotifyClientCredentials(client_id=client_ID, client_secret=secret_ID)
sp = spotipy.Spotify(client_credentials_manager=ccm)


band1 = input("Escriba el nombre del primer artista a comparar: ")
band2 = input("Escriba el nombre del segundo artista a comparar: ")

band1 = JesusWay69.get_artist(band1)
band2 = JesusWay69.get_artist(band2)

JesusWay69.compare(band1, band2)