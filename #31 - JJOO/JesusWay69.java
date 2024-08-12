package ejercicio31;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;
import java.util.TreeMap;

/*
 * EJERCICIO:
 * ¡Los JJOO de París 2024 han comenzado!
 * Crea un programa que simule la celebración de los juegos.
 * El programa debe permitir al usuario registrar eventos y participantes,
 * realizar la simulación de los eventos asignando posiciones de manera aleatoria
 * y generar un informe final. Todo ello por terminal.
 * Requisitos:
 * 1. Registrar eventos deportivos.
 * 2. Registrar participantes por nombre y país.
 * 3. Simular eventos de manera aleatoria en base a los participantes (mínimo 3).
 * 4. Asignar medallas (oro, plata y bronce) basándose en el resultado del evento.
 * 5. Mostrar los ganadores por cada evento.
 * 6. Mostrar el ranking de países según el número de medallas.
 * Acciones:
 * 1. Registro de eventos.
 * 2. Registro de participantes.
 * 3. Simulación de eventos.
 * 4. Creación de informes.
 * 5. Salir del programa.
 */
public class JesusWay69 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String option;
        OlympicGames olympicGames = new OlympicGames();

        do {
            System.out.print("""
                           Elija una opci\u00f3n:
                           1- Registrar evento
                           2- Registrar participante
                           3- Simular evento
                           4- Crear informe
                           5- Salir
                           --->  """);
            option = sc.next().strip();
            sc.nextLine();
            switch (option) {
                case "1":
                    System.out.print("Escriba el nombre de la competición a registrar: ");
                    String sport = sc.nextLine().strip().toUpperCase();
                    olympicGames.registerEvent(sport);
                    break;
                case "2":
                    System.out.print("Escriba el nombre del participante a registrar: ");
                    String name = sc.nextLine().strip().toUpperCase();
                    System.out.print("Escriba el nombre del pais de " + name + " : ");
                    String country = sc.nextLine().strip().toUpperCase();
                    olympicGames.registerAthlete(name, country);
                    break;
                case "3":
                    olympicGames.eventSimulator();
                    break;
                case "4":
                    olympicGames.showEvents();
                    olympicGames.showAthletes();
                    break;
                case "5":
                    break;

            }

        } while (!"5".equals(option));

    }

}

class OlympicGames {

    List<String> sportEvents = new ArrayList<>();
    Map<String, String> competitors = new HashMap<>();

    public OlympicGames() {
    }

    public void registerEvent(String event) {
        sportEvents.add(event);
        System.out.println("El evento deportivo " + event + " se ha registrado correctamente\n");

    }

    public void registerAthlete(String name, String country) {
        competitors.put(name, country);
        System.out.print("El participante " + name + " de " + country + " se ha registrado correctamente\n");
        showEvents();

    }

    public void showEvents() {
        System.out.println("Deportes disponibles:");
        int i = 0;
        for (String sport : sportEvents) {
            i++;
            System.out.println(i + "-" + sport);
        }

    }

    public void showAthletes() {
        int i = 0;
        System.out.println("Atletas disponibles: ");
        for (String key : competitors.keySet()) {
            String value = competitors.get(key);
            i++;
            System.out.println(i + "-" + key + " --> " + value);
        }
    }

    public void eventSimulator() {
        int athNum = 1, sportNum = 0;
        Scanner sc = new Scanner(System.in);
        System.out.println("Comienzan los eventos!!");
        System.out.println("-----------------------");
        TreeMap<String, String> selectecCompetitors = new TreeMap<>();
        
        boolean flag = true;

        while (flag) {
            showEvents();
            System.out.print("Elija el número del deporte para empezar la competición: ");
            sportNum = sc.nextInt();
            if (sportNum < 1 || sportNum > sportEvents.size()) {
                System.out.println("El número " + sportNum + " no corresponde a ningún deporte");
            } else {
                System.out.println("Empieza la competición de " + sportEvents.get(sportNum - 1));
                flag = false;
            }
        }
        while (!competitors.isEmpty() || athNum != 0) {
            showAthletes();
            System.out.print("Elija el número de un deportista para empezar la competición de: "
                    + sportEvents.get(sportNum - 1)
                    + "\n e introduce 0 cuando se hayan seleccionado al menos 3 participantes para terminar la selección");
            athNum = sc.nextInt();
            if (athNum < 0 || athNum > competitors.size()) {
                System.out.println("El número " + athNum + " no corresponde a ningún deportista");
            } else {
                int i = 0;
                for (String key : competitors.keySet()) {
                    String value = competitors.get(key);
                    i++;
                    if (athNum == i) {
                        selectecCompetitors.put(key, value);
                        System.out.println("Participante nº " + athNum + " añadido a la competición de " + sportEvents.get(sportNum - 1));
                    } else if (athNum == 0 && selectecCompetitors.size() < 3) {
                        System.out.println("Debe elegir al menos 3 participantes");
                    } else if (athNum == 0 && selectecCompetitors.size() >= 3) {
                        randomCompetition(selectecCompetitors);
                    }
                }
            } 
        }
        
        
    }

    public void randomCompetition(TreeMap selectecCompetitors) {
        String[] podium = {"oro", "plata", "bronce"};
        int medal =0;
        
        while (!selectecCompetitors.isEmpty()) {

            for (var podiumkey : selectecCompetitors.keySet()) {
                podiumkey = selectecCompetitors.lastKey();
                System.out.println("El deportista " + podiumkey + " de " + selectecCompetitors.get(podiumkey)
                        + " gana la medalla de " + podium[medal]);
                medal++;
                podiumkey.toString();
                selectecCompetitors.remove(podiumkey);

            }

        }

    }



}
