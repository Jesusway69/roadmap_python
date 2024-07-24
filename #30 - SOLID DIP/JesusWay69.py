import os, platform

if (platform.platform().startswith("macOS") or platform.platform().startswith("Linux")):
    os.system('clear')
else:
    os.system('cls')

""" 
 * EJERCICIO:
 * Explora el "Principio SOLID de Inversión de Dependencias (Dependency Inversion
 * Principle, DIP)" y crea un ejemplo simple donde se muestre su funcionamiento 
 * de forma correcta e incorrecta.
 *
"""
"""
El Principio de Inversión de Dependencia (DIP) establece que las clases de alto nivel
 no deben depender de clases de bajo nivel.
Es decir, se deben fabricar abstracciones mediante interfaces y clases abstractas
 para asegurarse de que dos módulos que deben interactuar entre sí solo se comuniquen
  a través de estas mismas, y de esta manera para esconder sus implementaciones concretas."""

class Fruit:
    def __init__(self, object) -> None:
        self.object = object
        self.name = object.name

    def print_fruit(self):
        self.article = "un"
        
        if self.object.name.endswith('a'):
            self.article = "una"
        print (f"La fruta es {self.article} {self.name} ")
class Pear(Fruit):
    def __init__(self) -> None:
        self.name = "pera"
    def print_fruit(self):
        super().print_fruit()
class Apple(Fruit):
    def __init__(self) -> None:
        self.name = "manzana"
class Melon(Fruit):
    def __init__(self) -> None:
        self.name = "melón"

 
pera = Fruit(Pear()).print_fruit()
melon = Fruit(Melon()).print_fruit()
manzana = Fruit(Apple()).print_fruit()


    
""" 
 * DIFICULTAD EXTRA (opcional):
 * Crea un sistema de notificaciones.
 * Requisitos:
 * 1. El sistema puede enviar Email, PUSH y SMS (implementaciones específicas).
 * 2. El sistema de notificaciones no puede depender de las implementaciones específicas.
 * Instrucciones:
 * 1. Crea la interfaz o clase abstracta.
 * 2. Desarrolla las implementaciones específicas.
 * 3. Crea el sistema de notificaciones usando el DIP.
 * 4. Desarrolla un código que compruebe que se cumple el principio."""