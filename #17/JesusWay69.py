import os, random
os.system('cls')

"""* EJERCICIO:
 * Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
 * números del 1 al 10 mediante iteración.
 *
 * DIFICULTAD EXTRA (opcional):
 * Escribe el mayor número de mecanismos que posea tu lenguaje
 * para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?"""

'''FOR CON RANGO CONDICIONAL DE INICIO Y PARADA'''
for i in range (1,11):
    print(i, end=" ")
i=0
print()

'''FOR CON RANGO SOLO DE PARADA Y CONDICIONAL PARA SALTARSE EL 0 CON EL QUE EMPIEZA POR DEFECTO'''
for i in range (11):
    if i == 0:
        continue
    print(i, end=" ")
i=0
print()
'''FOR ANIDADOS CON CONDICIÓN DE INICIO,PARADA Y PASO, EL PRIMERO IMPRIME LOS IMPARES Y EL SEGUNDO LOS PARES'''
for i in range (1,11,2):
    print(i, end=" ")
    for j in range(1):
        if i<10:
            print (i+1, end=" ")
i=0
print() 
'''BUCLE FOR-ELSE CON CONDICIÓN DE INICIO Y PARADA'''
for i in range (0,1):
    if i == 1:
        break 
else:
    for i in range(i+1,11):
        print(i,end=" ")
i=0
print()

   
'''WHILE CON CONDICIÓN DE PARADA Y OPERADOR DE INCREMENTO'''
while i<10:
    i+=1
    print(i, end=" ")
i=0
print()

'''WHILE CON OPERADOR DE INCREMENTO Y CONDICIÓN DE SALIDA (DO-WHILE)'''
while True:
    i+=1
    print (i,end=" ")
    if i == 10:
        break
i=0
print()

'''WHILE ANIDADOS CON CONDICIÓN DE PARADA Y OPERADOR DE INCREMENTO'''
while i<10:
   i+=1
   print(i, end=" ")
   while i<10:
       i+=1
       print(i, end=" ")
i=0
print()

'''FUNCIÓN CON INCREMENTO, CONDICIÓN DE PARADA Y RECURSIVIDAD'''
def iterator_1(i:int):
    i+=1
    print(i, end=" ")
    if i<=9:
        iterator_1(i)
iterator_1(i)
print()

'''FUNCIÓN CON GENERACIÓN DE NÚMEROS ALEATORIOS QUE SE AÑADEN A UN SET HASTA QUE ESTE CUMPLA LA CONDICIÓN DE LONGITUD 10'''
def iterator_2(i:int):
    my_set = set()
    while len(my_set)<i:
       num = random.randint(1,10)
       my_set.add(num)
    [print(num, end=" ") for num in my_set]
iterator_2(10)
print()

'''FUNCIÓN CON MÉTODO DE LENGUAJE ITER'''
def iterator_3():
    my_list = []
    [my_list.append(i) for i in range(1,11)]
    my_iterator = (iter(my_list))
    [print(next(my_iterator), end=" ") for i in range (len(my_list))]
iterator_3()
print()

def iterator_4(symbols:str):
    for char in symbols:
        print(ord(char)-40,end=" ")
iterator_4(")*+,-./012")
