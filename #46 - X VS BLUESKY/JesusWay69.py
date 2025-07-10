import os, platform
from datetime import datetime as DT

if (platform.platform().startswith("macOS") or platform.platform().startswith("Linux")):
    os.system('clear')
else:
    os.system('cls')

"""
 * EJERCICIO:
 * La alternativa descentralizada a X, Bluesky, comienza a atraer
 * a nuevos usuarios. ¿Cómo funciona una red de este estilo?
 * 
 * Implementa un sistema que simule el comportamiento de estas
 * redes sociales.
 * 
 * Debes crear las siguientes operaciones:
 * - Registrar un usuario por nombre e identificador único.
 * - Un usuario puede seguir/dejar de seguir a otro.
 * - Creación de post asociado a un usuario. Debe poseer
 *   texto (200 caracteres máximo), fecha de creación 
 *   e identificador único.   
 * - Eliminación de un post.
 * - Posibilidad de hacer like (y eliminarlo) en un post.
 * - Visualización del feed de un usuario con sus 10 publicaciones
 *   más actuales ordenadas desde la más reciente.
 * - Visualización del feed de un usuario con las 10 publicaciones
 *   más actuales de los usuarios que sigue ordenadas 
 *   desde la más reciente.
 *   
 * Cuando se visualiza un post, debe mostrarse:
 * ID de usuario, nombre de usuario, texto del post, 
 * fecha de creación y número total de likes.
 * 
 * Controla errores en duplicados o acciones no permitidas.
"""


class User:
    auto_increment_user_id = 0
    user_posts = []
    def __init__(self, name):
        self.name = name  
        User.auto_increment_user_id += 1
        self.id = User.auto_increment_user_id


    def create_Post(self, message):
        if (len(message)>200):
            print("No se puede crear un post de más de 200 caracteres")
        else:
            User.user_posts.append(message)
        

    def following():
        pass

    def show_posts(self):
        print(f"Mensajes de {self.name}:")
        [print("-", post, ", created at", '{}/{}/{}'.format(DT.now().day,DT.now().month,DT.now().year),
                "message id: ", index+1) for index, post in enumerate(User.user_posts)]

users_list = ["Manolo", "Sara", "Luis", "Ana", "Kevin", "Sandra", "Pedro", "Megan", "Victor", "Paula",
               "Miguel", "Silvia", "Pablo", "Rocío", "Joseph", "Isabel", "Tony", "Cristina", "Marco", "Elena"]
manolo = User(users_list[0])
sara = User(users_list[1])
luis = User(users_list[2])
ana = User(users_list[3])
kevin = User(users_list[4])
sandra = User(users_list[5])
pedro = User(users_list[6])
megan = User(users_list[7])

print(manolo.id, manolo.name)
print(pedro.id, pedro.name)
manolo.create_Post("Este es el primer mensaje de manolo")
manolo.create_Post("Este es el segundo mensaje de manolo")
manolo.show_posts()



