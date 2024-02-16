import os
os.system('cls')
from collections import deque

"""
 * EJERCICIO:
 * Implementa los mecanismos de introducción y recuperación de elementos propios de las
 * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
 * o lista (dependiendo de las posibilidades de tu lenguaje).
 *
 * DIFICULTAD EXTRA (opcional):
 * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
 *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
 *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.
"""



def pila (my_list):
 for i in range (1,11):
    my_list.append(i)

 print(my_list)

 my_list.pop()

 print(my_list)



def cola (my_list):
  for i in range (1,11):
    my_list.insert(0,i)
  print(my_list)
  my_list.pop(0)
  print(my_list)

def cola2 (my_list):
  my_list = deque(my_list)
  for i in range (1,11):
    my_list.append(i)
  print(my_list)
  my_list.popleft
  print(my_list)
  
  


my_list = []
pila(my_list)
my_list = []
cola(my_list)
my_list = []
cola2(my_list)