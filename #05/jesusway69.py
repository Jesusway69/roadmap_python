import os
os.system('clear')
"""
 * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.




"""

variable_por_valor = "Hola Python"
print("Variable por valor?? ANTES de la función:",variable_por_valor)
variable_por_referencia = ["Hola", "Python"]
print("Variable por referencia?? ANTES de la función:",variable_por_referencia)
def variables(variable_por_valor:str, variable_por_referencia:list[str,str]):
    variable_por_valor = variable_por_valor.replace("Hola","Adios")
    print("Variable por valor?? DENTRO de la función:",variable_por_valor)
    variable_por_referencia [0] = "Adios" 
    print("Variable por referencia?? DENTRO de la función:",variable_por_referencia)
variables(variable_por_valor,variable_por_referencia)

print("Variable por valor?? DESPUÉS de la función:",variable_por_valor)
print("Variable por referencia?? DESPUÉS de la función:",variable_por_referencia)