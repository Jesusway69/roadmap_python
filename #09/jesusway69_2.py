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
    
    
    def __init__(self):
       self.empleados_gerente = empleados_gerente = []
       self.empleados_proyectos = empleados_proyectos = []
       self.finanzas = False
       self.compras = False
       self.proyectos = False
       self.organizacion = False
       self.programacion = False
       self.despliegue = False
   
    def print(self, cargo, id , nombre):
          self.cargo = cargo
          self.id = id
          self.nombre = nombre
        #   if self.cargo == "Programador" or self.cargo =="Gerente de proyecto":
        #       self.empleados_gerente.append(nombre)
              
        #   if self.cargo == "Programador":
        #       self.empleados_proyectos.append(nombre)
         
          print ("\nid:", self.id, "\nNombre:",self.nombre,"\nCargo:", self.cargo,"\n¿Hace finanzas? =", 
               self.finanzas,"\n¿Hace compras? =", self.compras, "\n¿Hace proyectos? =", self.proyectos,
               "\n¿Organiza el trabajo? =", self.organizacion, "\n¿Pica código? =", self.programacion,
               "\n¿Despliega programas? =",self.despliegue)
      
    def print_empleados(self,list_empleados):
        print ("\nEmpleados a su cargo:", end=' ')
        [print(i, end=' ')for i in list_empleados]

          
        

          
class Gerente(Empleado):
      
      def es_gerente(self, id, nombre,lista_g):
        self.finanzas=True
        self.compras=True
        self.print("Gerente", id ,nombre)
        self.print_empleados(lista_g)


 
     
class Gerente_proyecto(Gerente,Empleado):
         
      def es_gerente_proyecto(self, id, nombre,lista_p):
        self.organizacion=True
        self.proyectos=True
        self.print("Gerente de proyecto", id ,nombre)
        self.print_empleados(lista_p)
        


class Programador (Gerente_proyecto,Gerente,Empleado):
      
      def es_programador(self, id, nombre):
        self.programacion=True
        self.despliegue=True     
        self.print("Programador", id ,nombre)
        
        

gerente = Gerente()
gerente_proyecto = Gerente_proyecto()
programador = Programador()

dict_empleados = {
1: "Paco",
2: "Sandra",
3: "Carlos",
4: "Ana",
5: "Pedro",
6: "Lucía"

}
list_empleados = []
list_proyectos = []
for k,v in dict_empleados.items():
      if  k>2 and k<5:
          list_proyectos.append(v)
      if k>= 5:
          list_empleados.append(v)
          list_proyectos.append(v)

for k,v in dict_empleados.items():

   if k<=2:
        gerente.es_gerente(k,v,list_empleados)
        
   elif k>2 and k<5:
        
        gerente_proyecto.es_gerente_proyecto(k,v,list_proyectos)
        
   else:
       
        programador.es_programador(k,v)
       

          
      


# gerente.es_gerente(1,"Paco")
# gerente_proyecto.es_gerente_proyecto(2, "Luis")
# programador.es_programador(3,"Pepe")



