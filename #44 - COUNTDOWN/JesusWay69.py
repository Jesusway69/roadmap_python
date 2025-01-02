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

months =["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
print("Introduzca la fecha y hora en la cual quiere que se pare la cuenta atrás")
while True:
    year = input("Introduzca el año: ")
    if not year.isdigit() or len(year)!=4:
        print ("ERROR: El año debe ser numérico de 4 cifras")
        continue
    elif int(year) < D.today().year:
        print("No puedes poner como objetivo un año que ya ha pasado")
        continue
    
    while True:
        month = input("Introduzca el mes en formato numérico: ")
        if  not month.isdigit() or len(month) > 2 or len(month) <= 0:
            print ("ERROR: El mes debe ser numérico de 1 o 2 cifras")
            continue
        elif int(month) < 1 or int(month) > 12:
            print ("ERROR: El mes no debe ser menor a 0 ni mayor a 12")
            continue
        elif int(month) < D.today().month:
            print("ERROR: No puedes poner como objetivo un mes que ya ha pasado")
            continue

        while True:
            day = input("Introduzca el día") 
            if not day.isdigit() or len(day) > 2 or len(day) <= 0:
                print ("ERROR: El día debe ser numérico de 1 o 2 cifras")
                continue
            elif (int(month)==4 or int(month)==6 or int(month)==9 or int(month)==11) and int(day)>30:
                print (f"El mes de {months[int(month)-1]} no puede tener más de 30 días") 
                continue
            elif int(day) < 1 or int(day) > 31:
                   print ("ERROR: El día no debe ser menor a 0 ni mayor a 31")
                   continue
            elif int(day) < D.today().day and int(month) == D.today().month:
                print("ERROR: No puedes poner como objetivo un día que ya ha pasado")
                continue

            while True:
                hour = input("Introduzca la hora (en formato 24h): ")
                if not hour.isdigit() or len(hour) > 2 or len(hour) <= 0:
                    print ("ERROR: la hora debe ser numérica de 1 o 2 cifras")
                    continue
                elif int(hour) > 24 or int(hour < 0):
                    print("ERROR: la hora debe ser de 0 a 24")
                    continue

                while True:
                    minute = input("Introduzca el minuto: ")
                    if not minute.isdigit() or len(minute) > 2 or len(minute) <= 0:
                        print ("ERROR: el minuto debe ser numérico de 1 o 2 cifras")  
                        continue
                    elif int(minute) > 59 or int(minute < 0):
                        print("ERROR: el minuto debe ser de 0 a 59")
                        continue
                    else:
                        break


while year != D.today().year and month != D.today().month and day != D.today().day and hour != DT.today().hour and minute != DT.today().minute:
    print(f"Fecha y hora objetivo: {year}/{month}/{day} {hour}:{minute}")
    print(f"")
                    
                    
                
           


    
    
    
    minute = input("Introduzca el minuto")
    second = input("Introduzca el segundo")

