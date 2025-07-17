import os, platform

if (platform.platform().startswith("macOS") or platform.platform().startswith("Linux")):
    os.system('clear')
else:
    os.system('cls')

"""
 * EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
"""

#FUNCIÓN SIN RETORNO NI PARÁMETROS
def print_until_10():
    for i in range (1,11):
        print(i, end=' ')
print_until_10()

#FUNCIÓN CON RETORNO
def input_data()->str:
    my_text = input(" \nEscriba su texto: ")
    return my_text

#FUNCIÓN SIN RETORNO CON UN PARÁMETRO RECIBIDO DE LA FUNCIÓN ANTERIOR 
def print_data(my_text:str):
    print(my_text)
print_data(input_data())

#FUNCIÓN QUE RECIBE VARIOS PARÁMETROS
def calc_avg (value1, value2, value3, value4, value5):
    print("prueba args:")
    print((value1 + value2 + value3 + value4 + value5) / 5)
calc_avg(1, 3, 5, 7, 9)

my_list = [1, 3, 5, 7, 9] #variable global
my_other_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] #variable global

#FUNCIÓN QUE RECIBE UNA LISTA COMO PARÁMETRO
def calc_avg_list (my_list):
    print(sum(my_list) / len(my_list))
calc_avg_list(my_list)

#FUNCIÓN LAMBDA (SÓLO PARA CÁLCULOS)
calculate_avg_with_lambda_funtcion = lambda value1, value2, value3, value4, value5: (value1 + value2 + value3 + value4 + value5) / 5
print(int(calculate_avg_with_lambda_funtcion(1,3,5,7,9)))

#FUNCIÓN LAMBDA CON FUNCIÓN DE LENGUAJE filter Y LLAMADA A OTRA FUNCIÓN ANTERIOR
odd_numbers = filter(lambda filtrado: filtrado % 2 != 0, my_other_list)
calc_avg_list(list(odd_numbers))

#FUNCIÓN QUE RECIBE LA VARIABLE GLOBAL my_list E IMPRIME SUS VALORES CON BUCLE FOR
def print_numbers_list_for(my_list):
    for i in (my_list):
     print (i, end=' -> ')
print_numbers_list_for(my_list)

#FUNCIÓN QUE IMPRIME LOS VALORES DE LA VARIABLE LOCAL my_list_local SIN USAR BUCLE
def print_numbers_list_without_loop():
    my_list_local = [1,3,5,7,9] #variable local
    print(my_list_local)
print_numbers_list_without_loop()

#FUNCIÓN QUE RECIBE VARIABLE GLOBAL E IMPRIME VALORES SIN BUCLE CON SEPARADOR DEFINIDO
def print_numbers_with_separator(my_list):
    print (*my_list , sep = "-")
print_numbers_with_separator(my_list)

#FUNCIÓN CON VARIABLE LOCAL QUE IMPRIME VALORES CON FUNCIÓN DE LENGUAJE join
def print_numbers_with_join_funtcion():
    my_list_str = ["1","3","5","7","9"] #la lista se debe definir con strings para usar join
    print('_'.join(my_list_str))
print_numbers_with_join_funtcion()

#FUNCIÓN IGUAL A LA ANTERIOR PERO RECIBE LISTA DE NÚMEROS Y LA CONVIERTE EN STRING
def print_numbers_with_join_funtcion_map(my_list):
    print('>'.join(map(str, my_list))) # con el método propio map se castea la lista de numérica a string
print_numbers_with_join_funtcion_map(my_list)

#FUNCIÓN RECURSIVA
def print_with_recursive_funtcion(num:int):
    num += 2
    if num < 10:
        print(num, end=' : ')
        print_with_recursive_funtcion(num)
print_with_recursive_funtcion(-1)

#FUNCIÓN DENTRO DE OTRA FUNCIÓN
def remove_even_numbers():
        def print_odd_numbers(my_other_list:list):
            print(my_other_list)# 4- La función interna imprime la lista de números impares

        print(my_other_list[0 : len(my_other_list)])# 1- Se imprime la lista completa
        for i in my_other_list:
          if i % 2 == 0:
            my_other_list.remove(i)# 2- Se quitan los números pares
        print_odd_numbers(my_other_list)# 3- Llamamos la la función que imprime y le pasamos la lista de números impares
remove_even_numbers()

"""
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda."""

string1 = "Hola"
string2 = "Python"
print ("\nEJERCICIO PROPUESTO")
print ("-------------------")

def hello_python(string1,string2):
    acc = 0
    for i in range (1,101):
        if i % 3 == 0 and i % 5 == 0:
            print(string1, string2)
        elif i % 3 == 0:
            print(string1)
        elif i % 5 == 0:
            print (string2)
        else:
            print(i)
            acc += 1
    print(f"hay {acc} números que no son múltiplos de 3 ni de 5")

hello_python(string1,string2)