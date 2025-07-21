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
    
    def __init__(self, name):
        self.name = name  
        User.auto_increment_user_id += 1
        self.id = User.auto_increment_user_id
        self.user_posts = []
        self.follow = ()


    def create_Post(self, message):
        self.message = message
        if (len(self.message)>200):
            print("No se puede crear un post de más de 200 caracteres")
        else:
            self.user_posts.append(self.message)
        

    def following(self, follow = ()):
        self.follow = follow
        return self.follow

    def show_posts(self):
        print(f"Mensajes de {self.name}:")
        [print("-", post, ", creado el", '{}/{}/{}'.format(DT.now().day,DT.now().month,DT.now().year),
                "message id: ", index+1) for index, post in enumerate(self.user_posts)]
    
    def show_user_profile(self):
        users_following = self.following(self.follow)
        print()
        print(f"INFORMACIÓN DE USUARIO\n -------------------\nUsername: {self.name}\nUserID: {self.id}")
        print(f"Following:")
        for follower in users_following:
            print("-",follower.name)
        self.show_posts()
        print()


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
victor = User(users_list[8])
paula = User(users_list[9])
miguel = User(users_list[10])


manolo.create_Post(f"Este es el primer mensaje de {manolo.name}")
manolo.create_Post(f"Este es el segundo mensaje de {manolo.name}")
sara.create_Post(f"Este es el primer mensaje de {sara.name}")
pedro.create_Post(f"Este es el primer mensaje de {pedro.name}")
kevin.create_Post(f"Este es el primer mensaje de {kevin.name}")
sara.create_Post(f"Este es el segundo mensaje de {sara.name}")

manolo.following((luis, ana))
sara.following((pedro,))
manolo.show_user_profile()
sara.show_user_profile()
megan.show_user_profile()
pedro.show_user_profile()




