import os, platform
from datetime import datetime as DT
from datetime import date as D

if (platform.platform().startswith("macOS") or platform.platform().startswith("Linux")):
    os.system('clear')
else:
    os.system('cls')



""" * EJERCICIO:
 * ¡El 12 de noviembre lanzo mouredev pro!
 * El campus de la comunidad para estudiar programación de
 * una manera diferente: https://mouredev.pro
 *
 * Crea un programa que funcione como una cuenta atrás.
 *
 * - Al iniciarlo tendrás que indicarle el día, mes, año,
 *   hora, minuto y segundo en el que quieres que finalice.
 * - Deberás transformar esa fecha local a UTC.
 * - La cuenta atrás comenzará y mostrará los días, horas,
 *   minutos y segundos que faltan.
 * - Se actualizará cada segundo y borrará la terminal en
 *   cada nueva representación del tiempo restante.
 * - Una vez finalice, mostrará un mensaje.
 * - Realiza la ejecución, si el lenguaje lo soporta, en
 *   un hilo independiente."""

# def number_validation(data:str):
#     if not data.isdigit():
#         print("el dato debe ser numérico")

months =["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
print("Introduzca la fecha y hora en la cual quiere que se pare la cuenta atrás")
while True:
    year = input("Introduzca el año: ")
    if not year.isdigit() or len(year)!=4:
            print ("ERROR: El año debe ser numérico de 4 cifras")
            continue
    elif int(year)<D.today().year:
            print("No puedes poner como objetivo un año que ya ha pasado")
            continue
    
    while True:
        month = input("Introduzca el mes: ")
        if  not month.isdigit() or len(month) > 2 or len(month) <= 0:
                print ("ERROR: El mes debe ser numérico de 1 o 2 cifras")
                continue
        elif int(month)<1 or int(month)>12:
                print ("ERROR: El mes no debe ser menor a 0 ni mayor a 12")
                continue

        while True:
            day = input("Introduzca el día") 
            if not day.isdigit() or len(day)>2 or len(day)<=0:
                print ("ERROR: El día debe ser numérico de 1 o 2 cifras")
                continue
            elif (int(month)==4 or int(month)==6 or int(month)==9 or int(month)==11) and int(day)>30:
                print (f"El mes de {months[int(month)-1]} no puede tener más de 30 días") 
                continue
            elif int(day)<1 or int(day)>31:
                   print ("ERROR: El día no debe ser menor a 0 ni mayor a 31")
                   continue
            while True:
                hour = input("Introduzca la hora (en formato 24h): ")
                if not hour.isdigit() or len(hour)>2 or len(hour)<=0:
                    print ("ERROR: la hora debe ser numérica de 1 o 2 cifras")
                continue




    
    
    
    minute = input("Introduzca el minuto")
    second = input("Introduzca el segundo")

