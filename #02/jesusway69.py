import os
os.system('clear') #MAC/LINUX
#os.system('cls') #WINDOWS


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
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
"""

#FUNCIÓN SIN RETORNO NI PARÁMETROS
def imprime_hasta_10():
    for i in range (1,11):
        print(i)

imprime_hasta_10

#FUNCIÓN CON RETORNO
def introducir_datos()->str:
    mi_texto = input("Escriba su texto: ")
    return mi_texto

#FUNCIÓN SIN RETORNO CON UN PARÁMETRO RECIBIDO DE LA FUNCIÓN ANTERIOR 
def imprimir_datos(mi_texto):
    print(mi_texto)

imprimir_datos(introducir_datos())

#FUNCIÓN QUE RECIBE VARIOS PARÁMETROS
def calcular_media_valores (valor1, valor2, valor3, valor4):
    media = (valor1+valor2+valor3+valor4)/4
    print(media)

calcular_media_valores(1,5,9,10)

#FUNCIÓN QUE RECIBE UNA LISTA COMO PARÁMETRO
def calcular_media_lista (mis_valores):
    print(sum(mis_valores)/len(mis_valores))

calcular_media_lista([1,5,9,10])

#FUNCIÓN LAMBDA (SÓLO PARA CÁLCULOS)
calcular_media_lambda = lambda valor1,valor2,valor3,valor4:(valor1+valor2+valor3+valor4)/4

print(calcular_media_lambda(1,5,9,10))






 
