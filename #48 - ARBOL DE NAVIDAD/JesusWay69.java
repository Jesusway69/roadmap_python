package reto_49;

import java.util.Scanner;

public class JesusWay69 {

    public static void main(String[] args) {
        //char [][] myTree = createTree(5);
        /*showTree(myTree);
        topStar(myTree, true);
        showTree(myTree);
        topStar(myTree, false);
        showTree(myTree);*/
        char[][] myTree = null;

        do {
            Scanner sc = new Scanner(System.in);
            System.out.println("""
              1- Crear árbol
              2- Añadir estrella 
              3- Eliminar estrella 
              4- Añadir 2 bolas aleatoriamente
              5- Quitar todas las bolas
              6- Añadir 3 luces aleatoriamente 
              7- Encender las luces
              8- Apagar las luces
                             """);
            System.out.print("Elija una opción: ");
            Byte option = sc.nextByte();
            if (option>8 || option <1 || option instanceof Byte == false){
                System.out.println("El dato tiene que ser numérico del 1 al 8");
            }
            switch (option) {
                case 1:
                    System.out.println("Introduzca la altura del árbol (mayor de 3): ");
                    int hight = sc.nextInt();
                    myTree = createTree(hight);
                    showTree(myTree);
                    break;
                case 2:
                    topStar(myTree, true);
                    showTree(myTree);
                    break;
                case 3:
                    topStar(myTree, false);
                    showTree(myTree);
                    break;
                case 4:
                    addBalls(myTree);
                    showTree(myTree);
                    break;
                case 5:
                case 6:
                case 7:
                case 8:
                default:

            }
        } while (true);
    }

    public static char[][] createTree(int files) {
        int columns = files * 2 - 1;
        int branch = 1;
        char[][] tree = new char[files + 2][columns];

        if (files <= 3) {
            System.out.println("No se puede crear un árbol de menos de 4 alturas");
            tree = null;
            return tree;
        }

        for (int i = 0; i < files; i++) {
            for (int j = 0; j < columns / 2; j++) {
                tree[i][j] = ' ';

            }
            for (int k = columns / 2; k < columns / 2 + branch; k++) {
                tree[i][k] = '*';

            }
            for (int l = columns / 2 + branch; l < files * 2 - 1; l++) {
                tree[i][l] = ' ';

            }
            columns -= 2;
            branch += 2;
        }
        columns = files * 2 - 1;
        for (int m = 0; m < 2; m++) {
            for (int n = 0; n < files - 2; n++) {
                tree[files + m][n] = ' ';

            }
            for (int p = files - 2; p < files + 1; p++) {
                tree[files + m][p] = '|';

            }
            for (int q = files + 1; q < files * 2 - 1; q++) {
                tree[files + m][q] = ' ';

            }

        }
        //System.out.println(Arrays.deepToString(tree));
        return tree;
    }

    public static void showTree(char[][] tree) {
        int i = 0;
        for (char[] branch : tree) {
            i++;
            for (char c : branch) {
                System.out.print(c);
            }
            System.out.println();

        }
    }

    public static char[][] topStar(char[][] tree, boolean switchStar) {
        if (tree == null) {
            System.out.println("ERROR: Hay que crear un árbol antes de poder modificarlo (opción 1)");
            return null;
        } else if (switchStar) {
            tree[0][tree[0].length / 2] = '@';
        } else {
            tree[0][tree[0].length / 2] = '*';
        }

        return tree;
    }

    public static char[][] addBalls(char[][] tree) {

        for (int i = 0; i < 2; i++) {
            int randomFile = (int) (Math.random() * tree.length - 2 + 1);
            int randomColumn = (int) (Math.random() * tree[0].length);
            if (tree[randomFile][randomColumn] == '*') {
                tree[randomFile][randomColumn] = 'O';
            } else {
                i--;
            }
        }
        return tree;
    }

}
