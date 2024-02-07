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



#FUNCION FIBONACCI POR ITERACIÓN
'''def fibonacci (fib_position:int):
    list_fibonacci = [0,1]
    for i in range (0,fib_position):
        list_fibonacci.append(list_fibonacci[i]+list_fibonacci[i+1])
        print("Posición " , i+1 , "=" ,list_fibonacci[i])
    print (f"La posición {fib_position} de la secuencia Fibonacci tiene el valor {list_fibonacci[fib_position-1]}")   

while True:
  fib_position = input("Introduzca un número: ")
  try:
   fib_position = int(fib_position)
   fibonacci(fib_position)
   break
  except ValueError:
    print("Sólo se pueden introducir números, pruebe de nuevo")'''




#FUNCIÓN FIBONACCI POR RECURSIVIDAD
'''
list_fibonacci = [0,1]
copy, counter1, counter2 = 0, 0, 1

def fibonacci (fib_position:int):
   global copy , counter1, counter2 
   if fib_position>copy:
    copy = fib_position
   if fib_position ==0:
     print("el nº debe ser mayor a 0")
     return
   if fib_position==2:
    print(f"La posición {copy} de la secuencia Fibonacci tiene el valor {list_fibonacci[copy-1]} ")
    return
   if fib_position == 1:
    print ("La posición 1 de la secuencia Fibonacci tiene el valor 0 ")
    return
   if fib_position == 2:
    print ("La posición 2 de la secuencia Fibonacci tiene el valor 1 ")
    return
   elif fib_position >=2:   
     list_fibonacci.append(list_fibonacci[counter1]+list_fibonacci[counter2])
   counter1 +=1
   counter2 +=1    
   fib_position -=1
   fibonacci(fib_position)


while True:
  fib_position = input("Introduzca un número: ")
  try:
   fib_position = int(fib_position)
   fibonacci(fib_position)
   break
  except ValueError:
    print("Sólo se pueden introducir números, pruebe de nuevo")'''


 
num =4
acc=0
def factorial (factorial_num:int):#4  3  2  1
  global acc
  if factorial_num>1:#si  si  si  no
   counter = factorial_num * factorial_num-1# 4*3=12  3*2=6   2*1=2
   acc = acc + counter# 12+0=12  12+6=18  18+2=20
   factorial_num -=1
   factorial(factorial_num)
  else:
   print(acc)#20

factorial(num)





