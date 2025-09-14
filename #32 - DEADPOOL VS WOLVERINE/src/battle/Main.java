package battle;

import java.util.Scanner;
import battle.fighters.*;

public class Main {
    public static void main(String[] args) throws InterruptedException {
        Scanner sc = new Scanner(System.in);

        Deadpool deadpool = new Deadpool();
        Wolverine wolverine = new Wolverine();

        System.out.print("Introduce la vida inicial de Deadpool: ");
        deadpool.setLifePoints(sc.nextInt());

        System.out.print("Introduce la vida inicial de Wolverine: ");
        wolverine.setLifePoints(sc.nextInt());

        Battle battle = new Battle(deadpool, wolverine);
        battle.start();

        sc.close();
    }
}
