package ejercicio15;

import java.time.Instant;
import java.time.LocalTime;
import java.time.temporal.ChronoUnit;

/*
 * Utilizando tu lenguaje, crea un programa capaz de ejecutar de manera
 * asíncrona una función que tardará en finalizar un número concreto de segundos
 * parametrizables. También debes poder asignarle un nombre. La función imprime
 * su nombre, cuándo empieza, el tiempo que durará su ejecución y cuando
 * finaliza.
 */
public class JesusWay69 {

    public static void main(String[] args) throws InterruptedException {
        asynchrone(4, "Hola mundo");
        parallelFuntcions();
    }

     static void asynchrone(int waitSeconds, String name) throws InterruptedException {
        LocalTime startTime = LocalTime.now();
        System.out.println("La ejecución de '" + name + "' durará " + waitSeconds + " segundos");
        System.out.println("La ejecución comienza a las " + LocalTime.now().getHour() + ":" + LocalTime.now().getMinute() + ":" + LocalTime.now().getSecond());
        Thread.sleep(waitSeconds * 1000);
        System.out.println("Ejecución terminada a las " + LocalTime.now().getHour() + ":" + LocalTime.now().getMinute() + ":" + LocalTime.now().getSecond());
        LocalTime endTime = LocalTime.now();
        System.out.println("Duración de la ejecución: " + ChronoUnit.SECONDS.between(startTime, endTime) + " segundos.");

    }

    /*
    
     */
     static void C() throws InterruptedException {
        System.out.println("Función C iniciada a las: " + LocalTime.now().getHour() + ":" + LocalTime.now().getMinute() + ":" + LocalTime.now().getSecond());
        Thread.sleep(3000);
        System.out.println("Función C terminada a las: " + LocalTime.now().getHour() + ":" + LocalTime.now().getMinute() + ":" + LocalTime.now().getSecond());
        D();
    }

     static void B() throws InterruptedException {
        System.out.println("Función B iniciada a las: " + LocalTime.now().getHour() + ":" + LocalTime.now().getMinute() + ":" + LocalTime.now().getSecond());
        Thread.sleep(2000);
        System.out.println("Función B terminada a las: " + LocalTime.now().getHour() + ":" + LocalTime.now().getMinute() + ":" + LocalTime.now().getSecond());
    }

     static void A() throws InterruptedException {
        System.out.println("Función A iniciada a las: " + LocalTime.now().getHour() + ":" + LocalTime.now().getMinute() + ":" + LocalTime.now().getSecond());
        Thread.sleep(1000);
        System.out.println("Función A terminada a las: " + LocalTime.now().getHour() + ":" + LocalTime.now().getMinute() + ":" + LocalTime.now().getSecond());
    }

     static void D() throws InterruptedException {
        System.out.println("Función D iniciada a las: " + LocalTime.now().getHour() + ":" + LocalTime.now().getMinute() + ":" + LocalTime.now().getSecond());
        Thread.sleep(1000);
        System.out.println("Función D terminada a las: " + LocalTime.now().getHour() + ":" + LocalTime.now().getMinute() + ":" + LocalTime.now().getSecond());
    }
    static void parallelFuntcions() throws InterruptedException{
        C();
        B();
        A();
    }
}
