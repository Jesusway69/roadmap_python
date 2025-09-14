package battle;

import battle.fighters.Character;

public class Battle {
    private Character fighter1;
    private Character fighter2;
    private Character skipTurn;
    private int round = 1;

    public Battle(Character f1, Character f2) {
        this.fighter1 = f1;
        this.fighter2 = f2;
    }

    public void start() throws InterruptedException {
        while (fighter1.isAlive() && fighter2.isAlive()) {
            System.out.println("\n--- Ronda " + round + " ---");
            turn(fighter1, fighter2);
            if (!fighter2.isAlive()) break;
            turn(fighter2, fighter1);
            round++;
            Thread.sleep(1000);
        }

        if (fighter1.isAlive()) {
            System.out.println(fighter1.getName() + " gana con " + fighter1.getLifePoints() + " puntos restantes");
        } else {
            System.out.println(fighter2.getName() + " gana con " + fighter2.getLifePoints() + " puntos restantes");
        }
    }

    private void turn(Character attacker, Character defender) {
        if (skipTurn == attacker) {
            System.out.println(attacker.getName() + " pierde su turno por tener que regenerarse.");
            skipTurn = null;
            return;
        }

        if (defender.evade()) {
            System.out.println(defender.getName() + " esquiva el ataque de " + attacker.getName());
            return;
        }

        int damage = attacker.attack();
        defender.receiveDamage(damage);
        System.out.println(attacker.getName() + " ataca con " + damage + " puntos de daño.");

        if (damage == attacker.maxDamage) {
            System.out.println("¡¡Ataque máximo de " + attacker.getName() + "!!");
            skipTurn = defender;
        }

        if (!defender.isAlive()) {
            System.out.println(defender.getName() + " se ha quedado sin puntos de vida.");
        } else {
            System.out.println(defender.getName() + " tiene ahora " + defender.getLifePoints() + " puntos.");
        }
    }
}
