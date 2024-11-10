import os, platform, git, datetime


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


def clone_repository(github_url, local_path):
    if not os.path.exists(local_path):
        repo = git.Repo.clone_from(github_url, local_path)
    else:
        repo = git.Repo(path)
    return repo

def add_stage(repo):
    repo.git.add('.')

def commit(repo):
    repo.index.commit(f'commit en {datetime.datetime.now()}')

def modify_repository(local_path):
    current_datetime = datetime.datetime.now()
    with open(f'{local_path}/file1.txt', 'a') as f:
        f.writelines(f'\nañadimos otra línea el {current_datetime}')
def show_status(repo):
    print (repo.git.status())

def show_log(repo):
    print(repo.git.log())


show_status(clone_repository(repo_url, path))
show_log(clone_repository(repo_url, path))

#modify_repository(path)

#commit(clone_repository(repo_url, path))
while True:


    choice = input("Selecciona una opción (1 al 12): ")

    match choice:
        case "1":
            pass
        case "2":
            pass
        case "3":
            pass
        case "4":
            pass
        case "5":
            pass
        case "6":
            pass
        case "7":
            pass
        case "8":
            pass
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