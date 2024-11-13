import os, platform, git
from datetime import datetime as DT

if (platform.platform().startswith("macOS") or platform.platform().startswith("Linux")):
    os.system('clear')
else:
    os.system('cls')

"""* EJERCICIO:
 * ¡Me voy de viaje al GitHub Universe 2024 de San Francisco!
 *
 * Desarrolla un CLI (Command Line Interface) que permita
 * interactuar con Git y GitHub de manera real desde terminal.
 *
 * El programa debe permitir las siguientes opciones:
 * 1. Establecer el directorio de trabajo
 * 2. Crear un nuevo repositorio
 * 3. Crear una nueva rama
 * 4. Cambiar de rama
 * 5. Mostrar ficheros pendientes de hacer commit
 * 6. Hacer commit (junto con un add de todos los ficheros)
 * 7. Mostrar el historial de commits
 * 8. Eliminar rama
 * 9. Establecer repositorio remoto
 * 10. Hacer pull
 * 11. Hacer push
 * 12. Salir"""


path = r"C:\Users\jesus\Documents\Python3project\GitProjectPython\\"
repo_url = 'https://github.com/Jesusway69/GitProjectPython'

def git_init(local_path):
    if os.path.exists(local_path):
        repo = git.Repo.init(local_path)
    else:
        print("la ruta especificada no existe en este ordenador")
        return
    return repo

def git_clone(github_url, local_path):
    if not os.path.exists(local_path):
        repo = git.Repo.clone_from(github_url, local_path)
    else:
        repo = git.Repo(path)
    return repo

def git_branch(repo, branch_name):
    repo.git.branch(branch_name)
    print("Nueva rama creada: ", branch_name)
    

def git_checkout(repo):
    print("Ramas actuales en este repositorio:")
    print(repo.git.branch())
    branch_name = input("Escriba el nombre de la rama a la que quiere cambiar (con asterisco la actual):")
    repo.git.checkout(branch_name)


def git_add(repo):
    repo.git.add('.')

def git_commit(repo):
    message = input("Introduzca el mensaje del commit: ")
    current_date = '{}{}{}'.format(DT.now().year, DT.now().month, DT.now().day)
    repo.index.commit(str(current_date) + " " + message) #revisar esto, devuellve string not callable

def modify_repository(local_path):
    current_datetime = DT.now()
    with open(f'{local_path}/file1.txt', 'a') as f:
        f.writelines(f'\nañadimos otra línea el {current_datetime}')

def git_status(repo):
    print (repo.git.status())

def git_log(repo):
    print(repo.git.log())

my_repo = git_init(path)


while True:
    print("""
    1- Crear repositorio local
    2- Clonar repositorio desde Github
    3- Crear nueva rama
    4- Cambiar de rama
    5- Mostrar cambios no añadidos a stage
    6- Añadir todos los cambios a stage
    7- Hacer commit del repositorio
    8- Mostrar historial de commits
    9- Establecer repositorio remoto
    10- Actualizar repositorio local desde remoto (pull)
    11- Subir cambios locales a remoto (push)""")

    choice = input("Selecciona una opción del 1 al 12: ")

    match choice:
        case "1":
            git_init(path)
        case "2":
            git_clone(repo_url, path)
        case "3":
            git_branch(my_repo, "nueva_rama")
        case "4":
            git_checkout(my_repo)
        case "5":
            git_status()
        case "6":
            git_add(my_repo)
        case "7":
            git_commit(my_repo)
        case "8":
            git_log(my_repo)
        case "9":
            pass
        case "10":
            pass
        case "11":
            pass
        case "12":
            print("Saliendo...")
            break
        case _:
            print("Opción no válida.")