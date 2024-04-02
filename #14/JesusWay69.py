import os , datetime
os.system('cls')


""" * EJERCICIO:
 * Crea dos variables utilizando los objetos fecha (date, o semejante) de tu lenguaje:
 * - Una primera que represente la fecha (día, mes, año, hora, minuto, segundo) actual.
 * - Una segunda que represente tu fecha de nacimiento (te puedes inventar la hora).
 * Calcula cuántos años han transcurrido entre ambas fechas.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la fecha de tu cumpleaños, formatéala y muestra su resultado de
 * 10 maneras diferentes. Por ejemplo:
 * - Día, mes y año.
 * - Hora, minuto y segundo.
 * - Día de año.
 * - Día de la semana.
 * - Nombre del mes.
 * (lo que se te ocurra...)"""


week_days = ["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo"]
months =["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
current_datetime = datetime.datetime.now()
current_date = datetime.date.today()
format_current_date = datetime.date.today().strftime('%A, %d-%B-%Y')
format_manual_time = datetime.datetime.strptime('29-07-1999 22:15:30', '%d-%m-%Y %H:%M:%S')
week_day = week_days[format_manual_time.weekday()]
week_today = week_days[current_date.weekday()]

current_year = current_date.year
current_month = months[current_date.month-1]
current_day = current_date.day
current_hour = current_datetime.hour
current_minute = current_datetime.minute
current_second = current_datetime.second

my_age = current_datetime - format_manual_time
my_age_years = int(my_age.days//365.25)



print(current_datetime,"\n",
     
        current_hour, ":",
        current_minute, ":",
        current_second, "\n",
        format_current_date, "\n",
        format_manual_time, week_day, "\n",
        my_age_years, "\n",
        my_age,
        "\n\n\n"
        )






def input_data()->datetime.date:
    while True:
        year = input("Escriba su año de nacimiento: ")
        if not year.isdigit or len(year)!=4:
            print ("ERROR: El año debe ser numérico de 4 cifras")
            continue
        while True:
            month = input("Escriba el mes de nacimiento: ")
            if not year.isdigit or len(month)>2 or len(month)<0:
                print ("ERROR: El mes debe ser numérico de 1 o 2 cifras")
                continue
            elif int(month)<1 or int(month)>12:
                print ("ERROR: El mes no debe ser menor a 0 ni mayor a 12")
                continue
            while True:
                day = input("Escriba el día de nacimiento: ")
                if not year.isdigit or len(month)>2 or len(month)<0:
                   print ("ERROR: El día debe ser numérico de 1 o 2 cifras")
                   continue
                elif int(month)<1 or int(month)>31:
                   print ("ERROR: El día no debe ser menor a 0 ni mayor a 31")
                   continue
                if ((int(year) % 4 != 0) and ((int(year) % 100 == 0) or (int(year) % 400 != 0)) and int(month)==2 and int(day)>28):
                    print (f"El año {year} no fue bisiesto y febrero no puede tener más de 28 días")
                    break
                
               

                return datetime.date(int(year),int(month),int(day))
#print(input_data())
       

my_test_date = datetime.date(1974,12,26)   

def show_data(date_object:datetime.date):
    str_date = str(f"{date_object.day}-{date_object.month}-{date_object.year}")
    format_date = datetime.datetime.strptime(str_date, '%d-%m-%Y')
    my_age = current_datetime - format_date
    my_age_years = int(my_age.days//365.25)
    print(f"\nHoy es {week_today} día {current_day} de {current_month} de {current_year}")
    print(f"Y son las {current_hour} horas y {current_minute} minutos\n")
    if current_hour>6 and current_hour<12:
      print("¡¡Buenos días!!\n")
    elif current_hour>11 and current_hour<21:
        print("¡¡Buenas tardes!!\n")
    else:
        print("¡¡Buenas noches!!\n")

    print(f"Como has indicado que naciste el día {date_object.day} de {months[date_object.month-1]} de {date_object.year} ...")
    print("... (por cierto naciste un", week_days[format_date.weekday()],")")
    print(f"y por lo tanto tienes {my_age_years} años")

    

      
show_data(input_data())


