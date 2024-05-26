import os, time, random
os.system('cls')



"""
 * EJERCICIO:
 * Explora el concepto de callback en tu lenguaje creando un ejemplo
 * simple (a tu elección) que muestre su funcionamiento.
 *
 """
def show_result(result):
    print(result)

def main_funtcion (fun, args,callback):
    result = fun(*args)
    callback(result)

def sum(a,b):
    return a + b
main_funtcion(sum, (546,7543), callback=show_result)

"""* DIFICULTAD EXTRA (opcional):
 * Crea un simulador de pedidos de un restaurante utilizando callbacks.
 * Estará formado por una función que procesa pedidos.
 * Debe aceptar el nombre del food, una callback de confirmación, una
 * de listo y otra de entrega.
 * - Debe imprimir un confirmación cuando empiece el procesamiento.
 * - Debe simular un tiempo aleatorio entre 1 a 10 segundos entre
 *   procesos.
 * - Debe invocar a cada callback siguiendo un orden de procesado.
 * - Debe notificar que el food está listo o ha sido entregado."""

def processing(state,args,callback):
    result = state(*args)
    if result == None:
        return
    callback(result)

def confirmation(*food):
    print(F"El plato de {food} se ha confirmado")
    seconds = random.randint(1,10)
    time.sleep(seconds)
    return ready(food)


def ready(*food):
    print(F"El plato de {food} está listo para servir")
    seconds = random.randint(1,10)
    time.sleep(seconds)
    return delivery(food)

def delivery(*food):
    print(F"El plato de {food} está servido")
      
processing(confirmation, ("fabada asturiana","cocido"), callback=ready)