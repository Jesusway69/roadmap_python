import os
os.system('cls')
from datetime import date as D

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

students_list = [["Jesus",'26/12/1984',[6.8,8.3,6.5,9.9]],
                 ["Sandra",'24/3/1989',[4.2,10,7.9,8,7.8]],
                 ["Pablo",'14/8/1983',[6.5,3,8,9.6,5,8.5]],
                 ["Leire",'2/11/1991',[5,6.7,10,9.3,4.7,7]]]

def students(option):
    def avg_qualification(students_list:list):
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
        for name, avg in zip(names_list,qualification_list) :
            print("nombre:",name," Nota media:", avg)

        name_qualifications_dict = {name:avg for name, avg in zip(names_list,qualification_list)}
        
         
        print(name_qualifications_dict)

    if option==1:
        return avg_qualification
prueba = students(1)
prueba(students_list)




