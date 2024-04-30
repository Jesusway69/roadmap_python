import os
os.system('cls')



#FUNCION FIBONACCI POR ITERACIÓN
def fibonacci (fib_position:int):
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
    print("Sólo se pueden introducir números, pruebe de nuevo")