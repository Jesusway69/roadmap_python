import os, platform, json

if (platform.platform().startswith("macOS") or platform.platform().startswith("Linux")):
    os.system('clear')
else:
    os.system('cls')

    """ * EJERCICIO:
    * ¡La Casa del Dragón ha finalizado y no volverá hasta 2026!
    * ¿Alguien se entera de todas las relaciones de parentesco
    * entre personajes que aparecen en la saga?
    * Desarrolla un árbol genealógico para relacionarlos (o invéntalo).
    * Requisitos:
    * 1. Estará formado por personas con las siguientes propiedades:
    *    - Identificador único (obligatorio)
    *    - Nombre (obligatorio)
    *    - Pareja (opcional)
    *    - Hijos (opcional)
    * 2. Una persona sólo puede tener una pareja (para simplificarlo).
    * 3. Las relaciones deben validarse dentro de lo posible.
    *    Ejemplo: Un hijo no puede tener tres padres.
    * Acciones:
    * 1. Crea un programa que permita crear y modificar el árbol.
    *    - Añadir y eliminar personas
    *    - Modificar pareja e hijo
    * 2. Podrás imprimir el árbol (de la manera que consideres).
    * 
    * NOTA: Ten en cuenta que la complejidad puede ser alta si
    * se implementan todas las posibles relaciones. Intenta marcar
    * tus propias reglas y límites para que te resulte asumible."""


    
def create_dict(id:int, name:str, spouse:str="", sons:list=[])->dict:
    character = {}
    character_value = {}
    character[id] = character_value
    character_value["Nombre"] = name
    character_value["Cónyuge"] = spouse
    character_value["Hijos"] = sons
    return character

def print_json_contain(file:str):
        with open(file) as contains:
            payload = json.load(contains)
        for element in  payload:
            print(element)


my_path = r"C:\Users\jesus\Documents\Python3project\roadmap_python\#34 - HOUSE OF THE DRAGON\\"
file = my_path + "family_tree.json"
json_root = []
# with open(file, 'w') as create_json:
#     json.dump(file,create_json, indent=4, sort_keys=False)

while True:
    print("""Elija una opción:
          1 - Añadir personaje
          2 - Eliminar personaje
          3 - Modificar pareja
          4 - Modificar hijo
          5 - salir
""")
    
    option = int(input("Introduzca un número del 1 al 5: "))
    id = 0
    match option:
        case 1: 
            sons =[]
            id +=1
            name = input("Escriba el nombre del personaje: ").title()
            spouse = input("Escriba el nombre de la pareja del personaje si tiene, si no pulse enter: ").title()
            son = None
            while son != "":
                son = input("Escriba el nombre de un hijo del personaje, si no tiene o ya ha escrito todos pulse enter: ").title()
                sons.append(son)
                if son == "":
                    json_root.append(create_dict(id, name, spouse, sons))
                    if spouse == "":
                        spouse = None
                    else:
                       json_root.append(create_dict(id+1, spouse, name, sons))
                    del sons[len(sons)-1]
                    break
                else:
                   continue
            with open(file, 'w') as add_dict:
                json.dump(json_root, add_dict, indent=4, sort_keys=False)
            print_json_contain(file)
            

        case 2:
            id_del = input("escriba el id del personaje a eliminar: ")
            firstData  = json.load(open(file))
            print(firstData)
                                              
            for row in firstData:              
                if id_del in row:
                #if row.keys() == str(id_del):
                    del row
                          
            open(file, "w").write(
                json.dump(firstData, indent=4, sort_keys=False)
)
        case 3:
            pass
        case 4:
            pass
        case 5:
            break
        case _:
            print("Sólo se pueden introducir números del 1 al 5, intente de nuevo")
















    

        
# my_dict = {"ID":id,
#         "Nombre":name,
#         "Cónyuge":spouse,
#         "Hijos":sons}
# return dict

# class Character:
#     def __init__(self, id, name) -> None:
#         self.id = id
#         self.name = name
#     def set_spouse(self, spouse):
#         self.spouse = spouse
#     def get_spouse(self):
#         return self.spouse
#     def set_sons(self, *args):
#         self.args = args
#     def get_sons(self):
#         return self.args