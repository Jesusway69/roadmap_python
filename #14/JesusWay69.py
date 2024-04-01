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
current_datetime = datetime.datetime.now()
current_date = datetime.date.today()
format_current_date = datetime.date.today().strftime('%A, %d-%B-%Y')
format_current_time = datetime.datetime.strptime('2024-04-02 0:50:30', '%Y-%m-%d %H:%M:%S')
week_day = week_days[format_current_time.weekday()]
current_year = current_date.year
current_month = current_date.month
current_day = current_date.day
current_hour = current_datetime.hour
current_minute = current_datetime.minute
current_second = current_datetime.second




print(current_datetime,"\n",
        
        current_date, "\n",
        current_year, "\n",
        current_month, "\n",
        current_day, "\n",
        current_hour, ":",
        current_minute, ":",
        current_second, "\n",
        format_current_date, "\n",
        format_current_time, week_day
        )
