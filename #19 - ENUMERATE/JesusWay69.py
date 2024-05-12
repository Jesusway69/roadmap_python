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
    def state(self,num=1):
        self.state_order = dict(enumerate(self.orders_state,start=1))
        return self.state_order.get(num)
    def waiting_to_cancelled(self):
        if self.state()=="PENDIENTE":
         self.state(4)
        else:
            print("No se puede cancelar un producto que ya se ha enviado")
    def waiting_to_sent(self):
        if self.state()=="PENDIENTE":
            self.state(2)
        else:
            print("No se puede enviar un producto que ya se ha enviado, entregado o cancelado")
    def sent_to_delivered(self):
        if self.state()=="ENVIADO":
            self.state(3)
        else:
            print("No se puede marcar como entregado un producto que no se ha enviado, ya se ha entregado o se ha cancelado")

orders_instance = Orders()


    
product_dict = { "P1":1,"P2":1,"P3":1,"P4":1,"P5":1,"P6":1,"P7":1,"P8":1,"P9":1,"P10":1}

while True:
    product = int(input("Seleccione un nº de producto:"))
    if product<1 or product>10 or product.is_integer == False:
        print("Sólo se pueden introducir números del 1 al 10, intente de nuevo")
    else:
        my_product = "P"+str(product)
        state = int(input("Elija una opción; 1-pasar a enviado 2-pasar a entregado 3-pasar a cancelado"))
        if state <1 or state>4 or state.is_integer== False:
             print("Sólo se pueden introducir números del 1 al 3, intente de nuevo")
        elif state==1:
            orders_instance.waiting_to_sent()
            product_dict[my_product]=orders_instance.state()
            print(f"El producto {my_product} se ha {orders_instance.state(2)}")
            break
        elif state==2:
            if product_dict[my_product]!="ENVIADO":
                print("No se puede entregar un producto que no se ha enviado")
            else:
                orders_instance.sent_to_delivered()
                product_dict[my_product]=orders_instance.state()
                print(f"El producto {my_product} se ha {orders_instance.state()}")
                break

   
    
    
    
    
    
    
    
    
  

            

