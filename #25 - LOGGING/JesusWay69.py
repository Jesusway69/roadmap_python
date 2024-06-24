import os, platform,logging, sys



if (platform.platform().startswith("macOS") or platform.platform().startswith("Linux")):
    os.system('clear')
else:
    os.system('cls')

""" * EJERCICIO:
 * Explora el concepto de "logging" en tu lenguaje. Configúralo y muestra
 * un ejemplo con cada nivel de "severidad" disponible.
 *
"""

#NONSET = 0
#DEBUG = 10
#INFO = 20
#WARNING = 30
#ERROR = 40
#CRITICAL = 50

LEVELS = {
	'notset': logging.NOTSET,
    'debug': logging.DEBUG,
    'info': logging.INFO,
    'warning': logging.WARNING,
    'error': logging.ERROR,
    'critical': logging.CRITICAL,
}

 
level = LEVELS.get('nonset', 0)
    

logging.basicConfig(
	
    
	#filename="#25.log",
	#filemode= "a",
	encoding="utf-8",
	level=level,
	format="%(asctime)s,%(msecs)1d - %(levelname)s %(message)s",
	datefmt='%d-%B-%Y,%H:%M:%S'
	
)


def division(a:int, b:int)->int:
	try:
		result = round((a / b),2)
		logging.info(f"División de {a} entre {b}. Resultado: {result} , operación correcta")
		
	except ZeroDivisionError as zero:
		result = None
		logging.error(zero)
	except TypeError as type:
		result = None
		logging.error(type)

	return result

def to_upper(text:str)->str:
	try:
		text = text*2
		text = text.upper()
		
		logging.info(text)
	except ValueError as val:
		text = None
		logging.warning(val)
	except Exception as ex:
		text = None
		logging.warning(ex)
	
	return text
def show_element(my_list:list,index:int)->int:
	try:
		num = my_list[index]
		logging.info(f"El índice {index} de la lista {my_list} es {num}")
	except IndexError as indexerr:
		num = None
		logging.critical(indexerr)
	
    

# try:
# 	division(8, 3)
# 	division(2, 0)
# 	division(9, "3")
# 	print()
# 	show_element([1,2,3],2)
# 	show_element([1,2,3],3)
# 	print()
# 	to_upper(45)
# 	to_upper("Hola Python ")
# 	to_upper("Hola", "Python")
	
	
	
# except Exception as ex:
# 	logging.warning(ex)
# 	print("excepción general")
# logging.info(f"Runnig at: {platform.platform()} with Python {platform.python_version()}")





""" * DIFICULTAD EXTRA (opcional):
 * Crea un programa ficticio de gestión de tareas que permita añadir, eliminar
 * y listar dichas tareas.
 * - Añadir: recibe nombre y descripción.
 * - Eliminar: por nombre de la tarea.
 * Implementa diferentes mensajes de log que muestren información según la
 * tarea ejecutada (a tu elección).
 * Utiliza el log para visualizar el tiempo de ejecución de cada tarea."""


tasks = {}

def add_task(name:str,description:str):
	tasks[name]= description
	logging.info(f"La tarea {name} se ha añadido correctamente\n")

def show_tasks():
	[print("Tarea: ", k ,"- Descripción: ", v , end = '\n') for k,v in tasks.items()]
print()
	
def delete_task(name:str):
	if name in tasks:
		tasks.pop(name)
		logging.info(f"La tarea {name} ha sido eliminada correctamente\n")
	else:
		logging.warning(f"Tarea {name} no encontrada\n")



while True:
	option = input("-1 Mostrar tareas \n-2 Añadir tarea \n-3 Borrar tarea \n-4 Salir\nSeleccione una opción: ")
	if not option.isdigit():
		logging.error(": Sólo se pueden introducir caracteres numéricos, intente de nuevo\n")
	elif int(option)<1 or int(option)>4:
		logging.warning(": El número no debe ser diferente a las opciones mostradas, intente de nuevo\n")
	else:	
		option = int(option)

		if option == 1:
			logging.debug("listado de tareas:")
			show_tasks()
			continue
		elif option == 2:
			task_name = input("Escriba el nombre de la tarea: ")
			task_desc = input("Describa la tarea: ")
			add_task(task_name,task_desc)
			continue
		elif option == 3:
			task_name = input("Escriba el nombre de la tarea a borrar: ")
			delete_task(task_name)
			continue
		elif option == 4:
			logging.warning(": Está saliendo del programa")
			break
		
		