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
 * - Registrar un usuario por nombre e identificador único. --OK
 * - Un usuario puede seguir/dejar de seguir a otro. --OK
 * - Creación de post asociado a un usuario. Debe poseer
 *   texto (200 caracteres máximo), fecha de creación 
 *   e identificador único.                            --OK
 * - Eliminación de un post.                           --OK
 * - Posibilidad de hacer like (y eliminarlo) en un post. --OK
 * - Visualización del feed de un usuario con sus 10 publicaciones
 *   más actuales ordenadas desde la más reciente.                 --OK
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
        self.user_posts = {}
        self.index_message = 0
        self.follow = set()
        self.user_followers = []

    def create_post(self, message):
        if (len(message) > 200):
            print("No se puede crear un post de más de 200 caracteres")
        else:
            self.index_message +=1
            self.user_posts[self.index_message] = {
    "message": message,
    "date": DT.now(),
    "likes": set()
}

    def following(self, *users):
        for user in users:
            self.follow.add(user)
            if self not in user.user_followers:
                user.user_followers.append(self)
        return self.follow
    
    
    def unfollow(self, user):  
        if user in self.follow:
            self.follow.remove(user) # type: ignore
            if self in user.user_followers:
                user.user_followers.remove(self)
            print(f"{self.name} ha dejado de seguir a {user.name}")
        else:
            print(f"{self.name} no puede dejar de seguir a {user.name} porque no lo estaba siguiendo anteriormente")


    def show_posts(self):    
        if len(self.user_posts) == 0:
                print(f"{self.name} no tiene nigún mensaje")
                return
        print(f"Mensajes de {self.name}:")
        for key, value in reversed(self.user_posts.items()):
            likes_counter = len(value["likes"])
            date = value["date"]
            print("-", value["message"], ", creado el", 
                  f"{date.day}/{date.month}/{date.year} {date.hour}:{date.minute}:{date.second}",
                  "message id:", key , "número de likes:", likes_counter)
        

    def show_user_profile(self):
        users_following = self.follow
        print()
        print(f"INFORMACIÓN DE USUARIO\n -------------------\nUsername: {self.name}\nUserID: {self.id}\nFollowers: {len(self.follow)}\
              \nSiguiendo a:")
        for follower in users_following:
            print("-", follower.name)
        self.show_posts()    
        print()
        

    def delete_post(self, messageID):
        if messageID not in self.user_posts:
            print(f"El usuario {self.name} no tiene ningún mensaje con id {messageID}")
        else:
            del(self.user_posts[messageID])
    

    def liked_post(self, user, postId: int):
        print("---------------------------\n")

        if postId not in user.user_posts:
            print(f"El usuario {user.name} no tiene ningún mensaje con id {postId}\n")
            return

        message = user.user_posts[postId]["message"]

        if postId not in user.user_posts:
            print(f"{self.name} no puede dar like al mensaje '{message}' porque ya le dio like antes\n")
            return

        user.user_posts[postId]["likes"].add(self)
        likes_counter = len(user.user_posts[postId]["likes"])
       
        print(f"{self.name} ha dado like al mensaje con id:{postId} de {user.name}"
            f", el mensaje de {user.name} '{message}' acumula {likes_counter} {'like' if likes_counter == 1 else 'likes'}\n")


    def unliked_post(self, user, postId:int):
        print("---------------------------\n") 
        if postId not in user.user_posts:
            print(f"el usuario {user.name} no tiene ningún mensaje con id {postId}\n")
            return
        
        message = user.user_posts[postId]["message"]

        if self not in user.user_posts[postId]["likes"]:
            print(f"{self.name} no puede quitar el like del mensaje con id {postId} de {user.name}",
                  "porque no le había dado like antes\n")
            return
        
        user.user_posts[postId]["likes"].discard(self)
        likes_counter = len(user.user_posts[postId]["likes"])

        print(f"{self.name} ha quitado el like al mensaje con id:{postId} de {user.name}"
        f", el mensaje de {user.name} '{message}' acumula {likes_counter} {'like' if likes_counter == 1 else 'likes'}\n")
        return
        
