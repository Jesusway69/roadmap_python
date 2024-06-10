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


class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
     print("Creando objeto..")


if __name__ == "__main__":
    instance1 = Singleton()
    instance2 = Singleton()
    print ("Instancia 1 = ", instance1)
    print ("Instancia 2 = ", instance2)
    print("\n")

""" * DIFICULTAD EXTRA (opcional):
 * Utiliza el patrón de diseño "singleton" para representar una clase que
 * haga referencia a la sesión de usuario de una aplicación ficticia.
 * La sesión debe permitir asignar un usuario (id, username, nombre y email),
 * recuperar los datos del usuario y borrar los datos de la sesión."""

class User (metaclass=SingletonMeta):
    __instance = None
    def get_instance():
         if UserSingleton.__instance == None:
            instance = super().__init__()
            __instance = instance

            return __instance
    def remove_instance():
        if UserSingleton.__instance != None:
            UserSingleton.__instance = None
         
class UserSingleton(User):
   
    def __init__(self,id,username,name,email):
        self.id = id
        self.username = username
        self.name = name
        self.email = email
        UserSingleton.__instance = self
        




ins_jesus = UserSingleton(1, "Jesusway69", "Jesus", "jesusway60@midominio.es")
ins_jose = UserSingleton(2, "Pepe84", "Jose", "pepepepe@midominio.es")


print(f"Sesion = {ins_jesus.get_instance.__closure__} , Username: {ins_jesus.username}, Nombre:{ins_jesus.name}, Email: {ins_jesus.email}")
print(f"Sesion = {ins_jose.get_instance.__closure__} , Username: {ins_jose.username}, Nombre:{ins_jose.name}, Email: {ins_jose.email}")
#UserSingleton.remove_instance()
print (ins_jesus.remove_instance.__closure__)
ins_ana = UserSingleton(3, "Ana57", "Ana", "anagarcia@midominio.es")
print(ins_ana.get_instance.__closure__)