import os, json
import xml.etree.cElementTree as ET
from xml.dom import minidom
from datetime import datetime as date
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
"""

	
ruta = r"C:\Users\jesus\Documents\Python3project\roadmap_python\#12\\"


def console(elem):
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ", newl="\n")

nacimiento = 1975
edad = date.now().year - nacimiento

empresa = ET.Element("EMPRESA")

programador = ET.SubElement(empresa, "PROGRAMADOR")
ET.SubElement(programador, "NOMBRE").text = "Jesus"
ET.SubElement(programador, "LENGUAJES").text = "[Python, Java, PhP]"
ET.SubElement(programador, "NACIMIENTO").text = str(nacimiento)
ET.SubElement(programador, "EDAD").text = str(edad)
programador = ET.SubElement(empresa, "PROGRAMADOR")
ET.SubElement(programador, "NOMBRE").text = "Sandra"
ET.SubElement(programador, "LENGUAJES").text = "[Javascript, HTML, CSS]"
ET.SubElement(programador, "NACIMIENTO").text = "1991"
ET.SubElement(programador, "EDAD").text = str(date.now().year - 1991)

file = ET.ElementTree(empresa)
file.write(ruta + "empresa.xml")

print (console(empresa))


json_file = '''{
 "nombre": "Jesus",
 "fecha de nacimiento": "1975",
 "lenguages": ["python", "java", "php"] 
}
'''
#string

yo = json.loads(json_file)#Transforma un string con formato json en un objeto diccionario python
print(yo)
print(type(yo))#dict

python_dict = {
 "nombre": "Jesus",
 "fecha de nacimiento": "1974",
 "lenguajes": ["python", "java", "php"]
}#dict

yo = json.dumps(python_dict)#Transforma un objeto diccionario python en un string
print(yo)
print(type(yo))#str












"""
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la lógica de creación de los archivos anteriores, crea un
 * programa capaz de leer y transformar en una misma clase custom de tu 
 * lenguaje los datos almacenados en el XML y el JSON.
 * Borra los archivos.
"""

class Programador:
    def __init__(self):
       pass 

    def create_dict(self, name:str, birth_year:int, languages:list):
        self.name = name
        self.birth_year = birth_year
        self.languages = languages
        dict = {"Name":self.name,
                "Birth year":self.birth_year,
                "Age": date.now().year - self.birth_year, 
                "Languages": self.languages}
        return dict


programador = Programador()
programador1 = programador.create_dict("Jesus", 1975, ["python", "java", "php"])
programador2 = programador.create_dict("Sandra", 1991, ["HTML", "CSS", "Javascript"])
programador3 = programador.create_dict("Pepe",1980, ["C#", "C", "Assembly"])
primary_list = [programador1,programador2,programador3]






with open('programadores.json', 'w') as create_write:
  json.dump(primary_list, create_write, indent=4, sort_keys=False, )

with open('programadores.json') as contains:
   payload = json.load(contains)
   for element in  payload:
      print(element)


