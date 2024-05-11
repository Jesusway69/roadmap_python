import os
os.system ('cls')

"""* EJERCICIO:
 * Empleando tu lenguaje, explora la definición del tipo de dato
 * que sirva para definir enumeraciones (Enum).
 * Crea un Enum que represente los días de la semana del lunes
 * al domingo, en ese orden. Con ese enumerado, crea una operación
 * que muestre el nombre del día de la semana dependiendo del número entero
 * utilizado (del 1 al 7).
 *
  """

weekdays_list = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
weekdays_tuple = "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"
weekdays_set = {"Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"}
weekdays_dict = dict(enumerate(weekdays_list, start=1))

[print(i,d , end=" ") for i, d in enumerate(weekdays_list, 1)]
print()
[print(i,d , end=" ") for i, d in enumerate(weekdays_tuple, 1)]
print()
[print(i,d , end=" ") for i, d in enumerate(weekdays_set, 1)]
print()
[print(i,d , end=" ") for i, d in weekdays_dict.items()]
print() 
print(weekdays_dict)



def show_day(key:int):
    days = list(enumerate(weekdays_list,1))
    if key < (len(weekdays_list)) and key > 0:
        print (f"El día de la semana correspondiente al número {key} es el {days[key-1][1]}")
    else:
        print ("El número debe ser mayor a 0 y menor a 8")
show_day(6)


"""* DIFICULTAD EXTRA (opcional):
 * Crea un pequeño sistema de gestión del estado de pedidos.
 * Implementa una clase que defina un pedido con las siguientes características:
 * - El pedido tiene un identificador y un estado.
 * - El estado es un Enum con estos valores: PENDIENTE, ENVIADO, ENTREGADO y CANCELADO.
 * - Implementa las funciones que sirvan para modificar el estado:
 *   - Pedido enviado
 *   - Pedido cancelado
 *   - Pedido entregado
 *   (Establece una lógica, por ejemplo, no se puede entregar si no se ha enviado, etc...)
 * - Implementa una función para mostrar un texto descriptivo según el estado actual.
 * - Crea diferentes pedidos y muestra cómo se interactúa con ellos."""

class Orders():
    def __init__(self) -> None:
        self.orders_state = ["PENDIENTE", "ENVIADO", "ENTREGADO", "CANCELADO" ]
    def state(self,num:int):
        self.state_order = dict(enumerate(self.orders_state,start=1))
        return self.state_order.values(num)
    def waiting_to_cancelled(self):
        pass
    def waiting_to_sent(self):
        pass
    def sent_to_delivered(self):
        pass

orders_instance = Orders()
    

            

