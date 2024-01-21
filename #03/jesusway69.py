import os
os.system ('cls')

"""
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización
 *   y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
 *   y a continuación los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más
 *   de 11 dígitos (o el número de dígitos que quieras).
 * - También se debe proponer una operación de finalización del programa."""
#LISTA , ESTRUCTURA DE ELEMENTOS MUTABLES QUE PUEDEN SER DE VARIOS TIPOS
lista = [1, 2, 3.5, 7j, "Hola", "Python", True , None , [4,5,6], (1,"hola",False)]
[print(i , end =' ') for i in lista]
print('\n')


#TUPLA , ESTRUCTURA DE ELEMENTOS INMUTABLES QUE PUEDEN SER DE VARIOS TIPOS
tupla = (1, 2, 2 , 3.5, 7j, "Hola", "Python", True , None , [4,5,6], [1,2,3])
[print(i, end =' ') for i in tupla]
print('\n')
#SET , ESTRUCTURA MUTABLE DE ELEMENTOS ÚNICOS
set = {7,9,2,8,4,5,6,1,8,3,0,4,8,1,0,4,3,3}
[print(i, end = ' ') for i in set]
print('\n')

#FROZENSET , ESTRUCTURA INMUTABLE DE ELEMENTOS ÚNICOS
frozen_set  = frozenset([1,0,3,5,9,6,1,3,4,8,7,2])
[print(i , end = ' ') for i in frozen_set]
print('\n')

#DICCIONARIO , ESTRUCTURA EN FORMATO CLAVE-VALOR INDEXADA POR LA CLAVE
diccionario = {
"Italia" : "Roma",
"España" : "Madrid",
"Francia" : "París",
"Alemania" : "Berlín"
}

print (diccionario["Alemania"])





