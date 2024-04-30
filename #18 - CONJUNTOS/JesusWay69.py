import os
os.system('clear')


""" * EJERCICIO:
 * Utilizando tu lenguaje crea un conjunto de datos y realiza las siguientes
 * operaciones (debes utilizar una estructura que las soporte):
 * - Añade un elemento al final.
 * - Añade un elemento al principio.
 * - Añade varios elementos en bloque al final.
 * - Añade varios elementos en bloque en una posición concreta.
 * - Elimina un elemento en una posición concreta.
 * - Actualiza el valor de un elemento en una posición concreta.
 * - Comprueba si un elemento está en un conjunto.
 * - Elimina todo el contenido del conjunto.
 *
 """

my_list = [1,7,0,2,4,6]
print("La lista original:            ", my_list)
my_list.append(8)

print("Le añadimos un 8 al final:    ",my_list)

my_list.insert(0,3)

print("Le añadimos un 3 al principio:",my_list)


my_tuple = "Hola", True, (1,2,3)
print("Creamos esta tupla:           ",my_tuple)
[my_list.insert(3,my_tuple[i]) for i in range(2,-1,-1)]

print("Insertamos los elementos de la tupla en la lista en la posición 3:",my_list)
hola = "Hola" in my_list
print ("¿El elemento \"Hola\" está en la lista? ", hola )
my_list.clear()
print("Borramos todo el contenido de la lista, ahora la lista es esta: ", my_list)

"""* DIFICULTAD EXTRA (opcional):
 * Muestra ejemplos de las siguientes operaciones con conjuntos:
 * - Unión.
 * - Intersección.
 * - Diferencia.
 * - Diferencia simétrica."""

my_set1 = {"Metallica", "Pantera", "Slipknot", "SOAD", "Megadeth", "Iron Maiden", "Tool", "Anthrax", "Gojira", "Avenged Sevenfold", "Korn", "Alice Cooper", "AC/DC"}
my_set2 = {"Kiss", "Judas Priest", "Saxon", "AC/DC", "Metallica", "Black Sabbath", "Megadeth","Linkin Park", "Pantera", "Alter Bridge", "Guns n' Roses", "Scorpions" }




