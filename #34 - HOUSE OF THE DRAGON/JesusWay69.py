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


    
def create_dict(id:int, name:str, spouse:str="", children:list=[])->dict:
    character:dict = {}
    character_value:dict = {}
    character[id] = character_value
    character_value["Nombre"] = name
    character_value["Pareja"] = spouse
    character_value["Hijos"] = children
    return character

def print_json_contain(file:str):
        with open(file) as contains:
            json_load:list = json.load(contains)
        for element in  json_load:
            print(element)

def get_json_contain(file:str)->list:
    with open(file, 'r') as contains:
            json_load = json.load(contains)
    return json_load

def create_file_json(file:str):
        with open(file, 'w') as create_json:
           json.dump(file,create_json, indent=4, sort_keys=False)

def print_family_tree(file:str):
    with open(file) as contains:
        json_load:list = json.load(contains)
    for i in range(len(json_load)):
        name = list(json_load[i].values())[0]["Nombre"]
        spouse = list(json_load[i].values())[0]["Pareja"]
        children = list(json_load[i].values())[0]["Hijos"]
        print(f"\n---- Nombre: {name} ---------------------- Pareja: {spouse} -----")
        print("-------Hijos: ",end='------')
        for j in range(len(children)):
            child = children[j]
            if j < len(children)-1:
                print(f"\b{child}", end=',  ')
            else:
                print(f"\b\b {child}")
        





my_path:str = r"C:\Users\jesus\Documents\Python3project\roadmap_python\#34 - HOUSE OF THE DRAGON\\"
file:str = my_path + "family_tree.json"
#create_file_json(file)
json_root:list = []
while True:
    print("""\nElija una opción:
          1 - Añadir personaje
          2 - Eliminar personaje
          3 - Modificar pareja
          4 - Añadir hijo
          5 - Imprimir árbol genealógico y salir
""")
    
    option = int(input("Introduzca un número del 1 al 5: "))
    match option: 
        
        case 1: 
            json_root:list = get_json_contain(file)#si pongo esto aquí se cae con archivo vacío
            if len(json_root)>0: 
                #json_root:list = get_json_contain(file)  si lo pongo aquí lo inicia bien incluso vacío pero lo machaca cada vez que se ejecuta de nuevo para añadir
                last_dict:dict = json_root[len(json_root)-1] 
                print(last_dict)
                list_key = list(last_dict.keys())
                id = int(list_key[0])
            else:
                id=0
                create_file_json(file)
            children =[]
            id +=1
            name:str = input("Escriba el nombre del personaje: ").title()
            spouse:str = input("Escriba el nombre de la pareja del personaje si tiene, si no pulse enter: ").title()
            son:str = None
            while son != "":
                son = input("Escriba el nombre de un hijo del personaje, si no tiene o ya ha escrito todos pulse enter: ").title()
                children.append(son)
                if son == "":
                    json_root.append(create_dict(id, name, spouse, children))
                    if spouse == "":
                        spouse = None
                    else:
                       json_root.append(create_dict(id+1, spouse, name, children)) 
                    del children[len(children)-1]
                    break
                else:
                   continue
            with open(file, 'w') as add_dict:
                json.dump(json_root, add_dict, indent=4, sort_keys=False)
            print_json_contain(file)
            

        case 2:
            id_del:str = input("escriba el id del personaje a eliminar: ")
            json_data:list = get_json_contain(file)                                                              
            for row in json_data:              
                if id_del in row:
                    json_data.remove(row)
                 
            with open(file, "w") as add_dict:
                json.dump(json_data, add_dict, indent=4, sort_keys=False)
                

        case 3:
            id_mod:str = input("Escriba el id del personaje cuya pareja se va a editar: ")
            json_data:list = get_json_contain(file)                               
            for row in json_data:              
                if id_mod in row:
                    print(f"La pareja actual de {row[id_mod]["Nombre"]} es {row[id_mod]["Pareja"]}")
                    new_spouse:str = input(f"Escriba el nombre de la nueva pareja de {row[id_mod]["Nombre"]}: ").capitalize()
                    row[id_mod]["Pareja"] = new_spouse
            with open(file, "w") as add_dict:
                json.dump(json_data, add_dict, indent=4, sort_keys=False)        
                    
        case 4:
            id_add_child:str = input("Escriba el id del personaje cuyo hijo se va a añadir: ")
            json_data:list = get_json_contain(file)                              
            for row in json_data:              
                if id_add_child in row:
                    print(f"Los hijos de {row[id_add_child]["Nombre"]} y {row[id_add_child]["Pareja"]} son {row[id_add_child]["Hijos"]}")
                    new_child = input(f"Escriba el nombre del nuevo/a hijo/a de {row[id_add_child]["Nombre"]} y {row[id_add_child]["Pareja"]}: ").capitalize()
                    row[id_add_child]["Hijos"].append(new_child)
            with open(file, "w") as add_dict:
                json.dump(json_data, add_dict, indent=4, sort_keys=False) 
        case 5:
            print_family_tree(file)
            break
        case _:
            print("Sólo se pueden introducir números del 1 al 5, intente de nuevo")
















    

        
# my_dict = {"ID":id,
#         "Nombre":name,
#         "Cónyuge":spouse,
#         "Hijos":children}
# return dict

# class Character:
#     def __init__(self, id, name) -> None:
#         self.id = id
#         self.name = name
#     def set_spouse(self, spouse):
#         self.spouse = spouse
#     def get_spouse(self):
#         return self.spouse
#     def set_children(self, *args):
#         self.args = args
#     def get_children(self):
#         return self.args