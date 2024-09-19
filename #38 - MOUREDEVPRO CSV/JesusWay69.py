import os, platform, csv, random

if (platform.platform().startswith("macOS") or platform.platform().startswith("Linux")):
    os.system('clear')
else:
    os.system('cls')

""" * EJERCICIO:
 * He presentado mi proyecto más importante del año: mouredev pro.
 * Un campus para la comunidad, que lanzaré en octubre, donde estudiar
 * programación de una manera diferente.
 * Cualquier persona suscrita a la newsletter de https://mouredev.pro
 * accederá a sorteos mensuales de suscripciones, regalos y descuentos.
 *
 * Desarrolla un programa que lea los registros de un fichero .csv y
 * seleccione de manera aleatoria diferentes ganadores.
 * Requisitos:
 * 1. Crea un .csv con 3 columnas: id, email y status con valor "activo"
 *    o "inactivo" (y datos ficticios).
 *    Ejemplo: 1 | test@test.com | activo
 *             2 | test2@test.com | inactivo
 *    (El .csv no debe subirse como parte de la corrección)
 * 2. Recupera los datos desde el programa y selecciona email aleatorios.
 * Acciones:
 * 1. Accede al fichero .csv y selecciona de manera aleatoria un email
 *    ganador de una suscripción, otro ganador de un descuento y un último
 *    ganador de un libro (sólo si tiene status "activo" y no está repetido).
 * 2. Muestra los emails ganadores y su id.
 * 3. Ten en cuenta que la primera fila (con el nombre de las columnas)
 *    no debe tenerse en cuenta."""

my_file = "#38 - MOUREDEVPRO CSV/newsletter_users.csv"
columns = ['id', 'email', 'activo']
users = [{'id':1, 'email':'supermario@mouredev.com', 'activo':True},
         {'id':2, 'email':'darkvader@mouredev.com', 'activo':True},
         {'id':3, 'email':'pikachu@mouredev.com', 'activo':True},
         {'id':4, 'email':'joseluistorrente@mouredev.com', 'activo':True},
         {'id':5, 'email':'homersimpson@mouredev.com', 'activo':True},
         {'id':6, 'email':'mickeymouse@mouredev.com', 'activo':True},
         {'id':7, 'email':'sansastark@mouredev.com', 'activo':True},
         {'id':8, 'email':'fionagalagher@mouredev.com', 'activo':True},
         {'id':9, 'email':'michaelscott@mouredev.com', 'activo':True},
         {'id':10, 'email':'sheldoncooper@mouredev.com', 'activo':True},
         {'id':11, 'email':'spiderman@mouredev.com', 'activo':True},
         {'id':12, 'email':'walterwhite@mouredev.com', 'activo':True},
         {'id':13, 'email':'petergriffin@mouredev.com', 'activo':True},
         {'id':14, 'email':'rachelgreen@mouredev.com', 'activo':True},
         {'id':15, 'email':'jessicajones@mouredev.com', 'activo':True},
         {'id':16, 'email':'ricksanchez@mouredev.com', 'activo':True},
         {'id':17, 'email':'maxrockatansky@mouredev.com', 'activo':True},
         {'id':18, 'email':'hackerman@mouredev.com', 'activo':True},
         {'id':19, 'email':'elliotalderson@mouredev.com', 'activo':True},
         {'id':20, 'email':'jesusway69@mouredev.com', 'activo':True},]

def create_csv(users:list):
    with open(my_file, mode='w', newline='') as file:
        writer = csv.DictWriter(file, delimiter = ';', fieldnames = columns )
        writer.writeheader()
        for user in users:
           writer.writerow(user)
    

#create_csv(users)

def read_list_csv():
    with open(my_file) as file:
        content_list_csv = csv.reader(file, delimiter=';')
        next(content_list_csv)
        for row in content_list_csv:
            print('El email es:', row[1])
read_list_csv()

def read_dict_csv():

    with open(my_file) as file:
        content_dict_csv = csv.DictReader(file, delimiter=';')
        for row in content_dict_csv:
            print('El email es:', row['email'])
read_dict_csv()

def lottery():
    with open('#38 - MOUREDEVPRO CSV/newsletter_users.csv') as file:
        content_dict_csv = csv.DictReader(file, delimiter=';')
        content_list_csv = list(content_dict_csv)
        winner_num = random.choice(content_list_csv)
        winner_num['activo'] = False
        print(winner_num['email'])
        print(winner_num['activo'])
    create_csv(content_list_csv)
        







#ejemplos: https://pywombat.com/articles/archivos-csv-python