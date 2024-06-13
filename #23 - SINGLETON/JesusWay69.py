import os, platform

if (platform.platform().startswith("macOS") or platform.platform().startswith("Linux")):
    os.system('clear')
else:
    os.system('cls')


""" * EJERCICIO:
 * Explora el patrón de diseño "singleton" y muestra cómo crearlo
 * con un ejemplo genérico.
 *
"""

class SingletonMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
       
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton1(metaclass=SingletonMeta):
    def some_business_logic(self):
     print("Creando objeto..")

if __name__ == "__main__":
        instance1 = Singleton1()
        instance2 = Singleton1()
        print ("Instancia 1 = ", instance1)
        print ("Instancia 2 = ", instance2)
        print("\n")

""" * DIFICULTAD EXTRA (opcional):
 * Utiliza el patrón de diseño "singleton" para representar una clase que
 * haga referencia a la sesión de usuario de una aplicación ficticia.
 * La sesión debe permitir asignar un usuario (id, username, nombre y email),
 * recuperar los datos del usuario y borrar los datos de la sesión."""

def singleton (class_instance):
    instances = {}
    def get_instance(*args, **kwargs):
        if class_instance not in instances:
            instances[class_instance] = class_instance(*args, **kwargs)
            return instances[class_instance]
        elif class_instance in instances:
            return instances[class_instance]
        elif class_instance == None:
            instances.clear()
            return instances[class_instance]
    return get_instance
    


@singleton 
class Session:
    def __init__(self,id=None,username=None,name=None,email=None):
   
            self.id = id
            self.username = username
            self.name = name
            self.email = email


    
    

jesus = Session(1, "Jesusway69", "Jesus", "jesusway60@midominio.es")
jose = Session(2, "Pepe84", "Jose", "pepepepe@midominio.es")
print(jesus , " -- ", jose)
print(f"Jesus = id: {jesus.id}, username: {jesus.username}, name: {jesus.name}, email: {jesus.email}")
print(f"Jose = id: {jose.id}, username: {jose.username}, name: {jose.name}, email: {jose.email}")

#remove_instance(jose)
print(jesus)
print(f"Jesus = id: {jesus.id}, username: {jesus.username}, name: {jesus.name},email: {jesus.email}")



# class Session:
#     def __init__(self,id,username,name,email):
        
#         self.id = id
#         self.username = username
#         self.name = name
#         self.email = email
#     # def Session(self,id,username,name,email):
#     #     self.id = id
#     #     self.username = username
#     #     self.name = name
#     #     self.email = email

# class Singleton(Session):
#     _session = None
#     def get_instance(self,id,username,name,email):
#         _session = Session
#         if _session == None:
#             _session = super().__new__(self,id,username,name,email)
#         return _session
        
    
#     def delete_session():
#         if Singleton.get_instance() != None:
#             Session

# jesus = Session(1, "Jesusway69", "Jesus", "jesusway60@midominio.es")
# jesus = Singleton(jesus.id,jesus.username,jesus.name,jesus.email)


# jose = Session(2, "Pepe84", "Jose", "pepepepe@midominio.es")
# jose = Singleton(jose.id,jose.username,jose.name,jose.email)
# print(jesus, jesus.name)
# print(jose , jose.name)



















# class Singleton:
#     _instance = None
#     id: int = None
#     username: str = None
#     name: str = None
#     email: str = None

#     def __new__(cls):
#         if cls._instance is None:
#             cls._instances = super().__new__(cls)
#         return cls._instance
    
#     def setter(self,id,username,name,email):
#         self.id = id
#         self.username = username
#         self.name = name
#         self.email = email
        
#     def getter(self):
#         return self.id,self.username,self.name,self.email
        

#     def remove_instance(self):
#         self.id = None
#         self.username = None
#         self.name = None
#         self.email = None
         
# class Session(MetaClass = Singleton):
#     #__instance = None
#     def __init__(self,id,username,name,email):
#         super.__init__()
#         self.id = id
#         self.username = username
#         self.name = name
#         self.email = email
#         #Singleton.__instance = self
        




# ins_jesus = Singleton
# print(ins_jesus.setter(1, "Jesusway69", "Jesus", "jesusway60@midominio.es"))

# ins_jesus.setter(1, "Jesusway69", "Jesus", "jesusway60@midominio.es")
# ins_jose = Singleton().set(2, "Pepe84", "Jose", "pepepepe@midominio.es")


# print(f"Sesion = {ins_jesus} , Singletonname: {ins_jesus.username}, Nombre:{ins_jesus.name}, Email: {ins_jesus.email}")
# print(f"Sesion = {ins_jose} , Singletonname: {ins_jose.username}, Nombre:{ins_jose.name}, Email: {ins_jose.email}")
# #Session.remove_instance()
# Singleton.remove_instance()
# ins_ana = Singleton(3, "Ana57", "Ana", "anagarcia@midominio.es")
# print(ins_ana, "Singletonname: ", ins_ana.username)