package ejercicio06;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

/**
 * EJERCICIO: Entiende el concepto de recursividad creando una función recursiva
 * que imprima números del 100 al 0.
 */
public class JesusWay69 {

    private static void countdown(int num) {
        num--;
        if (num >= 0) {
            System.out.print(num + " ");
            if (num % 10 == 0 && num != 100) {
                System.out.println(" ");
            }
            countdown(num);
        }

    }

    /*
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).
     */
    public static int fibonacci(int n) {
        n--;
        if (n <= 0) {
            return 0;
        } else if (n == 1) {
            return 1;
        } else {
            return fibonacci(n) + fibonacci(n - 1);
        }
    }

    public static int factorial(int n) {
        if (n == 0) {
            return 1;
        } else {
            return n * factorial(n - 1);
        }
    }

    public static void main(String[] args) {
        countdown(101);
        Scanner sc = new Scanner(System.in);
        System.out.print("""
                           \n1- Calcular factorial
                           2- Calcular posici\u00f3n en la secuencia Fibonacci
                           3- Salir
                           Elija una opci\u00f3n: """);
        String choose = sc.next();
         
        if (choose.matches("[1-3]+") == true) {
            int option = Integer.parseInt(choose);
            if (option == 1) {
                System.out.println("\nIntroduzca un número para calcular su factorial: ");
                String num = sc.next();

                int number = Integer.parseInt(num);
                System.out.println("El factorial de " + number + " es: " + factorial(number));

            } else if (option == 2) {
                System.out.println("\nIntroduzca un número para calcular su posición en la secuencia Fibonacci:");
                String num = sc.next();
                int number = Integer.parseInt(num);
                System.out.println("La posición " + number + " de la secuencia Fibonacci tiene el valor " + fibonacci(number));

            } else if (option == 3) {

            }

        } else {
            System.out.println("Sólo se pueden introducir números enteros del 1 al 3");
           
        }

    }

}
