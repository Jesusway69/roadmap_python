<<<<<<< HEAD
 
import os, platform,logging, sys
=======
import os, platform, logging
>>>>>>> edb76652ffb463a46de0c14038889721d5363182

if (platform.platform().startswith("macOS") or platform.platform().startswith("Linux")):
    os.system('clear')
else:
    os.system('cls')

""" * EJERCICIO:
 * Explora el concepto de "logging" en tu lenguaje. Configúralo y muestra
 * un ejemplo con cada nivel de "severidad" disponible.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa ficticio de gestión de tareas que permita añadir, eliminar
 * y listar dichas tareas.
 * - Añadir: recibe nombre y descripción.
 * - Eliminar: por nombre de la tarea.
 * Implementa diferentes mensajes de log que muestren información según la
 * tarea ejecutada (a tu elección).
 * Utiliza el log para visualizar el tiempo de ejecución de cada tarea."""
<<<<<<< HEAD
#UNSET = 0
#DEBUG = 10
#INFO = 20
#WARNING = 30
#ERROR = 40
#CRITICAL = 50

logging.basicConfig(
	filename="#25.log",
	encoding="utf-8",
	level=logging.DEBUG,
	format="%(asctime)s %(levelname)s %(message)s",
	filemode= "a"
)


def division(a:int, b:int)->int:
	try:
		result = a / b
		logging.info(f"División de {a} entre {b}. Resultado: {result}")
		
	except ZeroDivisionError as zero:
		result = None
		logging.error(zero)
	except TypeError as type:
		result = None
		logging.error(type)
	else:
		logging.info("Operación correcta")

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
	except IndexError as inderr:
		num = None
		logging.critical(inderr)
	


try:
	# print(division(8, 3)) 
	# print(division(2, 0)) 
	# print(division(9, "3"))
	
	# to_upper(45)
	# to_upper("Hola Python ")
	# to_upper("Hola", "Python")
	show_element([1,2,3],3)
	
	
except Exception as ex:
	logging.warning(ex)
logging.info(f"Runnig at: {platform.platform()} with Python {platform.python_version()}")





# LEVELS = {
#     'debug': logging.DEBUG,
#     'info': logging.INFO,
#     'warning': logging.WARNING,
#     'error': logging.ERROR,
#     'critical': logging.CRITICAL,
# }

# if len(sys.argv) > 1:
#     level_name = sys.argv[1]
#     level = LEVELS.get(level_name, logging.NOTSET)
#     logging.basicConfig(level=level)

# logging.debug('This is a debug message')
# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical error message')

#https://rico-schmidt.name/pymotw-3/logging/index.html
=======

logging.basicConfig(
	filename="log-de-hoy.log",
	encoding="utf-8",
	level=logging.DEBUG,
	format="%(asctime)s %(levelname)s %(message)s"
)

def add(a, b):
	try:
		result = a / b
		logging.info(f"Adding {a} and {b}. Result: {result}")
	except ZeroDivisionError as zero:
		result = None
		logging.error(zero)
	return result

print(add(2, 3)) 
print(add(2, 0)) 
>>>>>>> edb76652ffb463a46de0c14038889721d5363182