#LISTA DE USUARIOS
users_list = ["Jesus", "Sara", "Luis", "Ana", "Kevin", "Sandra", "Pedro", "Megan", "Victor", "Paula",
               "Miguel", "Silvia", "Pablo", "Rocío", "Joseph", "Isabel", "Tony", "Cristina", "Marco", "Elena"]

#CREACIÓN DE INSTANCIAS DE CLASE
users = [User(name) for name in users_list]
jesus, sara, luis, ana, kevin, sandra, pedro, megan, victor, paula, \
miguel, silvia, pablo, rocio, joseph, isabel, tony, cristina, marco, elena = users

#CREACIÓN DE MENSAJES
jesus.create_post(f"Este es el primer mensaje de {jesus.name}")
jesus.create_post(f"Este es el segundo mensaje de {jesus.name}")
sara.create_post(f"Este es el primer mensaje de {sara.name}")
pedro.create_post(f"Este es el primer mensaje de {pedro.name}")
kevin.create_post(f"Este es el primer mensaje de {kevin.name}")
sara.create_post(f"Este es el segundo mensaje de {sara.name}")
elena.create_post(f"Este es el primer mensaje de {elena.name}")
victor.create_post(f"Este es el primer mensaje de {victor.name}")
miguel.create_post(f"Este es el primer mensaje de {miguel.name}")
jesus.create_post(f"Este es el tercer mensaje de {jesus.name}")
paula.create_post(f"Este es el primer mensaje de {paula.name}")
marco.create_post(f"Este es el primer mensaje de {marco.name}")
joseph.create_post(f"Este es el primer mensaje de {joseph.name}")
paula.create_post(f"Este es el segundo mensaje de {paula.name}")
cristina.create_post(f"Este es el primer mensaje de {cristina.name}")
isabel.create_post(f"Este es el primer mensaje de {isabel.name}")

#CREACIÓN DE USUARIOS SEGUIDOS
jesus.following(luis, ana, rocio)
sara.following(pedro)
cristina.following(victor, jesus, paula, joseph)
ana.following(pedro, elena, joseph)
victor.following(jesus, paula, tony, pablo)
rocio.following(megan, pedro, paula)
isabel.following(kevin, marco, victor, cristina, paula)
elena.following(paula, isabel, kevin, joseph)
marco.following(cristina, elena, megan, jesus)
megan.following(pedro, joseph, tony, cristina)
kevin.following(marco, miguel, elena, pablo, jesus)

#EL USUARIO jesus INTENTA BORRAR UNA PUBLICACIÓN INEXISTENTE CON ID 4
jesus.delete_post(4)

#EL USUARIO jesus BORRA SU SEGUNDA PUBLICACIÓN CON ID 2
jesus.delete_post(2)
jesus.show_user_profile()

#LA USUARIA ISABEL INTENTA DEJAR DE SEGUIR A jesus AL QUE NO SEGUÍA ANTERIORMENTE
isabel.unfollow(jesus)

#LA USUARIA ISABEL DEJA DE SEGUIR A VICTOR
victor.show_user_profile()
isabel.unfollow(victor)
isabel.show_user_profile()
victor.show_user_profile()               #arreglar bug, no bajan los seguidores

#CREACIÓN DE VARIOS LIKES A MENSAJES CONCRETOS POR SU ID
cristina.liked_post(jesus, 1)
elena.liked_post(jesus, 1)
isabel.liked_post(victor, 1)
kevin.liked_post(jesus, 1)
megan.liked_post(jesus, 3)
cristina.liked_post(jesus, 1)

#jesus INTENTA DAR LIKE A UN MENSAJE DE JOSEPH QUE NO EXISTE
jesus.liked_post(joseph, 2)

#LA USUARIA cristina QUITA EL LIKE AL MENSAJE CON ID1 DE jesus
cristina.unliked_post(jesus, 1)

#LA USUARIA cristina INTENTA QUITAR UN LIKE A UN MENSAJE QUE NO HABÍA DADO LIKE ANTES
cristina.unliked_post(joseph, 1)

#MUESTRA DE PERFIL COMPLETO DE VARIOS USUARIOS
jesus.show_user_profile()
sara.show_user_profile()
megan.show_user_profile()
pedro.show_user_profile() 
kevin.show_user_profile()
marco.show_user_profile()
victor.show_user_profile()
elena.show_user_profile()
cristina.show_user_profile()
isabel.show_user_profile()



