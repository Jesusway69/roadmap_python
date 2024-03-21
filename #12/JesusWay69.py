import os, json
import xml.etree.cElementTree as ET
from xml.dom import minidom
os.system('cls')
"""
 * IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.
 *
 * EJERCICIO:
 * Desarrolla un programa capaz de crear un archivo XML y JSON que guarde los
 * siguientes datos (haciendo uso de la sintaxis correcta en cada caso):
 * - Nombre
 * - Edad
 * - Fecha de nacimiento
 * - Listado de lenguajes de programación
 * Muestra el contenido de los archivos.
 * Borra los archivos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la lógica de creación de los archivos anteriores, crea un
 * programa capaz de leer y transformar en una misma clase custom de tu 
 * lenguaje los datos almacenados en el XML y el JSON.
 * Borra los archivos.
"""

	
ruta = r"C:\Users\jesus\Documents\Python3project\roadmap_python\#12"


def console(elem):
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")


equipos = ET.Element("equipos")

comunidad = ET.SubElement(equipos, "ciudad")
ET.SubElement(comunidad, "Madrid").text = "Real Madrid"
ET.SubElement(comunidad, "Madrid").text = "Atlético Madrid"
ET.SubElement(comunidad, "Valencia").text = "Valencia cf"
ET.SubElement(comunidad, "Valencia").text = "Villarreal"

file = ET.ElementTree(equipos)
file.write(ruta+ "equipos.xml")

print (console(equipos))



json_file = '''{
 "nombre": "Jesus",
 "fecha de nacimiento": "26/12/1794",
 "lenguages": ["python", "java", "php"]
}
'''
yo = json.loads(json_file)
print(yo)
print(type(yo))

python_dict = {
 "nombre": "Jesus",
 "fecha de nacimiento": "26/12/1794",
 "lenguajes": ["python", "java", "php"]
}

yo = json.dumps(python_dict)
print(yo)
print(type(yo))

class Programador:
    def __init__(self, name, birth_date, languages):
        self.name = name
        self.birth_date = birth_date
        self.languages = languages
programador = Programador("Jesus", "26/12/1794", ["python", "java", "php"])
data = json.dumps(programador.__dict__)
print(data)
print(type(data))

object = [{"nombre": "jesus", "fecha de nacimiento": "26/12/1794", "lenguajes": ["python", "java", "php"]},
           {"nombre": "sara", "fecha de nacimiento": "14/05/1990", "lenguajes": ["kotlin", "javascript", "rust"]}]


with open('programadores.json', 'w') as f:
  json.dump(object, f, indent=4, sort_keys=False)





