import os, platform, logging

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