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

	
#ruta = r"C:\Users\jesus\Documents\Python3project\roadmap_python\\"


# def console(elem):
#     rough_string = ET.tostring(elem, 'utf-8')
#     reparsed = minidom.parseString(rough_string)
#     return reparsed.toprettyxml(indent="  ", newl="\n")

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
file.write("empresa.xml") #file.write(ruta + "empresa.xml") si queremos incluir la ruta




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
 "fecha de nacimiento": "1975",
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
      self.primary_list = []


    def create_file_json(self,filename:str):
        self.filename = filename
        self.file = self.filename+'.json'
        with open(self.file, 'w') as create_json:
           json.dump(self.file,create_json, indent=4, sort_keys=False, )
        

    def add_dict_json(self,file:str, name:str, birth_year:int, languages:list):
        self.file = file
        self.name = name
        self.birth_year = birth_year
        self.languages = languages
        dict = {"Name":self.name,
                "Birth year":self.birth_year,
                "Age": date.now().year - self.birth_year, 
                "Languages": self.languages}
        self.primary_list.append(dict)
        with open(self.file , 'w') as write_json:
            json.dump(self.primary_list, write_json , indent=4, sort_keys=False)


    def print_json_contain(self, file:str):
        with open(file) as contains:
            payload = json.load(contains)
        for element in  payload:
            print(element)

    def print_xml_contain(self,elem:object):
        rough_string = ET.tostring(elem, 'utf-8')
        reparsed = minidom.parseString(rough_string)
        print (reparsed.toprettyxml(indent="  ", newl="\n"))

    def create_xml(self, python_dict:dict):
        self.python_dict = python_dict

        root = ET.Element("EMPRESA")

        for key, value in self.python_dict.items():
            subroot = ET.SubElement(root, key)
            if isinstance(value, list):
                for item in value:
                    ET.SubElement(subroot, "item").text = item
            else:
                subroot.text = str(value)

        file = ET.ElementTree(root)
        file.write("empresa.xml")
       


programador = Programador()
programador.create_file_json('programadores')
programador1 = programador.add_dict_json("programadores.json", "Jesus", 1975, ["python", "java", "php"])
programador2 = programador.add_dict_json("programadores.json", "Sandra", 1991, ["HTML", "CSS", "Javascript"])
programador3 = programador.add_dict_json("programadores.json", "Pepe", 1980, ["C#", "C", "Assembly"])
programador4 = programador.add_dict_json("programadores.json", "Brais", 1988, ["Swift", "Kotlin", "Python"])
programador.print_json_contain("programadores.json")
print()
programador.print_xml_contain(empresa)
programador.create_xml(python_dict)



