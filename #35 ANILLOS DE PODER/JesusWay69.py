import os, platform, json

if (platform.platform().startswith("macOS") or platform.platform().startswith("Linux")):
    os.system('clear')
else:
    os.system('cls')

""" * EJERCICIO:
 * ¡La temporada 2 de "Los Anillos de Poder" está a punto de estrenarse!
 * ¿Qué pasaría si tuvieras que encargarte de repartir los anillos
 * entre las razas de la Tierra Media?
 * Desarrolla un programa que se encargue de distribuirlos.
 * Requisitos:
 * 1. Los Elfos recibirán un número impar.
 * 2. Los Enanos un número primo.
 * 3. Los Hombres un número par.
 * 4. Sauron siempre uno.
 * Acciones:
 * 1. Crea un programa que reciba el número total de anillos
 *    y busque una posible combinación para repartirlos.
 * 2. Muestra el reparto final o el error al realizarlo."""

def prime_generator(num):
    prime_list = []
    for i in range(2, num + 1):
        prime = True
        for j in range(2, i):
            if i % j == 0:
                prime = False
                break
        if prime:
            prime_list.append(i)
                   
                
    return prime_list
rings = 10
print(prime_generator(rings))


div = len(prime_generator(rings))//2

print(div)


enanos = prime_generator(rings)[div-1]
sauron = 1

rings = rings-enanos-sauron

if rings%2==0:
    hombres = rings/2
    elfos = rings/2-1
else:
    elfos = rings//2
    hombres = rings-elfos
rings = rings-hombres-elfos

print (f"De los 100 anillos se han repartido {sauron} para Sauron, {int(elfos)} para los Elfos, {int(enanos)} para los Enanos y {int(hombres)} para los Hombres")

print ("Sobran: ",int(rings), " anillos")



