package ejercicio29;


/*
 * EJERCICIO:
 * Explora el "Principio SOLID de Segregación de Interfaces
 * (Interface Segregation Principle, ISP)", y crea un ejemplo
 * simple donde se muestre su funcionamiento de forma correcta e incorrecta.
 */
public class JesusWay69 {

    public static void main(String[] args) {
        OstrichISP ostrich = new OstrichISP();
        SwiftISP swift = new SwiftISP();
        PenguinISP penguin = new PenguinISP();

    }

}

/*
La siguiente interfaz no cumple el principio de segregación de interfaces ya que modela el contenido
de las diferentes clases de aves con todas las características de las cuales solo la primera (tiene plumas)
es común a todas las aves pero no las demás que aun así es obligatorio declarar sus métodos en todas las clases
además la constante que debemos devolver en cada método está seteada en true con lo cual en los métodos cuya
característica no cumpla el ave debemos forzar la salida retornando false.
 */

interface Bird {

    boolean haveFeathers();

    boolean flies();

    boolean swims();

    boolean run();
    final boolean CHARACTERISTIC = true;
}

class Ostrich implements Bird {

    @Override
    public boolean haveFeathers() {
        return CHARACTERISTIC;
    }

    @Override
    public boolean flies() {
        return false;
    }

    @Override
    public boolean swims() {
        return false;
    }

    @Override
    public boolean run() {
        return CHARACTERISTIC;
    }

}

class swift implements Bird {

    @Override
    public boolean haveFeathers() {
        return CHARACTERISTIC;
    }

    @Override
    public boolean flies() {
        return CHARACTERISTIC;
    }

    @Override
    public boolean swims() {
        return false;
    }

    @Override
    public boolean run() {
        return false;

    }
}

class Penguin implements Bird {

    @Override
    public boolean haveFeathers() {
        return CHARACTERISTIC;
    }

    @Override
    public boolean flies() {
        return false;
    }

    @Override
    public boolean swims() {
        return CHARACTERISTIC;
    }

    @Override
    public boolean run() {
        return true;
    }
}

interface BirdISP {

    boolean haveFeathersISP();

    String birdName();
    final boolean CHARACTERISTICISP = true;

}

interface FlyingBirdISP {

    boolean fliesISP();
}

interface SwimmingBirdISP {

    boolean swimsISP();
}

interface RunnerBirdISP {

    boolean run();
}

class OstrichISP implements BirdISP, RunnerBirdISP {

    @Override
    public boolean run() {
        return CHARACTERISTICISP;
    }

    @Override
    public boolean haveFeathersISP() {
        return CHARACTERISTICISP;
    }

    @Override
    public String birdName() {
        return "Avestruz";
    }

}

class PenguinISP implements BirdISP, SwimmingBirdISP, RunnerBirdISP {

    @Override
    public boolean haveFeathersISP() {
        return CHARACTERISTICISP;
    }

    @Override
    public boolean swimsISP() {
        return CHARACTERISTICISP;
    }

    @Override
    public boolean run() {
        return CHARACTERISTICISP;
    }

    @Override
    public String birdName() {
        return "Pingüino";
    }

}

class SwiftISP implements BirdISP, FlyingBirdISP {

    @Override
    public boolean haveFeathersISP() {
        return CHARACTERISTICISP;
    }

    @Override
    public boolean fliesISP() {
        return CHARACTERISTICISP;
    }

    @Override
    public String birdName() {
        return "Vencejo";
    }

}

/*
 * DIFICULTAD EXTRA (opcional):
 * Crea un gestor de impresoras.
 * Requisitos:
 * 1. Algunas impresoras sólo imprimen en blanco y negro.
 * 2. Otras sólo a color.
 * 3. Otras son multifunción, pueden imprimir, escanear y enviar fax.
 *  Instrucciones:
 * 1. Implementa el sistema, con los diferentes tipos de impresoras y funciones.
 * 2. Aplica el ISP a la implementación.
 * 3. Desarrolla un código que compruebe que se cumple el principio.
 */
