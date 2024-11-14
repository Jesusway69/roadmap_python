import os, platform, git
from datetime import datetime as DT

import git.exc

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

def git_branch(repo):
    print("Ramas actuales en este repositorio:")
    print(repo.git.branch())
    branch_name = input("Escriba el nombre de la nueva rama a crear: ")
    try:
        repo.git.branch(branch_name)
        print("Nueva rama creada: ", branch_name)
    except git.exc.GitCommandError as err:
        print(f"\n {err} la rama {branch_name} ya existe")
    

def git_checkout(repo):
    print("Ramas actuales en este repositorio:")
    print(repo.git.branch())
    try:  
        branch_name = input("Escriba el nombre de la rama a la que quiere cambiar (con asterisco la actual): ")
        repo.git.checkout(branch_name)
    except git.exc.GitCommandError as err:
        print(f"\n {err} la rama {branch_name} no existe")


def git_add(repo):
    repo.git.add('.')

def git_commit(repo):
    message = input("Introduzca el mensaje del commit: ")
    current_date = '{}{}{}'.format(DT.now().year, DT.now().month, DT.now().day)
    repo.index.commit(str(current_date) + " " + message)

def modify_repository(local_path):
    current_datetime = DT.now()
    with open(f'{local_path}/file1.txt', 'a') as f:
        f.writelines(f'\nañadimos otra línea el {current_datetime}')

def git_status(repo):
    print (repo.git.status())

def git_log(repo):
    print(repo.git.log())

def git_remote_add(repo):
    try:
        remote_branch = input("Introduzca el nombre de la rama principal remota (origin por defecto pulsando enter): ")
        if len(remote_branch) == 0: remote_branch = 'origin'
        repo_url = input("Introduzca una url válida para crear repositorio remoto en github: ")
        repo.create_remote(remote_branch, repo_url)
    except git.exc.GitCommandError as err:
        print(f"\n {err} la url {repo_url} no existe o la rama remota ya existe")

my_repo = git_init(path)
#my_repo.remote().pull método para pull

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

    option = input("Selecciona una opción del 1 al 12: ")

    match option:
        case "1":
            git_init(path)
        case "2":
            git_clone(repo_url, path)
        case "3":
            git_branch(my_repo)
        case "4":
            git_checkout(my_repo)
        case "5":
            git_status(my_repo)
        case "6":
            git_add(my_repo)
        case "7":
            git_commit(my_repo)
        case "8":
            git_log(my_repo)
        case "9":
            git_remote_add(my_repo)
        case "10":
            pass
        case "11":
            pass
        case "12":
            print("Fin del programa")
            break
        case _:
            print("Opción no válida.")