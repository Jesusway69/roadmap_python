import os
os.system('cls')

"""
* EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición,
 *   recorrido, conversión a mayúsculas y minúsculas, reemplazo, división, unión,
 *   interpolación, verificación...
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas"""
print("MÉTODOS Y MANIPULACIONES BÁSICAS CON STRINGS")
my_string = "Hola PYTHON"
print ("\"Hola Python\"")
#Para imprimir con comillas o caracteres reservados se usa backslash antes del caracter

print(r"c:\users\usuario\carpeta\archivo.txt")
#Si queremos imprimir un string que incluya backslash formateamos con una r (raw string)

print("Ho" + "la Py" + "thon") 
#Concatenación de varios strings

print ("Ding! " * 5)
 #Python admite multiplicaciones de strings

print (str(len("123456789")) + " caracteres")
 #La función len() devuelve medida en int, str castea a string y + concatena

print(len("123456789") * 9)
# La función len() devuelve cantidad de caracteres y se puede operar con el número resultante

print(my_string.find("THON"))
# .find devuelve el índice donde comienza la subcadena especificada

print(my_string.replace("PYTHON","JAVASCRIPT"))
# .replace sustituye la parte del string especificada por otra especificada

print(my_string.capitalize())
# .capitalize devuelve el string con el primer caracter en mayúsculas y el resto en minúsculas

print(my_string.upper())
# .upper devuelve todo el string en mayúsculas

print(my_string.lower())
# .lower devuelve todo el string en minúsculas

print(my_string[2:8])
#deja sólo los caraceteres dentro del rango, el resto los borra(en este caso borra los 0,1,9,10 y 11)

print(my_string[:8])
#En caso de omitir el primer valor equevale a 0 y solo borra a partir del valor especificado

lista_caracteres_ascii = [72,111,108,97,32,80,121,116,104,111,110]
#lista con los códigos ascii de "Hola Python"

[print(chr(i) , end='') for i in lista_caracteres_ascii]
#Con la función chr() obtenemos el caracter asociado a su código ascii

print('')
[print(my_string[i] , end='') for i in range(len(my_string))]
#Se pueden recorrer los caracteres de un string con un bucle for por índice 


print('')
[print(my_string[i] , end='') for i, char in enumerate(my_string)]
#Tambien con un bucle for por índice usando la función enumerate()

print('')
[print(char , end='') for char in my_string]
#Se pueden recorrer los caracteres de un string con un bucle foreach sin índice
