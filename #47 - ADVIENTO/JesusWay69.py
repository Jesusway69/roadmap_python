import os, platform

if (platform.platform().startswith("macOS") or platform.platform().startswith("Linux")):
    os.system('clear')
else:
    os.system('cls')

""" * EJERCICIO:
 * ¡Cada año celebramos el aDEViento! 24 días, 24 regalos para
 * developers. Del 1 al 24 de diciembre: https://adviento.dev
 *
 * Dibuja un calendario por terminal e implementa una
 * funcionalidad para seleccionar días y mostrar regalos.
 * - El calendario mostrará los días del 1 al 24 repartidos
 *   en 6 columnas a modo de cuadrícula.
 * - Cada cuadrícula correspondiente a un día tendrá un tamaño
 *   de 4x3 caracteres, y sus bordes serán asteríscos.
 * - Las cuadrículas dejarán un espacio entre ellas.
 * - En el medio de cada cuadrícula aparecerá el día entre el
 *   01 y el 24.
 *
 * Ejemplo de cuadrículas:
 * **** **** **** **** **** ****
 * *01* *02* *03* *04* *05* *06*
 * **** **** **** **** **** ****
 *
 * - El usuario seleccioná qué día quiere descubrir.
 * - Si está sin descubrir, se le dirá que ha abierto ese día
 *   y se mostrará de nuevo el calendario con esa cuadrícula
 *   cubierta de asteríscos (sin mostrar el día).
 *
 * Ejemplo de selección del día 1
 * **** **** **** 
 * **** *02* *03*
 * **** **** ****
 *
 * - Si se selecciona un número ya descubierto, se le notifica
 *   al usuario."""

# stars_list = ['*','*','*','*']

# def print_stars():
#     for star in stars_list:
#         print(star, end='')
# for i in range(12):
#     print('')
#     for j in range(6):
#         print_stars(), print(end=' ')

for i in range (1,349):
    if i%5 == 0:
        print(' ', end='')
        i+=1
    if i%30==0:
        print('')
    else:
        print(i, end='')


