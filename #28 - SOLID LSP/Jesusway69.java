package roadmap.ejercicio28
/*
 * EJERCICIO:
 * Explora el "Principio SOLID de Sustitución de Liskov (Liskov Substitution Principle, LSP)" 
 * y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.
 *
 */
public class Jesusway69 {

    public static void main(String[] args) {
        Figure1 rectangle = new Figure1();
        Rectangle1 rectangle1 = new Rectangle1();
        Square1 square1 = new Square1();
        Rectangle2 rectangle2 = new Rectangle2(2, 9);
        Square2 square2 = new Square2(5);
        Circle2 circle2 = new Circle2(4);
        Car car = new Car();
        Motorcycle motorcycle = new Motorcycle();
        Truck truck = new Truck();
        System.out.println("rectangle1 = " + rectangle1.calculateArea(4, 2));
        System.out.println("rectangle = " + rectangle.calculateArea(3, 5));
        System.out.println("square1 = " + square1.calculateArea(4, 6));
        System.out.println("rectangle2 = " + rectangle2.calculateArea());
        System.out.println("square2 = " + square2.calculateArea());
        System.out.println("circle2 = " + circle2.calculateArea());
        System.out.println("car = " + car.accelerate());
        vehicleTest(car);
        vehicleTest(motorcycle);
        vehicleTest(truck);

    }

    public static void vehicleTest(Object object) {
        String name = "";
        boolean accelerate = false;
        if (object instanceof Car) {
            name = ((Car) object).name;
            accelerate = ((Car) object).accelerate();
        } else if (object instanceof Motorcycle) {
            name = ((Motorcycle) object).name;
            accelerate = ((Motorcycle) object).accelerate();
        } else if (object instanceof Truck) {
            name = ((Truck) object).name;
            accelerate = ((Truck) object).accelerate();
        }

        System.out.println("El Vehículo " + name + " acelera?: " + accelerate);

    }

}

class Figure1 {

    public int base;
    public int height;

    public Figure1() {
    }

    public Figure1(int base, int height) {
        this.base = base;
        this.height = height;
    }

    protected int calculateArea(int base, int height) {

        return base * height;
    }
}

class Rectangle1 extends Figure1 {

    public Rectangle1() {
    }

    public Rectangle1(int base, int height) {
        super.base = base;
        super.height = height;
        super.calculateArea(super.base, super.height);

    }
}

class Square1 extends Figure1 {

    public Square1() {
    }

    @Override
    protected int calculateArea(int base, int height) {
        return base * base;
    }
}

abstract class Figure2 {

    public abstract double calculateArea();
}

class Rectangle2 extends Figure2 {

    public int base2;
    public int height2;

    public Rectangle2() {

    }

    public Rectangle2(int base2, int height2) {
        this.base2 = base2;
        this.height2 = height2;
    }

    @Override
    public double calculateArea() {
        return base2 * height2;
    }

}

class Square2 extends Figure2 {

    public int side2;

    public Square2() {
    }

    public Square2(int side2) {
        this.side2 = side2;
    }

    @Override
    public double calculateArea() {
        return side2 * side2;

    }
}

class Circle2 extends Figure2 {

    public int radius;

    public Circle2() {
    }

    public Circle2(int radius) {
        this.radius = radius;
    }

    @Override
    public double calculateArea() {
        return Math.round(Math.pow(radius, 2) * Math.PI * 100d) / 100d;
    }

}

/*
 * DIFICULTAD EXTRA (opcional):
 * Crea una jerarquía de vehículos. Todos ellos deben poder acelerar y frenar, así como
 * cumplir el LSP.
 * Instrucciones:
 * 1. Crea la clase Vehículo.
 * 2. Añade tres subclases de Vehículo.
 * 3. Implementa las operaciones "acelerar" y "frenar" como corresponda.
 * 4. Desarrolla un código que compruebe que se cumple el LSP.
 */
class Vehicle {

    public String name;
    public boolean accelerate = true;
    public boolean brake = true;

    public Vehicle() {

    }

    public boolean accelerate() {
        return accelerate;
    }

    public boolean brake() {
        return brake;
    }

}

class Car extends Vehicle {

    public String name;

    public Car() {
        this.name = "coche";

    }

    @Override
    public boolean accelerate() {
        return accelerate;
    }

    @Override
    public boolean brake() {
        return brake;
    }

}

class Motorcycle extends Vehicle {

    public String name;

    public Motorcycle() {
        this.name = "moto";
    }

    @Override
    public boolean accelerate() {
        return accelerate;
    }

    @Override
    public boolean brake() {
        return brake;
    }

}

class Truck extends Vehicle {

    public String name;

    public Truck() {
        this.name = "camión";
    }

    @Override
    public boolean accelerate() {
        return accelerate;
    }

    @Override
    public boolean brake() {
        return brake;
    }

}
