import os, platform

if (platform.platform().startswith("macOS") or platform.platform().startswith("Linux")):
    os.system('clear')
else:
    os.system('cls')


""" * EJERCICIO:
 * Cada 1 de septiembre, el Hogwarts Express parte hacia la escuela
 * de programación de Hogwarts para magos y brujas del código.
 * En ella, su famoso sombrero seleccionador ayuda a los programadores
 * a encontrar su camino...
 * Desarrolla un programa que simule el comportamiento del sombrero.
 * Requisitos:
 * 1. El sombrero realizará 10 preguntas para determinar la casa del alumno.
 * 2. Deben existir 4 casas. Por ejemplo: Frontend, Backend, Mobile y Data.
 *    (Puedes elegir las que quieras)
 * Acciones:
 * 1. Crea un programa que solicite el nombre del alumno y realice 10
 *    preguntas, con cuatro posibles respuestas cada una.
 * 2. Cada respuesta asigna puntos a cada una de las casas (a tu elección).
 * 3. Una vez finalizado, el sombrero indica el nombre del alumno 
 *    y a qué casa pertenecerá (resuelve el posible empate de manera aleatoria,
 *    pero indicándole al alumno que la decisión ha sido complicada)."""



houses = {"Frontend":0, "Backend":0, "Mobile":0 , "Data":0}
questions = {"¿Cual de estas definiciones se ajusta más a tu personalidad?":
             ["1 - Analítico, me gusta tener todo perféctamente calculado",
             "2 - Introvertido, me gusta tener perfil bajo y trabajar en la sombra",
             "3 - Nómada digital, me gusta viajar pero estar siempre conectado",
              "4 - Creativo, me gusta enseñar mis obras y disfruto con el estilo"],
              "¿Cual de estas tecnologías te gusta más?":
              ["1 - Kotlin", "2 - CSS", "3 - MySQL", "4 - Python"],
              "¿Cual de estos dispositivos preferirías como regalo?":
              ["1 - Un Chromebook", "2 - Un iPad con apple pencil", "3 - Un laptop con Arch Linux", "4 - Un smartphone de gama alta"],
              "¿Cual de estas asignaturas te gusta o te gustó más estudiar?":
              ["1 - Telecomunicaciones", "2 - Matemáticas", "3 - Robótica", "4 - Dibujo artístico"],
              "¿Cual de 4 películas según tu personalidad crees que más se adapte a ti por temática?, (si no la has visto busca la sinopsis)":
              ["1 - El indomable will Hunting--back", " 2 - Her--mobile", "3 - Ghost in the shell--front", "4 - Moneyball--data"]}


