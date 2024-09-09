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


houses = [0,0,0,0]
houses_dict = {"Frontend":0, "Backend":0, "Mobile":0 , "Data":0}
# points = [{1:{1:[1,3,2,4],2:[1,4,2,3],3:[1,3,4,2],4:[4,1,3,2]}},
#          {2:{1:[2,3,4,1],2:[4,1,3,2],3:[1,3,2,4],4:[2,4,1,3]}},
#          {3:{1:[1,2,3,4],2:[4,1,3,2],3:[1,4,2,3],4:[1,2,4,3]}},
#          {4:{1:[1,3,4,2],2:[1,3,2,4],3:[1,4,3,2],4:[4,1,3,2]}},
#          {5:{1:[1,4,2,4],2:[2,1,4,3],3:[4,2,3,1],4:[2,1,3,4]}},
#          {6:{1:[1,4,2,3],2:[4,1,3,2],3:[1,3,2,4],4:[3,1,4,2]}},
#          {7:{1:[1,4,2,3],2:[4,2,3,1],3:[1,3,2,4],4:[3,1,4,2]}}]

points_distribution =  [{1:[1,4,2,6],2:[1,6,2,4],3:[1,4,6,2],4:[6,1,4,2]},
                        {1:[2,4,6,1],2:[6,1,4,2],3:[1,4,2,6],4:[2,6,1,4]},
                        {1:[1,2,4,6],2:[6,1,4,2],3:[1,6,2,4],4:[1,2,6,4]},
                        {1:[1,4,6,2],2:[1,4,2,6],3:[1,6,4,2],4:[6,1,4,2]},
                        {1:[1,6,2,4],2:[2,1,6,4],3:[6,2,4,1],4:[2,1,4,6]},
                        {1:[1,6,2,4],2:[6,1,4,2],3:[1,4,2,6],4:[4,1,6,2]},
                        {1:[1,6,2,4],2:[6,2,4,1],3:[1,4,2,6],4:[4,1,6,2]}]

questions = {"pregunta 1: ¿Cual de estas definiciones se ajusta más a tu personalidad?":
             ["1 - Analítico, me gusta tener todo perféctamente calculado",
             "2 - Introvertido, me gusta tener perfil bajo y trabajar en la sombra",
             "3 - Nómada digital, me gusta viajar pero estar siempre conectado",
             "4 - Creativo, me gusta enseñar mis obras y disfruto con el estilo"],

              "pregunta 2: ¿Cual de estas tecnologías te gusta más?":
              ["1 - Kotlin", "2 - CSS", "3 - MySQL", "4 - Python"],

              "pregunta 3: ¿Cual de estos dispositivos portátiles preferirías como regalo?":
              ["1 - Un Chromebook", "2 - Un iPad con apple pencil", "3 - Un laptop con Arch Linux", "4 - Un smartphone de gama alta"],

              "pregunta 4: ¿Cual de estas asignaturas te gusta o te gustó más estudiar?":
              ["1 - Telecomunicaciones", "2 - Matemáticas", "3 - Robótica", "4 - Dibujo artístico"],

              "pregunta 5: ¿Cual de 4 películas según tu personalidad crees que más se adapte a ti por temática?, (si no la has visto busca la sinopsis)":
              ["1 - El indomable will Hunting--back", "2 - Her--mobile", "3 - Ghost in the shell--front", "4 - Moneyball--data"],

              "pregunta 6: ¿Cual de estos coches crees que va mejor contigo?":["1 - Cualquier utilitario barato, funcional y discreto",
              "2 - Uno con estilo tipo Fiat 500 o Mini Cooper", "3 - El que mejor relación específica tenga entre CV/Cilindrada/Consumo",
              "4 - Un Tesla o similar, que sea eléctrico y con conectividad de todo tipo con mi smartphone a bordo y en remmoto"],

              "pregunta 7: ¿Cual de estas carreras hubieses elegido de no haber sido la de informática?":["1 - Cualquier otra ingeniería",
              "2 - Bellas artes", "3 - Sin duda administración de empresas", "4 - Si existe, alguna que estudie nanotecnología"]
              }


name = input("introduzca su nombre: ").capitalize()

def user(answer:int, round:int):
    #index = 0
    distribution_question:dict = points_distribution[round-1]
    distribution_answer:list = list(distribution_question[answer])
    for index in range(len(houses)):
            houses[index] = houses[index] + distribution_answer[index]



def quest_printer(questions:dict):
    for question in list(questions.keys()):
        round = 1
        print(question)
        for answers in questions[question]:
            print(answers)
        answer = input("Elija una de las 4 opciones--> ")
        if not answer.isdigit() or int(answer)<1 or int(answer)>4:
            print("Sólo se pueden introducir números del 1 al 4, pruebe de nuevo")
            continue
        round +=1
        user(int(answer), round)

quest_printer(questions)
print ("resultado = " , houses)
Frontend = houses[0]
houses_dict["Frontend"] = houses[0]
Backend = houses[1]
houses_dict["Backend"] = houses[1]
Mobile = houses[2]
houses_dict["Mobile"] = houses[2]
Data = houses[3]
houses_dict["Data"] = houses[3]
win = max(houses_dict.items(), key=lambda x: x[1])[0]

print(f"Por las respuestas que has dado {name} parece que el sector de programación que más se adapta a ti es el de {win}")


