import os, platform

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
    for row in tree:
        for column in row:
            print(column, end='')
        print()

show_tree(create_tree(10))



 