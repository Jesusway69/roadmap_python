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
# row = 0
# column = 0
mickey_position = [0,0]

def printer(labyrinth):
    for v in labyrinth:
        print()
        for h in v:
            print(h, end='') 
    print()



def up(last_row, last_column, mickey_position):
    if last_row<0:
        print("No se puede subir")
        last_row+=1
        printer(labyrinth)
        
    else:
        labyrinth[row][column] = "⬜️"
        labyrinth[last_row][last_column] = "🐭"
        mickey_position = [last_row, last_column]
        printer(labyrinth)
    return mickey_position

def down(last_row, last_column, mickey_position):
    if last_row>5:
        print("No se puede bajar")
        last_row-=1
        printer(labyrinth)
        
    else:
        labyrinth[row][column] = "⬜️"
        labyrinth[last_row][last_column] = "🐭"
        mickey_position = [last_row, last_column]
        printer(labyrinth)
    return mickey_position

def left(last_row, last_column, mickey_position):
    if last_column<0:
        print("No se puede ir a la izquierda") 
        last_column+=1
        printer(labyrinth)
       
    else:
        labyrinth[row][column] = "⬜️"
        labyrinth[last_row][last_column] = "🐭"
        mickey_position = [last_row, last_column]
        printer(labyrinth)
    return mickey_position 
                
def right(last_row, last_column, mickey_position):
    if last_column>5:
        print("No se puede ir a la derecha")
        last_column -=1
        printer(labyrinth)
        
    else:
        labyrinth[row][column] = "⬜️"
        labyrinth[last_row][last_column] = "🐭"
        mickey_position = [last_row, last_column]
        printer(labyrinth)
    return mickey_position 

   
printer(labyrinth)
while True:
 
    movement = input("""\n\nElija un movimiento para guiar a Mickey por el laberinto:
              n - Subir
              s - Bajar
              w - Izquierda
              e - Derecha
                  
              """)
    row, column = mickey_position
    last_row, last_column = row, column
    

    if movement != "n" and movement != "s" and movement != "w" and movement != "e":
        print("comando no válido")
        continue
    elif labyrinth[row][column] == '⬛️':
        print("Por las zonas negras no puedes pasar, intenta de nuevo")
        continue
    elif labyrinth[row][column] == '🚪':
        print("¡¡Has encontrado la salida del laberinto!!")
        break
    else:

        if movement == "n":
            last_row = row -1
            mickey_position = up(last_row, last_column, mickey_position)
        elif movement == "s":
            last_row = row +1
            mickey_position = down(last_row, last_column, mickey_position)
        elif movement == "w":
            last_column = column -1
            mickey_position =left(last_row, last_column, mickey_position)
        elif movement == "e":
            last_column = column +1
            mickey_position =right(last_row, last_column, mickey_position)

    
    



