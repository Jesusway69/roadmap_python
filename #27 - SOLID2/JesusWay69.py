import os, platform
from math import pi

if (platform.platform().startswith("macOS") or platform.platform().startswith("Linux")):
    os.system('clear')
else:
    os.system('cls')

    """ * EJERCICIO:
 * Explora el "Principio SOLID Abierto-Cerrado (Open-Close Principle, OCP)"
 * y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.
 """
    
class Figure:
    def __init__(self, data1, data2):#Creamos una clase para generar objetos de figuras geométricas
        self.data1 = data1 # que se crearán aportando 2 medidas, base y altura si es un rectángulo
        self.data2 = data2 # o radio y PI si se trata de un círculo por ejemplo

class RectangleArea: # Al crear una clase con una función específica para calcular el área de un rectángulo
    def calc(object):  # no nos serviría para calcular el área de otra figura geométrica
        return object.data1 * object.data2
    
rectangle = Figure(2,4)
print(f"El área del rectángulo es: {RectangleArea.calc(rectangle)}")


class CalulateArea(Figure):#Si creamos una clase genérica que herede los objetos de la clase padre Figure
    def rectangle(object): # podremos ampliar el cálculo de áreas de más figuras añadiendo más métodos a esa clase hija
        return object.data1 * object.data2
    
    def circle_for_radius(object):
        return round((object.data1 ** 2 * pi),2)
    
    def circle_for_diameter(object):
        return round(((object.data1 / 2) ** 2 * pi),2)
    
    def circle_for_perimeter(object):
        return round((object.data1 * 2),2)
    
    def square(object):
        return object.data1 ** 2
    
    def triangle(object):
        return round((object.data1 * object.data2 / 2),2)
    
square1 = Figure(4,None)
circle1 = Figure(4, None)
circle2 = Figure(circle1.data1 * 2, None)
circle3 = Figure(circle2.data1 * pi, None)
triangle1 = Figure(3,7)
print (f"El área del cuadrado es: {CalulateArea.square(square1)}")
print (f"El área del círculo por su radio es: {CalulateArea.circle_for_radius(circle1)}")
print (f"El área del círculo por su diámetro es: {CalulateArea.circle_for_diameter(circle2)}")
print (f"El área del círculo por su perímetro es: {CalulateArea.circle_for_perimeter(circle3)}")
print (f"El área del triángulo es: {CalulateArea.triangle(triangle1)}")
print()

 

 
"""
    * DIFICULTAD EXTRA (opcional):
    * Desarrolla una calculadora que necesita realizar diversas operaciones matemáticas.
    * Requisitos:
    * - Debes diseñar un sistema que permita agregar nuevas operaciones utilizando el OCP.
    * Instrucciones:
    * 1. Implementa las operaciones de suma, resta, multiplicación y división.
    * 2. Comprueba que el sistema funciona.
    * 3. Agrega una quinta operación para calcular potencias.
    * 4. Comprueba que se cumple el OCP."""
    
class Operator:
    def __init__(self,num1, num2) -> None:
        self.num1 = num1
        self.num2 = num2

    def my_sum(self):
        return self.num1 + self.num2
    def my_subt(self):
        return self.num1 - self.num2
    def my_mult(self):
        return self.num1 * self.num2
    def my_div(self):
        return round((self.num1 / self.num2),2)
        
op1 = Operator(2,3)

print(op1.my_sum())
print(op1.my_subt())
print(op1.my_div())
print(op1.my_mult())

class Power(Operator):
    def __init__(self,num1, num2) -> None:
        self.num1 = num1
        self.num2 = num2
        

    def my_pow(self):
        acc = self.num1
        for i in range(1, self.num2):
            acc = Operator(self.num1 , acc).my_mult()   
        return acc
print()
op1 = Power(2,3)
print(op1.my_sum())
print(op1.my_subt())
print(op1.my_div())
print(op1.my_mult())
print(op1.my_pow())
