package reto_49;

import java.util.Scanner;

public class JesusWay69 {

    public static void main(String[] args) {
        char [][] myTree = createTree(5);
        showTree(myTree);
        topStar(myTree, true);
        showTree(myTree);
        topStar(myTree, false);
        showTree(myTree);
        Scanner sc = new Scanner(System.in);
        
        
        
        
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
        }else if(switchStar){
            tree[0][tree[0].length/2] = '@';
        }else{
            tree[0][tree[0].length/2] = '*';
        }
        

        return tree;
    }

}
