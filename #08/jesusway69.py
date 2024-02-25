import os
#os.system('clear') #MAC/LINUX
os.system('cls') #WINDOWS
""" * EJERCICIO:
 * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 * atributos y una función que los imprima (teniendo en cuenta las posibilidades
 * de tu lenguaje).
 * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 * utilizando su función.
 *
"""


class MyClass:
    def __init__(self) -> None:
        self.my_num_list = []
        
    def my_iterator(self,init_num, end_num):
     for i in range(init_num,end_num):
          self.my_num_list.append(i)
     self.show_list(self.my_num_list)

    def show_list(self, my_num_list):
       print(self.my_num_list)

result = MyClass()
result.my_iterator(1,11)
print("\n\n")


       



""" * DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido."""

class Stack():
    def __init__(self) -> None:
      self.my_stack_list = []

    def add (self, init_number, end_number):
      for num in range (init_number, end_number):
       self.my_stack_list.append(num)

    def unstack (self):
      self.my_stack_list.pop()
    
    def leght (self):
       return len(self.my_stack_list)
    
    def show (self):
       print(self.my_stack_list)


class Queue():
    def __init__(self) -> None:
      self.my_stack_list = []

    def add (self, init_number, end_number):
     for num in range (init_number, end_number):
       self.my_stack_list.append(num)

    def dequeue (self):
      self.my_stack_list.pop(0)
    
    def leght (self):
       return len(self.my_stack_list)
    
    def show (self):
       print(self.my_stack_list)

stack_instance = Stack()
queue_instance = Queue()

stack_instance.add(1,11)
stack_instance.show()
print(f"La lista tiene {stack_instance.leght()} números\n")
stack_instance.unstack()
stack_instance.show()
print(f"La lista tiene {stack_instance.leght()} números\n")

queue_instance.add(1,11)
queue_instance.show()
print(f"La lista tiene {queue_instance.leght()} números\n")
queue_instance.dequeue()
queue_instance.show()
print(f"La lista tiene {queue_instance.leght()} números\n")


   
   