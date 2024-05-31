import os
os.system('cls')
from datetime import datetime as DT

"""* EJERCICIO:
 * Explora el concepto de funciones de orden superior en tu lenguaje 
 * creando ejemplos simples (a tu elección) que muestren su funcionamiento.
 *
"""

def operator(fun):
    def sum(num1,num2):
        return num1+num2
    def multiplication(num1,num2):
        return num1*num2
    def substraction(num1,num2):
        return num1-num2
    def division (num1,num2):
        if num2 !=0:
           return num1/num2
        else:
            return "No se puede dividir entre 0"
    def pow (num1,num2):
        return num1**num2
    if fun == '+':
        return sum
    elif fun == '-':
        return substraction
    elif fun == '*':
        return multiplication
    elif fun == "**":
        return pow
    elif fun == '/':
        return division
    else:
        print("Operador incorrecto")
    
suma = operator('+')
resta = operator('-')
multiplicacion = operator('*')
division = operator('/')
potencia = operator("**")
print (suma(485,896),"",resta(456,89.5),"",division(4,0),"",potencia(2,8),"",multiplicacion(14,24))
print('\n\n\n\n')



""" * DIFICULTAD EXTRA (opcional):
 * Dada una lista de estudiantes (con sus nombres, fecha de nacimiento y 
 * lista de calificaciones), utiliza funciones de orden superior para
 * realizar las siguientes operaciones de procesamiento y análisis:
 * - Promedio calificaciones: Obtiene una lista de estudiantes por nombre
 *   y promedio de sus calificaciones.
 * - Mejores estudiantes: Obtiene una lista con el nombre de los estudiantes
 *   que tienen calificaciones con un 9 o más de promedio.
 * - Nacimiento: Obtiene una lista de estudiantes ordenada desde el más joven.
 * - Mayor calificación: Obtiene la calificación más alta de entre todas las
 *   de los alumnos.
 * - Una calificación debe estar comprendida entre 0 y 10 (admite decimales)."""

students_list = [["Jesus",DT.strptime('26/12/1974','%d/%m/%Y'),[9.8, 8.3, 7.8, 9.9, 10, 9.7, 9.6, 9.7, 9.3]],
                 ["Sandra",DT.strptime('24/3/1989','%d/%m/%Y'),[6.2, 9.6, 7.9, 8, 7.8, 8.4, 9, 7.8, 9.8, 8.6]],
                 ["Pablo",DT.strptime('14/8/1982','%d/%m/%Y'),[6.5, 7.3, 8, 9.6, 5, 8.5, 9, 9.8, 8, 9.6, 9]],
                 ["Leire",DT.strptime('2/11/1991','%d/%m/%Y'),[9.5, 9.7, 9.8, 9.3, 7.7, 9, 9, 8.7, 9.9, 8.9]]]

def students(option:int):
    def avg_qualification(students_list:list)->dict:
        qualification_list = []
        names_list=[]
        acc=0
        
        for student in students_list:
            names_list.append(student[0])
            for qualification in student[2]:
                acc = qualification + acc
                qualification=0
            qualification_list.append(round(acc/len(student[2]),1))
            acc=0
        if option == 1:
            print("Nota media de los alumnos: \n")
            for name, avg in zip(names_list,qualification_list) :
                print("Nombre:",name," Nota media:", avg)
        name_qualifications_dict = {name:avg for name, avg in zip(names_list,qualification_list)}     
        return name_qualifications_dict

    def best(students_list:list):
      best_students = avg_qualification(students_list)
      print("Estudiantes con un 9 o más de nota media: \n")
      for k,v in best_students.items():                                                                
          if v>=9:
              print (k,v)

    def sorted_age(students_list:list):
        print("Lista de estudiantes ordenados desde el más joven:\n")
        sorted_age_list = sorted(students_list, key=lambda student: student[1],reverse=True)
        for student in sorted_age_list:
            birth_date = student[1].strftime('%d/%m/%Y')
            print(f"{student[0]}  -  Fecha de nacimiento: {birth_date}")
    

    def hight_qualification(students_list:list):
        print("Lista de estudiantes con su nota más alta: \n")
        for student in students_list:
            hightest=0
            name = student[0]
            for qualification in student[2]:
                if qualification > hightest:
                    hightest = qualification
            print (f"{name}  -  Calificación más alta: {hightest}")

    if option==1:
        return avg_qualification
    if option==2:
        return best
    if option==3:
        return sorted_age
    if option==4:
        return hight_qualification
    
while True:
    option = input("""Elija una opción:\n1-Mostrar la nota media de todos los alumnos\n2-Mostrar los alumnos con nota media igual o superior a 9
    3-Mostrar todos los alumnos ordenados por fecha de nacimiento desde el más joven\n4-Mostrar todos los alumnos con su nota más alta\n5-Salir\n---> """)
    if option=="5":
        break
    if option.isdigit:
        option = int(option) 
        if int(option)>4 or int(option)<1:
            print("Solo se pueden introducir números del 1 al 5, intente de nuevo o pulse enter para salir")        
        else:
            students(int(option))(students_list)
            break
    else:
        print("Solo se pueden introducir números del 1 al 5, intente de nuevo o pulse enter para salir") 





