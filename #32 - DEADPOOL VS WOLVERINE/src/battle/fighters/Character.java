package battle.fighters;

import java.util.Random;

public abstract class Character {
    protected String name;
    public int maxDamage;
    protected int shield;
    protected int lifePoints;
    protected Random random = new Random();

    public Character(String name, int maxDamage, int shield) {
        this.name = name;
        this.maxDamage = maxDamage;
        this.shield = shield;
    }

    public void setLifePoints(int points) {
        this.lifePoints = points;
    }

    public boolean isAlive() {
        return lifePoints > 0;
    }

    public String getName() {
        return name;
    }

    public int getLifePoints() {
        return lifePoints;
    }


    public int attack() {
        return random.nextInt(maxDamage - 10 + 1) + 10;
    }

   
    public boolean evade() {
        return random.nextInt(100) < shield;
    }

    public void receiveDamage(int damage) {
        lifePoints -= damage;
    }
}
