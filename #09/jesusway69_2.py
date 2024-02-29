import os
os.system('clear') #MAC/LINUX
#os.system('cls') #WINDOWS

"""
 *
 * DIFICULTAD EXTRA (opcional):
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo."""

class Empleado():
    def __init__(self, id , nombre):
       self.id = id
       self.nombre = nombre
       self.finanzas = False
       self.compras = False
       self.proyectos = False
       self.organizacion = False
       self.programacion = False
       self.despliegue = False
   
    def print(self):
          print ("id:", self.id, "Nombre:",self.nombre,"\nHace finanzas? =", self.finanzas,
               "\nHace compras? =", self.compras, "\nHace proyectos? =", self.proyectos,
               "\nOrganiza el trabajo? =", self.organizacion, "\nPica código? =", self.programacion,
               "\nDespliega programas? =",self.despliegue , "\n")
     
class Gerente(Empleado):
    def es_gerente(self):
        self.finanzas=True
        self.compras=True
        self.print()
     
class Gerente_proyecto(Gerente,Empleado):
    def es_gerente_proyecto(self):
        self.organizacion=True
        self.proyectos=True
        self.print()

class Programador (Gerente_proyecto,Gerente,Empleado):
    def es_programador(self):
        self.programacion=True
        self.despliegue=True
        self.print()


gerente = Gerente(1, "Paco")
gerente_proyecto = Gerente_proyecto(2, "Luis")
programador = Programador(3,"Pepe")
gerente= Gerente(5,"Antonio")

programador.es_programador()
gerente.es_gerente()
gerente_proyecto.es_gerente_proyecto()

