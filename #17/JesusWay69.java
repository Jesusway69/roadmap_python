package roadmap.ejercicio_17;

import java.util.ArrayList;
import java.util.List;
import java.util.Set;
import java.util.TreeSet;

/*
 * EJERCICIO:
 * Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
 * números del 1 al 10 mediante iteración.
 *
 * DIFICULTAD EXTRA (opcional):
 * Escribe el mayor número de mecanismos que posea tu lenguaje
 * para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?
 */
public class JesusWay69 {

    public static void main(String[] args) {
        iterator1();
        iterator2();
        iterator3();
        iterator4();
        iterator5();
        iterator6();
        iterator7();
        iterator8();
        iterator9(0);
        iterator10();
        iterator11();
        iterator12();
        iterator13();
        iterator14();
    }

    private static void iterator1() {
        for (int i = 1; i <= 10; i++) {
            System.out.print(i + " ");
        }
        System.out.print(" --> Método 1");
        System.out.println("");
    }

    private static void iterator2() {
        int i = 1;
        while (i <= 10) {
            System.out.print(i + " ");
            i++;
        }
        System.out.print(" --> Método 2");
        System.out.println("");
    }

    private static void iterator3() {
        int i = 1;
        do {
            System.out.print(i + " ");
            i++;
        } while (i <= 10);
        System.out.print(" --> Método 3");
        System.out.println("");
    }

    private static void iterator4() {
        for (int i = 1, j = 2; i < 10 && j <= 10; i += 2, j += 2) {//for con 2 índices de control(par,impar)
            System.out.print(i + " " + j + " ");
        }
        System.out.print(" --> Método 4");
        System.out.println("");
    }

    private static void iterator5() {
        for (int i = 1, j = 2; i < 10 && j <= 10; i++, j++) {
            if (i % 2 != 0 || j % 2 == 0) {
                System.out.print(i + " " + j + " ");
            }
        }
        System.out.print(" --> Método 5");
        System.out.println("");
    }

    private static void iterator6() {
        int i;
        for (i = 1; i <= 5; i++) {
            if (i <= 5) {
                System.out.print(i + " ");
                continue;
            }
        }
        for (int j = i; j <= 10; j++) {
            System.out.print(j + " ");
        }
        System.out.print(" --> Método 6");
        System.out.println("");
    }

    private static void iterator7() {
        int i = 1;
        for (; true;) {
            if (i <= 10) {
                System.out.print(i + " ");
                i++;
            } else {
                System.out.print(" --> Método 7");
                System.out.println("");
                break;
            }

        }
    }

    private static void iterator8() {
        int i;
        for (i = 1; i <= 10; i += 2) {
            System.out.print(i + " ");
            for (int j = 0; j < 1; j++) {
                if (i < 10) {
                    System.out.print(i + 1 + " ");
                }
            }
        }
        System.out.print(" --> Método 8");
        System.out.println("");
    }

    private static void iterator9(int i) {
        if (i < 10) {
            System.out.print(++i + " ");
            iterator9(i);
        } else {
            System.out.print(" --> Método 9");
            System.out.println("");
        }

    }

    private static void iterator10() {
        StringBuilder nums = new StringBuilder();
        for (int i = 1; i <= 10; i++) {
            nums.append(i);
        }
        for (int j = 0; j <= nums.length() - 1; j++) {
            if (nums.charAt(j) == '0') {
                System.out.print("\b0 ");
            } else {
                System.out.print(nums.charAt(j) + " ");
            }
        }
        System.out.print(" --> Método 10");
        System.out.println("");

    }

    private static void iterator11() {
        Set<Integer> mySet = new TreeSet<Integer>();
        do {
            int num = (int) (Math.random() * 10 + 1);
            mySet.add(num);
        } while (mySet.size() <= 9);

        for (Integer value : mySet) {
            System.out.print(value + " ");
        }
        System.out.print(" --> Método 11");
        System.out.println("");
    }

    private static void iterator12() {
        char[] myList = {'3', '4', '5', '6', '7', '8', '9', ':', ';', '<'};

        for (int myCode : myList) {
            System.out.print((myCode - 50) + " ");
        }
        System.out.print(" --> Método 12");
        System.out.println("");

    }

    private static void iterator13() {
        int i = 0;
        while (i < 2) {
            i++;
            System.out.print(i + " ");
            while (i < 3) {
                i++;
                System.out.print(i + " ");
                while (i < 4) {
                    i++;
                    System.out.print(i + " ");
                    while (i < 5) {
                        i++;
                        System.out.print(i + " ");
                        while (i < 10) {
                            i++;
                            System.out.print(i + " ");
                        }
                    }
                }
            }
        }
        System.out.print(" --> Método 13");
        System.out.println("");
    }

    private static void iterator14() {
        List<String> myList = new ArrayList<>();
        int a = 1, b = 11, c = b + a, d = b * 2, e = c + d, f = e + d, g = f + d, h = g / 2 - 30, i = (g + d) / 10;
        myList.add(c + "");
        myList.add(e + "");
        myList.add(f + "");
        myList.add(g + "");
        myList.add(h + "");
        myList.add(i + "");

        for (String element : myList) {
            for (int j = 0; j < element.length(); j++) {
                if (element.charAt(j) == '0') {
                    System.out.print("\b");
                }
                System.out.print(element.charAt(j) + " ");
            }
        }
        System.out.print(" --> Método 14");
        System.out.println("");
    }

}
