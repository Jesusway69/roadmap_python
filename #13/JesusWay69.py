import os, unittest
os.system('cls')
os.system('clear')
"""
 * EJERCICIO:
 * Crea una función que se encargue de sumar dos números y retornar
 * su resultado.
 * Crea un test, utilizando las herramientas de tu lenguaje, que sea
 * capaz de determinar si esa función se ejecuta correctamente.
 *
"""


# def sum_two_numbers(num1:int,num2:int)->int:
#     return num1+num2
# print(sum_two_numbers(15,85))

# class TestSum(unittest.TestCase):
#     def test_suma_positiva(self):
#         self.assertEqual(sum_two_numbers(3, 9), 12)  # Verifica si la suma de 3 y 5 es igual a 8

#     def test_suma_negativa(self):
#         self.assertEqual(sum_two_numbers(-1, 1), 0) 

#     def test_suma_float(self):
#         self.assertEqual(sum_two_numbers(2.5,7.3),9.8)
# if __name__ == '__main__':
#     unittest.main()

""" * DIFICULTAD EXTRA (opcional):
 * Crea un diccionario con las siguientes claves y valores:
 * "name": "Tu nombre"
 * "age": "Tu edad"
 * "birth_date": "Tu fecha de nacimiento"
 * "programming_languages": ["Listado de lenguajes de programación"]
 * Crea dos test:
 * - Un primero que determine que existen todos los campos.
 * - Un segundo que determine que los datos introducidos son correctos."""

my_personal_dict = {
   "name": "Jesus",
   "age": 48,
   "birth_date": "12-10-1975",
   "programming_languages": ["Python", "Java", "Javascript"]
}
print(len(my_personal_dict))
class TestDict(unittest.TestCase):
    def test_exist_items(self):
        self.assertEqual(len(my_personal_dict),4)

if __name__ == '__main__':
    unittest.main()