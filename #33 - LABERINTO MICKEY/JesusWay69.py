import os, platform

if (platform.platform().startswith("macOS") or platform.platform().startswith("Linux")):
    os.system('clear')
else:
    os.system('cls')

""" * EJERCICIO:
 * ¡Disney ha presentado un montón de novedades en su D23!
 * Pero... ¿Dónde está Mickey?
 * Mickey Mouse ha quedado atrapado en un laberinto mágico
 * creado por Maléfica.
 * Desarrolla un programa para ayudarlo a escapar.
 * Requisitos:
 * 1. El laberinto está formado por un cuadrado de 6x6 celdas.
 * 2. Los valores de las celdas serán:
 *    - ⬜️ Vacío
 *    - ⬛️ Obstáculo
 *    - 🐭 Mickey
 *    - 🚪 Salida
 * Acciones:
 * 1. Crea una matriz que represente el laberinto (no hace falta
 * que se genere de manera automática).
 * 2. Interactúa con el usuario por consola para preguntarle hacia
 * donde se tiene que desplazar (arriba, abajo, izquierda o derecha).
 * 3. Muestra la actualización del laberinto tras cada desplazamiento.
 * 4. Valida todos los movimientos, teniendo en cuenta los límites
 * del laberinto y los obtáculos. Notifica al usuario.
 * 5. Finaliza el programa cuando Mickey llegue a la salida."""


labyrinth =[["🐭","⬛️","⬛️","⬜️","⬜️","⬜️",],
            ["⬜️","⬜️","⬛️","⬜️","⬛️","⬜️",],
            ["⬛️","⬜️","⬛️","⬜️","⬜️","⬜️",],
            ["⬛️","⬜️","⬛️","⬜️","⬜️","⬛️",],
            ["⬜️","⬜️","⬛️","⬜️","⬜️","🚪",],
            ["⬜️","⬜️","⬜️","⬜️","⬛️","⬜️",],]
row = 0
column = 0
mickey_position = [0,0]

def movements(movement):

    def up(labyrinth):
            if mickey_position in labyrinth[0]:
                print("No se puede subir")
            else:
                labyrinth[row-1][column] = '🐭'
    printer(labyrinth)

    def down(labyrinth):
        if mickey_position in labyrinth[5]:
            print("No se puede bajar")
        else:
           labyrinth[row+1][column] = '🐭' 
    printer(labyrinth)

    def left(labyrinth):
        for rows in labyrinth:
            if '🐭' in rows:
                if rows.index('🐭') == 0: 
                   print("No se puede ir a la izquierda")
                   return
            else:
               labyrinth[row][column-1] = '🐭'
    printer(labyrinth) 
                    
    def right(labyrinth):
        for rows in labyrinth:
            if '🐭' in rows:
                if rows.index('🐭') == 5: 
                    print("No se puede ir a la derecha")
                    return
        else:
            labyrinth[row][column+1] = '🐭' 
    printer(labyrinth) 
    def printer(labyrinth):
        for v in labyrinth:
            print()
            for h in v:
                print(h, end='') 
    
    if movement == "n":
        return up
    elif movement == "s":
        return down
    elif movement == "w":
        return left
    elif movement == "e":
        return right
    else:
        printer(labyrinth)
   

while True:
    
    movements("")(labyrinth)
    
    movement = input("""Elija un movimiento para guiar a Mickey por el laberinto:
              n - Subir
              s - Bajar
              w - Izquierda
              e - Derecha
                  
              """).lower()
    row, column = mickey_position
    last_row, last_column = row, column
    
    if movement is not "n" or "s" or "w" or "e":
        print("comando no válido")

    elif labyrinth[row][column] == '⬛️':
        print("Por las zonas negras no puedes pasar, intenta de nuevo")
        continue
    elif labyrinth[row][column] == '🚪':
        print("¡¡Has encontrado la salida del laberinto!!")
        break
    else:
        labyrinth[last_row][last_column]
        movements(movement)(labyrinth)

    
    



