from os import system
from platform import platform
from JesusWay69 import get_artist, print_albums, print_top_songs

if (platform().startswith("macOS") or platform().startswith("Linux")):
    system('clear')
else:
    system('cls')

artist = input("Escriba el nombre del artista para ver sus albums y canciones más populares: ")
artist = get_artist(artist)
artist_name = artist["artists"]["items"][0]["name"]
print()
print(f'Esta es la discografía de {artist_name} ordenada de más antiguo a más reciente: ')
print_albums(artist)
print()
print(f'Estas son la canciones más famosas de {artist_name} ordenadas de mayor a menor popularidad: ')
print_top_songs(artist)






