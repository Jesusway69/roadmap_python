import os, platform
from abc import ABC, abstractmethod

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

class Apple(Fruit):
    def __init__(self) -> None:
        self.name = "manzana"

class Melon(Fruit):
    def __init__(self) -> None:
        self.name = "melón"

 
pera = Fruit(Pear()).print_fruit()
melon = Fruit(Melon()).print_fruit()
manzana = Fruit(Apple()).print_fruit()

class FruitDIP(ABC):
    @abstractmethod
    def set_name(self, name):
        self.name = name
class PrintFruitDIP(ABC):
    @abstractmethod
    def print_fruit(self):
        self.article = "un"
        if self.name.endswith('a'):
            self.article = "una"
        print (f"La fruta es {self.article} {self.name} ")

class Orange(FruitDIP, PrintFruitDIP):
    name = "naranja"
    def set_name(self, name):
        return super().set_name(name)
    def print_fruit(self):
        return super().print_fruit()
    
class WaterMelon(FruitDIP, PrintFruitDIP):
    name = "sandía"
    def set_name(self, name):
        return super().set_name(name)
    def print_fruit(self):
        return super().print_fruit()
    
class Lemon(FruitDIP, PrintFruitDIP):
    name = "limón"
    def set_name(self, name):
        return super().set_name(name)
    def print_fruit(self):
        return super().print_fruit()
    
naranja = Orange().print_fruit()
sandia = WaterMelon().print_fruit()
limon = Lemon().print_fruit()

    
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


class MessageInterface(ABC):
    @abstractmethod
    def email(self):
        pass
    @abstractmethod
    def push(self):
        pass
    @abstractmethod
    def sms(self):
        pass

class SendNotification(MessageInterface):
    def email(self, message):
        self.message = message
        print (self.message, "--> Enviando email...")
    def push(self,message):
        self.message = message
        print (self.message,"--> Enviando push...")
    def sms(self,message):
        self.message = message
        print (self.message,"--> Enviando SMS...")

class Confirmation(MessageInterface):   
    def confEmail(self,message):
        message = SendNotification()
        print (message,"--> Email enviado")
    def push(self,message):
        self.message = message
        print (self.message,"--> Mensaje PUSH enviado")
    def sms(self,message):
        self.message = message
        print (self.message,"--> Mensaje SMS enviado")
    
class Email(SendNotification, Confirmation):
    def __init__(self):
        message = "Esto es un mensaje de email..."
        return super().email(message)
class Push(SendNotification):
    def __init__(self) -> None:
        message = "Esto es un mensaje PUSH..."
        return super().push(message)
class Sms(SendNotification):
    def __init__(self) -> None:
        message = "Esto es un mensaje SMS..."
        return super().sms(message)
    
email = Email()
email.confEmail(email)
push = Push()
sms = Sms()