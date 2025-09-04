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
 * - Posibilidad de hacer like (y eliminarlo) en un post.
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
        self.user_post_liked = []
        self.index_message = 0
        self.follow = ()

    def create_post(self, message):
        if (len(message) > 200):
            print("No se puede crear un post de más de 200 caracteres")
        else:
            self.index_message +=1
            self.user_posts[str(self.index_message)] = message

    def following(self, follow = ()):
        self.follow = follow
        return self.follow
    
    def unfollow(self, user):
        #self.user_unfollow = user
        user_follow_list = list(self.follow)
        if user in user_follow_list:
            user_follow_list.remove(user)
            self.follow = tuple(user_follow_list)
            print(f"{self.name} ha dejado de seguir a {user.name}")
        else:
            print(f"{self.name} no puede dejar de seguir a {user.name} porque no lo estaba siguiendo anteriormente")

    def show_posts(self):
        print(f"Mensajes de {self.name}:")
        [print("-", v, ", creado el", '{}/{}/{}'.format(DT.now().day,DT.now().month,DT.now().year),
                "message id:", k) for k, v in reversed(self.user_posts.items())]
        
    def show_user_profile(self):
        users_following = self.follow
        print()
        print(f"INFORMACIÓN DE USUARIO\n -------------------\nUsername: {self.name}\nUserID: {self.id}\nSiguiendo a:")
        for follower in users_following:
            print("-",follower.name)
        self.show_posts()    
        print()
        
    def delete_post(self, messageID):
        #self.messageID = messageID
        if str(messageID) not in self.user_posts:
            print(f"El usuario {self.name} no tiene ningún mensaje con id {messageID}")
        else:
            del(self.user_posts[str(messageID)])
    

def liked_post(follower: User, user: User, postId: int):
    print("---------------------------\n")

    if str(postId) not in user.user_posts:
        print(f"El usuario {user.name} no tiene ningún mensaje con id {postId}\n")
        return

    message = user.user_posts[str(postId)]

    for like_sublist in user.user_post_liked:
        if like_sublist[0] == follower.name and like_sublist[1] == postId and like_sublist[2] == user.name:
            print(f"{follower.name} no puede dar like al mensaje '{message}' porque ya le dio like antes\n")
            return

    user.user_post_liked.append([follower.name, postId, user.name, message])
    likes_counter = sum(1 for like in user.user_post_liked if like[3] == message)

    print(f"{follower.name} ha dado like al mensaje con id:{postId} de {user.name}"
          f", el mensaje de {user.name} '{message}' acumula {likes_counter} {'like' if likes_counter == 1 else 'likes'}\n")


def unliked_post(follower:User, user:User, postId:int):
    print("---------------------------")
    print()
    
    if len(user.user_post_liked) == 0 or str(postId) not in user.user_posts:
        print(f"el usuario {user.name} no tiene ningún mensaje con id {postId}")
        print()
        return
    else:
        message = user.user_posts[str(postId)]
        for like_sublist in user.user_post_liked:
            if message and follower in like_sublist :
                user.user_post_liked.remove(like_sublist)
                likes_counter = sum(1 for sub_list in user.user_post_liked for element in sub_list if element == message)
                print(f"{follower.name} ha quitado el like al mensaje con id:{postId} de {user.name}"
                f", el mensaje de {user.name} '{message}' acumula {likes_counter}{'like' if likes_counter == 1 else 'likes'}\n")
                return
  
            
#LISTA DE USUARIOS
users_list = ["Jesus", "Sara", "Luis", "Ana", "Kevin", "Sandra", "Pedro", "Megan", "Victor", "Paula",
               "Miguel", "Silvia", "Pablo", "Rocío", "Joseph", "Isabel", "Tony", "Cristina", "Marco", "Elena"]

#CREACIÓN DE INSTANCIAS DE CLASE
jesus = User(users_list[0])
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
silvia = User(users_list[11])
pablo = User(users_list[12])
rocio = User(users_list[13])
joseph = User(users_list[14])
isabel = User(users_list[15])
tony = User(users_list[16])
cristina = User(users_list[17])
marco = User(users_list[18])
elena = User(users_list[19])

#CREACIÓN DE MENSAJES
jesus.create_post(f"Este es el primer mensaje de {jesus.name}")
jesus.create_post(f"Este es el segundo mensaje de {jesus.name}")
sara.create_post(f"Este es el primer mensaje de {sara.name}")
pedro.create_post(f"Este es el primer mensaje de {pedro.name}")
kevin.create_post(f"Este es el primer mensaje de {kevin.name}")
sara.create_post(f"Este es el segundo mensaje de {sara.name}")
victor.create_post(f"Este es el primer mensaje de {victor.name}")
miguel.create_post(f"Este es el primer mensaje de {miguel.name}")
jesus.create_post(f"Este es el tercer mensaje de {jesus.name}")
paula.create_post(f"Este es el primer mensaje de {paula.name}")
marco.create_post(f"Este es el primer mensaje de {marco.name}")
joseph.create_post(f"Este es el primer mensaje de {joseph.name}")
paula.create_post(f"Este es el segundo mensaje de {paula.name}")
isabel.create_post(f"Este es el primer mensaje de {isabel.name}")

#CREACIÓN DE USUARIOS SEGUIDOS
jesus.following((luis, ana))
sara.following((pedro,))
ana.following((pedro, elena, joseph))
victor.following((jesus, paula, tony, pablo))
rocio.following((megan, pedro, paula))
isabel.following((kevin, marco, victor, cristina, paula))

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

#EL USUARIO jesus INTENTA BORRAR UNA PUBLICACIÓN INEXISTENTE CON ID 4
jesus.delete_post(4)
#EL USUARIO jesus BORRA SU SEGUNDA PUBLICACIÓN CON ID 2
jesus.delete_post(2)
jesus.show_user_profile()
#LA USUARIA ISABEL INTENTA DEJAR DE SEGUIR A jesus AL QUE NO SEGUÍA ANTERIORMENTE
isabel.unfollow(jesus)
#LA USUARIA ISABEL DEJA DE SEGUIR A VICTOR
isabel.unfollow(victor)
isabel.show_user_profile()
#CREACIÓN DE VARIOS LIKES A MENSAJES CONCRETOS POR SU ID
liked_post(cristina, jesus, 1)
liked_post(elena, jesus, 1)
liked_post(isabel, victor, 1)
liked_post(kevin, jesus, 1)
liked_post(megan, jesus, 3)
liked_post(cristina, jesus, 1)
liked_post(jesus, joseph, 2)
#LA USUARIA cristina QUITA EL LIKE AL MENSAJE CON ID1 DE jesus
unliked_post(cristina, jesus, 1)






