import os, platform, csv

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

columns = ['id', 'email', 'activo']
users = [{'id':1, 'email':'supermario@mouredev.com', 'activo':True},
         {'id':2, 'email':'darkvader@mouredev.com', 'activo':True},
         {'id':3, 'email':'pikachu@mouredev.com', 'activo':True},
         {'id':4, 'email':'manoloeldelbombo@mouredev.com', 'activo':True},
         {'id':5, 'email':'homersimpson@mouredev.com', 'activo':True},
         {'id':6, 'email':'mickeymouse@mouredev.com', 'activo':True},
         {'id':7, 'email':'sansastark@mouredev.com', 'activo':True},
         {'id':8, 'email':'fionagalagher@mouredev.com', 'activo':True},
         {'id':9, 'email':'michaelscott@mouredev.com', 'activo':True},
         {'id':10, 'email':'sheldoncooper@mouredev.com', 'activo':True},]

def create_csv():
    with open('#38 - MOUREDEVPRO CSV/newsletter_users.csv', mode='w', newline='') as file:
        writer = csv.DictWriter(file, delimiter= ';', fieldnames=columns )
        writer.writeheader()
        for user in users:
           writer.writerow(user)
    

#create_csv()

def read_csv():
    with open('#38 - MOUREDEVPRO CSV/newsletter_users.csv') as file:
        content_csv = csv.reader(file, delimiter=';')
        next(content_csv)
        for row in content_csv:
            print(row)
#read_csv()

def read_email():

    with open('#38 - MOUREDEVPRO CSV/newsletter_users.csv') as file:
        csv_reader = csv.DictReader(file, delimiter=';')

        for row in csv_reader:
            email = row['email']
            print('El email es:', email)
read_email()