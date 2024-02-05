import os
os.system('cls')


"""
 * EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
 *
"""
num = 101
def countdown (num):
    num -=1
    if num >= 0:
        print(num, end=' ')
        if num % 10 == 0 and num != 100:
            print('')
        countdown(num)
countdown(num)











"""
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).
"""

