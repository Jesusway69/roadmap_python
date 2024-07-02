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



class Library():
    def __init__(self) -> None:
        self.books_list = []
        self.users_list = []
        self.state_dict = {}

    def add_book(self,title, author, units): 
        self.title = title
        self.author = author
        self.units = units
        book = [] 
        book.append(title)
        book.append(author)
        book.append(units)
        self.books_list.append(book)
        return self.books_list

    def add_user (self, id, name, email):
        self.id = id
        self.name = name
        self.email = email
        user = []
        user.append(self.id)
        user.append(self.name)
        user.append(self.email)
        self.users_list.append(user)
        return self.users_list

    def rent_book(self, book, user):
        self.book = book
        self.user = user
        id=0
        title=""
        for data in book:
            if data == type(int):
                id=data
                title = self.book[0]
        
        self.state_dict[title] = id
        uds = self.books_list[len(self.books_list)-1][2]
        uds -=1
        return self.state_dict

    def return_book(self, book):
        self.book = book     
        title= book[0]
        for titles in self.state_dict.keys():
            if title in self.state_dict:
               self.state_dict.pop(titles)
        uds = self.books_list[len(self.books_list)-1][2]
        uds +=1
        return self.state_dict

    def printer_book(books:list):
        header = ["Título: ", "   Autor: ", "   Uds: "]
        for book in books:
            for data, head in zip(book,header):
                print(head , data, end="")
            print()

    def printer_user(users:list):
        header = ["ID: ", "   Nombre: ", "   Email: "]
        for user in users:
            for data, head in zip(user,header):
                print(head, data, end="  ")
            print()



book1 = Library()
user1 = Library()
rent1 = Library()
quijote = book1.add_book("Don Quijote", "Cervantes", 3)
Library.printer_book(quijote)
jesus = user1.add_user(1,"Jesus","jesus@gmail.com")
Library.printer_user(jesus)
print(rent1.rent_book(quijote, jesus))





# book2 = Library.books("Git y Github", "Mouredev", 4)
# jesus = Library.users(1, "Jesus", "jesus@gmail.com")
# sandra = Library.users(2, "Sandra", "sandra@icloud.com")
# Library.printer(Library.add_book(book1))
# Library.add_book(book2)
# Library.add_user(jesus)
# Library.add_user(sandra)



class Book:
    def __init__(self, title, author, units) -> None:
        self.title = title
        self.author = author
        self.units = units

class User:
    def __init__(self, id, name, email) -> None:
        self.id = id
        self.name = name
        self.email = email

class Rent:
    def __init__(self) -> None:
        self.rent_books = []
    def rent_book(self, book, user):
        if book.units > 0:
            book.units -= 1
            self.rent_books.append([book.title, user.id])
    def return_book(self,book):
        for rent in self.rent_books:
            if rent[0]==book:
                self.rent_books.pop(rent)
                book.units +=1
                
class Management(Rent):
    def __init__(self) -> None:
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)

    def add_user(self, user):
        self.users.append(user)

    def manage_rent(self,title,id):
        for user in self.users:
            if user[0] == title and user[1] == id:
                return self.rent_book(title,id)
            else:
                return False
    def manage_return(self,title,id):
        for user in self.users:
            if user[0] == title and user[1] == id:
                return self.return_book(title,id)
            else:
                return False
    


        

        
    
        
