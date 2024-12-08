import os, platform, random

if (platform.platform().startswith("macOS") or platform.platform().startswith("Linux")):
    os.system('clear')
else:
    os.system('cls')


""" * EJERCICIO:
 * ¡Ha comenzado diciembre! Es hora de montar nuestro
 * árbol de Navidad...
 *
 * Desarrolla un programa que cree un árbol de Navidad
 * con una altura dinámica definida por el usuario por terminal.
 *
 * Ejemplo de árbol de altura 5 (el tronco siempre será igual):
 *
 *     *
 *    ***
 *   *****
 *  *******
 * *********
 *    |||
 *    |||
 *
 * El usuario podrá seleccionar las siguientes acciones:
 * 
 * - Añadir o eliminar la estrella en la copa del árbol (@)
 * - Añadir o eliminar bolas de dos en dos (o) aleatoriamente
 * - Añadir o eliminar luces de tres en tres (+) aleatoriamente
 * - Apagar (*) o encender (+) las luces (conservando su posición)
 * - Una luz y una bola no pueden estar en el mismo sitio
 *
 * Sólo puedes añadir una estrella, y tantas luces o bolas
 * como tengan cabida en el árbol. El programa debe notificar
 * cada una de las acciones (o por el contrario, cuando no
 * se pueda realizar alguna)."""

def create_tree(hight:int)->list:
    tree = []
    base = hight * 2 - 1
    branch = 1
    for i in range(hight):
        tree.append([])
        [tree[i].append(' ') for j in range(base // 2)]
        [tree[i].append('*') for k in range(branch)]
        [tree[i].append(' ') for l in range(base // 2)]
        base -= 2
        branch += 2
    for m in range (1, 3):
        tree.append([])
        [tree[i + m].append(' ') for n in range(hight - 2)]
        [tree[i + m].append('|') for o in range(3)]
        [tree[i + m].append(' ') for p in range(hight - 2)]

    return tree

def show_tree(tree:list):
    print()
    for row in tree:
        for column in row:
            print(column, end='')
        print()

def add_star(tree:list, switch:bool)->list:
    if switch:
        star = ['@' if x == '*' else x for x in tree[0]]
    else:
        star = ['*' if x == '@' else x for x in tree[0]]
    tree[0] = star
    return tree

def add_balls(tree:list):
    i=0
    while i !=2:
        branch = random.randint(1, len(tree)-3)
        ball = random.randint(0, len(tree[branch]))
        print("ronda:",i," rama:",branch," columna:", ball)
        if tree[branch][ball-1] != '*':
            continue
        else:
            tree[branch][ball-1] = 'o'
            i+=1
    return tree

def remove_balls(tree:list):
    for row in range(1, len(tree)-2):
        for column in range(len(tree[row])):
            if tree[row][column] == 'o':
                tree[row][column] = '*'
    return tree




# tree = create_tree(15)
# show_tree(tree)
# show_tree(add_star(tree, True))
# show_tree(add_balls(tree))
# show_tree(add_balls(tree))
# show_tree(remove_balls(tree))



while True:
    print("""
    
    1- Crear árbol
    2- Añadir 2 bolas aleatoriamente
    3- Quitar todas las bolas
    4- Añadir 3 luces aleatoriamente 
    5- Encender las luces
    6- Apagar las luces
          
    """)

    option = input("Selecciona una opción del 1 al 6: ") 

    match option:
        case "1":
            hight = input("Indroduzca la altura del árbol a crear: ")
            tree = create_tree(hight)
        case "2":
            add_balls(tree=None)
        case "3":
            remove_balls(tree=None)
        case "4":
            pass
        case "5":
            pass
        case "6":
            pass