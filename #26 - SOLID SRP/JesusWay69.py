import os, platform

if (platform.platform().startswith("macOS") or platform.platform().startswith("Linux")):
    os.system('clear')
else:
    os.system('cls')

""" 
 * EJERCICIO:
 * Explora el "Principio SOLID de Responsabilidad Única (Single Responsibility
 * Principle, SRP)" y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.
 """


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

print("\n")

"""
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
        book.append(self.title)
        book.append(self.author)
        book.append(self.units)
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
        if book.units > 0:   
            self.state_dict[self.book.title] = self.user.id
            self.book.units -=1 
        return self.state_dict

    def return_book(self, book, user):
        self.book = book 
        self.user = user    
        if book.title in self.state_dict.keys():
            if user.id in self.state_dict.values():
               del self.state_dict[book.title] 
               self.book.units +=1
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


print("EJEMPLO CON UNA CLASE PARA TODA LA GESTIÓN")
print("------------------------------------------")

book1 = Library()
user1 = Library()
rent1 = Library()

quijote = book1.add_book("Don Quijote de La Mancha", "Miguel de Cervantes", 3)
jesus = user1.add_user(1,"Jesus","jesus@gmail.com")
Library.printer_user(jesus)
Library.printer_book(quijote)
print (f"El libro '{book1.title}' tiene {book1.units} ejemplares")
rent1.rent_book(book1,user1)
print(f"El usuario {user1.name} ha alquilado un ejemplar del libro '{book1.title}'")
print (f"El libro '{book1.title}' ahora tiene {book1.units} ejemplares")
rent1.return_book(book1, user1)
print(f"El usuario {user1.name} ha devuelto un ejemplar del libro '{book1.title}'")
print (f"El libro '{book1.title}' vuelve a tener {book1.units} ejemplares")


print("\n")

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
            return self.rent_books
                  
class Management:
    def __init__(self) -> None:
        self.books = []
        self.users = []
        self.rent_books = []
        self.rent = Rent()
        

    def add_book(self, book):
        self.books.append(book)

    def add_user(self, user):
        self.users.append(user)

    def manage_rent(self,title,id):
        self.rent.rent_book(title, id)
        for user in self.rent_books:
            if user[0] == title and user[1] == id:              
                return self.rent()
            else:
                return False
    def manage_return(self,book,user):
            if [book.title,user.id] in self.rent.rent_books:
                self.rent.rent_books.remove([book.title,user.id])
                book.units +=1
            else:
                return False
            
print("EJEMPLO VARIAS CLASES CON RESPONSABILIDADES ÚNICAS PARA LA GESTIÓN")
print("------------------------------------------------------------------")
   
book2 = Book("Git y Github", "Mouredev", 4)
jesus = User(1, "Jesus", "jesus@gmail.com")
sandra = User(2, "Sandra", "sandra@icloud.com")
rent = Management() 

print(f"Uds disponibles del título '{book2.title}' : {book2.units}")
rent.manage_rent(book2, sandra)
print(f"La usuaria {sandra.name} ha alquilado un ejemplar del libro '{book2.title}'")
print(f"Uds disponibles del título '{book2.title}' : {book2.units}")
rent.manage_rent(book2, jesus)
print(f"El usuario {jesus.name} ha alquilado un ejemplar del libro '{book2.title}'")
print(f"Uds disponibles del título '{book2.title}' : {book2.units}")
rent.manage_return(book2, sandra)
print(f"La usuaria {sandra.name} ha devuelto un ejemplar del libro '{book2.title}'")
print(f"Uds disponibles del título '{book2.title}' : {book2.units}")


        
    
        
