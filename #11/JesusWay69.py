import os
os.system('clear')


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



file=open("JesusWay69.txt", "w")
file.write("Jesus\n")
file.write("99\n")
file.write("Python\n")
file.close()
file=open("JesusWay69.txt", "r")
readfile = file.read()
file.close
print(readfile)

file = open("JesusWay69.txt", "a")
file.write("linea nueva añadida\n")
file=open("JesusWay69.txt", "r")
readfile = file.read()
file.close
print(readfile)

file = open("JesusWay69.txt", "r+")
readfile = file.read()
file.write("otra linea nueva añadida\n")

readfile = file.read()
file.close
print(readfile , "hola")




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
    open (self.nombre_fichero, "w").close() 
   
   def añadir(self, producto, cantidad, precio):
      file = self.nombre_fichero
      self.producto = producto
      self.cantidad = cantidad
      self.precio = precio
      file = open(file,"a") 
      file.write(self.producto)
      file.write(",")
      file.write(self.cantidad)
      file.write(",")
      file.write(self.precio)
      file.write("\n")
      file.close
   
os.remove("ventas.txt")
# device = Devices("ventas.txt")
# device.añadir("Macbook", "7", "2500")
# device.añadir("HP Elitebook", "5", "1500")

      