import os, platform, random

if (platform.platform().startswith("macOS") or platform.platform().startswith("Linux")):
    os.system('clear')
else:
    os.system('cls')

""" * EJERCICIO:
 * ¡El último videojuego de Dragon Ball ya está aquí!
 * Se llama Dragon Ball: Sparking! ZERO.
 *
 * Simula un Torneo de Artes Marciales, al más puro estilo
 * de la saga, donde participarán diferentes luchadores, y el
 * sistema decidirá quién es el ganador.
 *
 * Luchadores:
 * - Nombre.
 * - Tres atributos: velocidad, ataque y defensa
 *   (con valores entre 0 a 100 que tú decidirás).
 * - Comienza cada batalla con 100 de salud.
 * Batalla:
 * - En cada batalla se enfrentan 2 luchadores.
 * - El luchador con más velocidad comienza atacando.
 * - El daño se calcula restando el daño de ataque del
 *   atacante menos la defensa del oponente.
 * - El oponente siempre tiene un 20% de posibilidad de
 *   esquivar el ataque.
 * - Si la defensa es mayor que el ataque, recibe un 10%
 *   del daño de ataque.
 * - Después de cada turno y ataque, el oponente pierde salud.
 * - La batalla finaliza cuando un luchador pierde toda su salud.
 * Torneo:
 * - Un torneo sólo es válido con un número de luchadores
 *   potencia de 2.
 * - El torneo debe crear parejas al azar en cada ronda.
 * - Los luchadores se enfrentan en rondas eliminatorias.
 * - El ganador avanza a la siguiente ronda hasta que sólo
 *   quede uno.
 * - Debes mostrar por consola todo lo que sucede en el torneo,
 *   así como el ganador."""

"õ"

class Character:
    def __init__(self, items) -> None:
        self.items = items
    def __getitem__(self, index):
        return self.items[index]

son_goku = Character(["Son Goku", 87, 69, 100])
vegeta = Character(["Vegeta", 78, 77, 100])
son_gohan = Character(["Son Gohan", 76, 59, 100])
trunks = Character(["Trunks", 77,61, 100])
freezer = Character(["Freezer", 73, 69, 100])
piccolo = Character(["Piccolo", 87, 55, 100])
krilin = Character(["Krilin", 49, 78, 100])
bulma = Character(["Bulma", 66, 56, 100])
cell = Character(["Cell", 59, 80, 100])
broly = Character(["Broly", 70, 52, 100])
kame_sennin = Character(["Kame Sennin", 83, 48, 100])
ten_shin_han = Character(["Ten Shin Han", 67, 59, 100])
raditz = Character(["Raditz", 59, 77, 100])
beerus = Character(["Beerus", 63, 80, 100])
kaio = Character(["Kaiõ", 71, 52, 100])
mr_satan = Character(["Mr. Satán", 80, 51, 100])
zamasu = Character(["Zamasu", 69, 71, 100])
yamcha = Character(["Yamcha", 72, 59, 100])
majin_boo = Character(["Majin Boo", 70, 49, 100])
vegetto = Character(["Vegetto", 82, 54, 100])#20
androide_n_17 = Character(["Androide nº17", 58, 84, 100])
gotenks = Character(["Gotenks", 81, 52, 100])
bardock = Character(["Bardock", 76, 59, 100])
whis = Character(["Whis", 52, 73, 100])
chi_chi = Character(["Chi-Chi", 56, 86, 100])
shenlong = Character(["Shenlong", 58, 80, 100])
yamoshi = Character(["Yamoshi", 68, 50, 100])
videl = Character(["Videl", 81, 52, 100])
nappa = Character(["Nappa", 75, 51, 100])
bra = Character(["Bra", 81, 54, 100])
dabra = Character(["Dabra", 53, 87, 100])
jeice = Character(["Jeice", 80, 54, 100])

characters = [son_goku, vegeta, son_gohan, trunks, freezer, piccolo, krilin, bulma, cell, broly,
              kame_sennin, ten_shin_han, raditz, beerus, kaio, mr_satan, zamasu, yamcha, majin_boo,
              vegetto, androide_n_17, gotenks, bardock, whis, chi_chi, shenlong, yamoshi, videl, 
              nappa, bra, dabra, jeice]



def couples(characters:list)->list:
    tournament_list = []
    random.shuffle(characters)
    counter = 0
    for i in range (len(characters)//2):
        tournament_list.append([])
        tournament_list[i].append(characters[counter])
        tournament_list[i].append(characters[counter+1])
        counter += 2
    return tournament_list

def show_battles(tournament_list):
    print("Los emparejamientos serán los siguientes:")
    for battle in tournament_list:
        print(f"{battle[0][0]} VS {battle[1][0]}") 

def fight(fighter1:object, fighter2:object):
    print(f"Batalla entre {fighter1[0]} y {fighter2[0]}")
    if fighter1[1] >= fighter2[1]:
        print(f"Ataca primero {fighter1[0]}")
    else:
        print(f"Ataca primero {fighter2[0]}")
    


#show_battles(couples(characters))

#if random.random()>0.2: con esta sentencia hay un 80% de posibilidades de true

