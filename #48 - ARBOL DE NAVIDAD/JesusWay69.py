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
    for branch in range(hight):
        tree.append([])
        for i in range(base):
            if i == base // 2:
                tree[branch].append('*')
            if i == base // 2 - branch:
                tree[branch].append('*')
            else:
                tree[branch].append(' ')
    print(tree)
    return tree, hight

def show_tree(tree:list, hight:int):
    for index, branch in enumerate(tree):
        if index == hight:
            print()
        else:
            print(branch)
tree, hight = create_tree(5)
show_tree(tree, hight)