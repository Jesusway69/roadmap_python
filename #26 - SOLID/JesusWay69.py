import os, platform

if (platform.platform().startswith("macOS") or platform.platform().startswith("Linux")):
    os.system('clear')
else:
    os.system('cls')
print(os.getcwd())

""" * EJERCICIO:
 * Explora el "Principio SOLID de Responsabilidad Única (Single Responsibility
 * Principle, SRP)" y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.
 *
 * DIFICULTAD EXTRA (opcional):
 * Desarrolla un sistema de gestión para una biblioteca. El sistema necesita
 * manejar diferentes aspectos como el registro de libros, la gestión de usuarios
 * y el procesamiento de préstamos de libros.
 * Requisitos:
 * 1. Registrar libros: El sistema debe permitir agregar nuevos libros con
 * información básica como título, autor y número de copias disponibles.
 * 2. Registrar usuarios: El sistema debe permitir agregar nuevos usuarios con
 * información básica como nombre, número de identificación y correo electrónico.
 * 3. Procesar préstamos de libros: El sistema debe permitir a los usuarios
 * tomar prestados y devolver libros.
 * Instrucciones:
 * 1. Diseña una clase que no cumple el SRP: Crea una clase Library que maneje
 * los tres aspectos mencionados anteriormente (registro de libros, registro de
 * usuarios y procesamiento de préstamos).
 * 2. Refactoriza el código: Separa las responsabilidades en diferentes clases
 * siguiendo el Principio de Responsabilidad Única."""


class Device (object):
    def __init__(self, model, type) -> None:
        self.model = model
        self.type = type
    def get_model(self):
        return self.model()
    def get_type(self):
        return self.type()
    def print_device(self):
        return print(f"El {self.model} es un {self.type}")
Device("macbook", "laptop").print_device()


"""Referencias actuales:
https://www.freecodecamp.org/espanol/news/los-principios-solid-explicados-en-espanol/
https://softwarecrafters.io/python/principios-solid-python"""



class Library(object):
    def __init__(self) -> None:
        self.books_list = []
        self.users_list = []
        self.state_dict = {}
        self.title = ""
        self.author = ""
        self.units = None
        self.id = None
        self.name = ""
        self.email = ""

    # def books(title, author, units): 
    #     # self.title = title
    #     # self.author = author
    #     # self.units = units
    #     user_list = [] 
    #     user_list.append(title)
    #     user_list.append(author)
    #     user_list.append(units)
    #     return user_list
        
    def add_book(self,object_book):
        self.object_book = object_book
        self.books_list.append(list(self.object_book))
        return self.books_list

    # def users (self, id, name, email):
    #     self.id = id
    #     self.name = name
    #     self.email = email
    #     book_list = []
    #     book_list.append(self.id)
    #     book_list.append(self.name)
    #     book_list.append(self.email)
    #     return book_list


    def add_user(self, object_user):
        self.object_user = object_user
        self.users_list.append(list(object_user))
        return self.users_list

    def rent_book(self, book, user):
        self.book = book
        self.user = user
        self.state_dict[book] = user
        self.books_list[len(self.books_list)][2]-1

    def return_book(self, book, user):
        self.book = book
        self.user = user
        self.state_dict.pop(book)
        self.books_list[len(self.books_list)][2]+1
    def printer(object):
       
        print(object)

class Book(Library):
    def __init__(self, title, author, units) -> None:
        self.title = title
        self.author = author
        self.units = units

class User(Library):
    def __init__(self, id, name, email) -> None:
        self.id = id
        self.name = name
        self.email = email


book1 = Book("Don Quijote", "Cervantes", 3)
my_library = Book.printer(book1)







# book2 = Library.books("Git y Github", "Mouredev", 4)
# jesus = Library.users(1, "Jesus", "jesus@gmail.com")
# sandra = Library.users(2, "Sandra", "sandra@icloud.com")
# Library.printer(Library.add_book(book1))
# Library.add_book(book2)
# Library.add_user(jesus)
# Library.add_user(sandra)




        
    
        
