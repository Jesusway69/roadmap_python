package ejercicio09;

/*
* EJERCICIO:
 * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
 * implemente una superclase Animal y un par de subclases Perro y Gato,
 * junto con una función que sirva para imprimir el sonido que emite cada Animal.
 */
public class JesusWay69 {

    public static void main(String[] args) {
        Animal animal = new Animal();
        Perro perro = new Perro();
        Gato gato = new Gato();
        Vaca vaca = new Vaca();
        Empleado empleado = new Empleado();
        Gerente gerente = new Gerente();

        animal.print(perro.sonido, perro.animal);
        perro.print(perro.animal, perro.sonido);
        gato.print(gato.sonido, gato.animal);
        vaca.print(vaca.sonido, vaca.animal);
        System.out.println("");
        empleado.print(0, "Luis", "Gerente");
        gerente.print(1, "Paco", "Gerente");
        

    }

}

class Animal {

    public String animal;
    public String sonido;
    private String articulo;

    public Animal() {
        //animal = "";
        //sonido = "";
        articulo = "El";
    }

    public void print(String sonido, String animal) {
        if (animal.charAt(animal.length() - 1) == 'a') {
            articulo = "La";
        }
        System.out.println(articulo + " " + animal + " " + sonido);

    }

}

class Perro extends Animal {

    public Perro() {
        super();
        this.animal = "perro";
        this.sonido = "ladra";
    }

    @Override
    public void print(String sonido, String animal) {
        super.print("ladra", "perro");
    }

}

class Gato extends Animal {

    public Gato() {
        super();
        this.animal = "gato";
        this.sonido = "maulla";
    }
}

class Vaca extends Animal {

    public Vaca() {
        super();
        this.animal = "vaca";
        this.sonido = "muge";
    }
}


/*
 * DIFICULTAD EXTRA (opcional):
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo.
 */
class Empleado {

    public String finanzas = "NO";
    public String compras = "NO";
    public String proyectos = "NO";
    public String organizacion = "NO";
    public String programacion = "NO";
    public String despliegue = "NO";
    public int id;
    public String nombre;
    public String cargo;

    public Empleado() {

    }

    public Empleado(int id, String nombre, String cargo) {
        this.id = id;
        this.nombre = nombre;
        this.cargo = cargo;
    }

    public void print(int id, String nombre, String cargo) {
        System.out.println("\nID: " + id + "\nnombre: " + nombre + "\ncargo: " + cargo + "\nHace finanzas? " + finanzas
                + "\nHace compras? " + compras + "\nHace proyectos? " + proyectos + "\nOrganiza el trabajo? " + organizacion
                + "\nPica código? " + programacion + "\nDespliega programas? " + despliegue);

    }

}

class Gerente extends Empleado{

    public Gerente() {
        super();
        this.compras = "SI";
        this.finanzas = "SI";
    }

   // public Gerente(int id, String nombre, String cargo) {
        //super(id, nombre, cargo);
   // }
    
    
    
    
}
