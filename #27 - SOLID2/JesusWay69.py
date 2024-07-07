import os, platform

if (platform.platform().startswith("macOS") or platform.platform().startswith("Linux")):
    os.system('clear')
else:
    os.system('cls')

    """ * EJERCICIO:
 * Explora el "Principio SOLID Abierto-Cerrado (Open-Close Principle, OCP)"
 * y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.
 *
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
