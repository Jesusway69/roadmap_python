""" * EJERCICIO:
 * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 * atributos y una función que los imprima (teniendo en cuenta las posibilidades
 * de tu lenguaje).
 * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 * utilizando su función.
 *
 * DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido."""


class MyClass:
    def __init__(self) -> None:
        self.my_num_list = []
    def my_iterator(self,init_num, end_num):
     for i in range(init_num,end_num):
      MyClass.add_num()
    def add_num(self,i):
       MyClass.my_num_list.append(i)
result = MyClass.add_num(1,11)
print(result)
       