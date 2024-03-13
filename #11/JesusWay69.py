import os
os.system('cls')


"""
 * IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.
 *
 * EJERCICIO:
 * Desarrolla un programa capaz de crear un archivo que se llame como
 * tu usuario de GitHub y tenga la extensión .txt.
 * Añade varias líneas en ese fichero:
 * - Tu nombre.
 * - Edad.
 * - Lenguaje de programación favorito.
 * Imprime el contenido.
 * Borra el fichero.
 *
 
"""



# file=open("JesusWay69.txt", "w")
# file.write("Jesus\n")
# file.write("99\n")
# file.write("Python\n")
# file.close()
# file=open("JesusWay69.txt", "r")
# readfile = file.read()
# file.close
# print(readfile)

# file = open("JesusWay69.txt", "a")
# file.write("linea nueva añadida\n")
# file=open("JesusWay69.txt", "r")
# readfile = file.read()
# file.close
# print(readfile)

# file = open("JesusWay69.txt", "r+")
# readfile = file.read()
# file.write("otra linea nueva añadida\n")

# readfile = file.read()
# file.close
# print(readfile)
# print("\n")




"""
* DIFICULTAD EXTRA (opcional):
 * Desarrolla un programa de gestión de ventas que almacena sus datos en un 
 * archivo .txt.
 * - Cada producto se guarda en una línea del arhivo de la siguiente manera:
 *   [nombre_producto], [cantidad_vendida], [precio].
 * - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
 *   actualizar, eliminar productos y salir.
 * - También debe poseer opciones para calcular la venta total y por producto.
 * - La opción salir borra el .txt.

"""

class Devices ():
   def __init__(self,nombre_fichero):
    self.nombre_fichero = nombre_fichero
    file = open (self.nombre_fichero, "w")
    file.write("PRODUCTO , UDS VENDIDAS, PRECIO\n")
    file.close()
   
   def add(self, producto, cantidad, precio):
      file = self.nombre_fichero
      self.producto = producto
      self.cantidad = cantidad
      self.precio = precio
      file = open(file,"a") 
      
      file.write(self.producto)
      file.write(" , ")
      file.write(self.cantidad)
      file.write(" , ")
      file.write(self.precio)
      file.write("\n")
      file.close

   def show_all(self):
     file = self.nombre_fichero
     n_line = 0
     file = open(file, "r")
     
     print("Contenido del fichero:\n")
     for i in file:
      if n_line == 0:
        print(i)
        n_line +=1
      else:
       print(n_line, " - " ,i)
       n_line +=1
     file.close()
   
   def find(self,substring):
     file = self.nombre_fichero
     self.substring = substring
     product_list =[]
     file =  open(file, 'r+')
     line = file.readline()
     for line in file:
         if self.substring in line:
           product_list.append(line)
           continue
         elif self.substring not in line:
           continue
         else:
           print("Artículo no encontrado\n")
     print("los productos que busca son:\n")
     for i in product_list:
       print("- ",i)
     file.close()

   def remove(self):
      file = self.nombre_fichero
      self.show_all()
      line_edit = int(input("Introduzca el número del elemento a borrar: "))
      with open(file , "r+") as file:
       lines = file.readlines()
       print(lines)
      #with open(file, "w") as file:
       line = lines[line_edit]
       lines.remove(line)
       for line in lines:
         file.write(line)
      
       file1 = file.read()
       print(file1)
       
      

       


   
#os.remove("ventas.txt")
device = Devices("ventas.txt")
device.add("Macbook", "7", "2500")
device.add("HP Elitebook", "5", "1500")
device.add("Samsung Galaxy S24", "9", "700")
device.add("HP Pavilion", "6", "1200")
#device.find("0")
#device.show_all()
device.remove()


      