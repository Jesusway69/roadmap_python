import os
os.system('clear') #MAC/LINUX
os.system('cls') #WINDOWS

"""
* EJERCICIO:
 * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
 * implemente una superclase Animal y un par de subclases Perro y Gato,
 * junto con una función que sirva para imprimir el sonido que emite cada Animal."""

class Animal():
    
    def __init__(self,sonido, animal):
        self.sonido = sonido
        self.animal = animal
    def print(self):
        print(self.animal , "hace", self.sonido)


class Especie(Animal):
    articulo ="El"
    def print(self):
        if self.animal.endswith("a"):
            self.articulo="La"
         
        print(self.articulo, self.animal , "hace", self.sonido)

mi_perro = Especie("Guau!", "perro")
mi_gato = Especie("Miau!", "gato")
mi_vaca = Especie("Muuuu!", "vaca")
mi_perro.print()
mi_gato.print()
mi_vaca.print()
print("\n\n\n")


"""
 *
 * DIFICULTAD EXTRA (opcional):
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo."""

class Gerentes():
    def __init__(self, id, nombre) -> None:
       self.id = id
       self.nombre = nombre
       self.finanzas = False
       self.compras = False
       self.proyectos = False
       self.organizacion = False
       self.programacion = False
       self.despliegue = False
    
    def set_gerencia(self):
        self.finanzas=True
        self.compras=True

    def set_gerencia_proyectos(self):
        self.organizacion=True
        self.proyectos=True

    def set_programacion(self):
        self.programacion=True
        self.despliegue=True

    def print(self):
     print ("id:", self.id, "Nombre:",self.nombre,"\nHace finanzas? =", self.finanzas,
               "\nHace compras? =", self.compras, "\nHace proyectos? =", self.proyectos,
               "\nOrganiza el trabajo? =", self.organizacion, "\nPica código? =", self.programacion,
               "\nDespliega programas? =",self.despliegue , "\n")
   

class Gerentes_proyecto(Gerentes):
    pass

class Programador (Gerentes_proyecto,Gerentes):
    pass

gerencia = Gerentes(1, "Paco")
gerencia.set_gerencia()
gerencia.print()

gerencia_proyectos = Gerentes_proyecto(2, "luis")
gerencia_proyectos.set_gerencia_proyectos()
gerencia_proyectos.print()

programadores = Programador(3, "Pepe")
programadores.set_programacion()
programadores.print()