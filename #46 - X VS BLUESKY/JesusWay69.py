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
auto_increment_likes=0
class User:
    auto_increment_user_id = 0
    
    def __init__(self, name):
        self.name = name  
        User.auto_increment_user_id += 1
        self.auto_increment_likes = 0
        self.id = User.auto_increment_user_id
        self.user_posts = {}
        self.user_post_liked = []
        self.index_message = 0
        self.follow = ()

    def create_Post(self, message):
        self.message = message
        if (len(self.message)>200):
            print("No se puede crear un post de más de 200 caracteres")
        else:
            self.index_message +=1
            self.user_posts[str(self.index_message)] = message

    def following(self, follow = ()):
        self.follow = follow
        return self.follow
    
    def unfollow(self, user):
        self.user_unfollow = user
        user_follow_list = list(self.follow)
        if self.user_unfollow in user_follow_list:
            user_follow_list.remove(self.user_unfollow)
            self.follow = tuple(user_follow_list)
            print(f"{self.name} ha dejado de seguir a {self.user_unfollow.name}")
        else:
            print(f"{self.name} no puede dejar de seguir a {self.user_unfollow.name} porque no lo estaba siguiendo anteriormente")

    def show_posts(self):
        print(f"Mensajes de {self.name}:")
        [print("-", v, ", creado el", '{}/{}/{}'.format(DT.now().day,DT.now().month,DT.now().year),
                "message id:", k) for k, v in reversed(self.user_posts.items())]
        
    def show_user_profile(self):
        users_following = self.following(self.follow)
        print()
        print(f"INFORMACIÓN DE USUARIO\n -------------------\nUsername: {self.name}\nUserID: {self.id}")
        print(f"Siguiendo a:")
        for follower in users_following:
            print("-",follower.name)
        self.show_posts()    
        print()
        
    def delete_post(self, messageID):
        self.messageID = messageID
        if str(self.messageID) not in self.user_posts:
            print(f"El usuario {self.name} no tiene ningún mensaje con id {self.messageID}")
        else:
            del(self.user_posts[str(self.messageID)])
    
def liked_post(follower, user, postId):
        message = user.user_posts[str(postId)]
        likes:int =1

        message_profile = [follower.name, postId, user.name, message, likes]
        if message_profile[4] == len(user.user_post_liked):
            message_profile = [follower.name, postId, user.name, message, likes +1]
        user.user_post_liked.append(message_profile)
        print(f"{follower.name} ha dado like al mensaje con id:{message_profile[1]} de {user.name}",
              f", el mensaje de {user.name} '{message_profile[3]}' acumula {message_profile[4]}"
               , "like" if message_profile[4] == 1 else "likes")
        #print(user.user_post_liked) 

#LISTA DE USUARIOS
users_list = ["Manolo", "Sara", "Luis", "Ana", "Kevin", "Sandra", "Pedro", "Megan", "Victor", "Paula",
               "Miguel", "Silvia", "Pablo", "Rocío", "Joseph", "Isabel", "Tony", "Cristina", "Marco", "Elena"]

#CREACIÓN DE INSTANCIAS DE CLASE
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
manolo.create_Post(f"Este es el primer mensaje de {manolo.name}")
manolo.create_Post(f"Este es el segundo mensaje de {manolo.name}")
sara.create_Post(f"Este es el primer mensaje de {sara.name}")
pedro.create_Post(f"Este es el primer mensaje de {pedro.name}")
kevin.create_Post(f"Este es el primer mensaje de {kevin.name}")
sara.create_Post(f"Este es el segundo mensaje de {sara.name}")
victor.create_Post(f"Este es el primer mensaje de {victor.name}")
miguel.create_Post(f"Este es el primer mensaje de {miguel.name}")
manolo.create_Post(f"Este es el tercer mensaje de {manolo.name}")
paula.create_Post(f"Este es el primer mensaje de {paula.name}")
marco.create_Post(f"Este es el primer mensaje de {marco.name}")
joseph.create_Post(f"Este es el primer mensaje de {joseph.name}")
paula.create_Post(f"Este es el segundo mensaje de {paula.name}")
isabel.create_Post(f"Este es el primer mensaje de {isabel.name}")

#CREACIÓN DE USUARIOS SEGUIDOS
manolo.following((luis, ana))
sara.following((pedro,))
ana.following((pedro, elena, joseph))
victor.following((manolo, paula, tony, pablo))
rocio.following((megan, pedro, paula))
isabel.following((kevin, marco, victor, cristina, paula))

#MUESTRA DE PERFIL COMPLETO DE VARIOS USUARIO
manolo.show_user_profile()
sara.show_user_profile()
megan.show_user_profile()
pedro.show_user_profile()
kevin.show_user_profile()
marco.show_user_profile()
victor.show_user_profile()
elena.show_user_profile()
cristina.show_user_profile()
isabel.show_user_profile()

#EL USUARIO MANOLO INTENTA BORRAR UNA PUBLICACIÓN INEXISTENTE CON ID 4
manolo.delete_post(4)
#EL USUARIO MANOLO BORRA SU SEGUNDA PUBLICACIÓN CON ID 2
manolo.delete_post(2)
manolo.show_user_profile()
#LA USUARIA ISABEL INTENTA DEJAR DE SEGUIR A MANOLO AL QUE NO SEGUÍA ANTERIORMENTE
isabel.unfollow(manolo)
#LA USUARIA ISABEL DEJA DE SEGUIR A VICTOR
isabel.unfollow(victor)
isabel.show_user_profile()
#CREACIÓN DE VARIOS LIKES A MENSAJES CONCRETOS POR SU ID
liked_post(cristina, manolo, 1)
liked_post(elena, manolo, 1)
liked_post(isabel, victor, 1)
liked_post(megan, manolo, 3)

#print (manolo.user_posts.get('1'))





