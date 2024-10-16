import os, platform

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
    def __init__(self, name, speed, shield, health) -> None:
        self.name = name
        self.speed = speed
        self.shield = shield
        self.health = health

son_Goku = Character("Son Goku", 83, 62, 100)
vegeta = Character("Vegeta", 78, 70, 100)
son_gohan = Character("Son Gohan", 77, 59, 100)
trunks = Character("Trunks", 77,61, 100)
freezer = Character("Freezer", 71, 69, 100)
piccolo = Character("Piccolo", 87, 55, 100)
krilin = Character("Krilin", 49, 78, 100)
bulma = Character("Bulma", 66, 56, 100)
cell = Character("Cell", 59, 80, 100)
broly = Character("Broly", 71, 52, 100)
kame_sennin = Character("Kame Sennin", 83, 48, 100)
ten_shin_han = Character("Ten Shin Han", 67, 59, 100)
raditz = Character("Raditz", 59, 77, 100)


#= Character("",,, 100)