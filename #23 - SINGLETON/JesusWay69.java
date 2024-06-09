package ejercicio23;

/*
* EJERCICIO:
 * Explora el patrón de diseño "singleton" y muestra cómo crearlo
 * con un ejemplo genérico.
 */
public class JesusWay69 {

    private static JesusWay69 jesusway69;// Variable estática para recibir la unica instancia del Singleton

    private JesusWay69() {
        System.out.println("Creando objeto...");
    }

    public static JesusWay69 getJesusway69() {

        if (jesusway69 == null) { //Condicional para crear la instancia si es null
            jesusway69 = new JesusWay69();//en caso de ser la primera vez es null y se llama al constructor
        }
        return jesusway69;// Retorna el objeto único creado
    }

    public static void main(String[] args) {
        JesusWay69 instance1 = JesusWay69.getJesusway69();//Creamos un objeto instancia1
        JesusWay69 instance2 = JesusWay69.getJesusway69();// y otro objeto instancia2
        System.out.println("Instancia1 = " + instance1);//Observamos que el objeto generado en esta instancia
        System.out.println("Instancia2 = " + instance2);// es el mismo que el generado en la siguiente instancia

        Session session = Singleton.getInstance(1, "Jesusway69", "Jesus", "jesusway60@midominio.es");
        Session session2 = Singleton.getInstance(2, "Pepe84", "Jose", "pepepepe@midominio.es");
        
        System.out.println("Nombre2 = "+ session2.getName());
        int id = session.getId();
        
        String username = session.getUsername();
        String name = session.getName();
        String email = session.getEmail();
        System.out.println("\nSesión = " + session);
        System.out.println("ID = " + id);
        System.out.println("Name = " + name);
        System.out.println("Username = " + username);
        System.out.println("email = " + email);
        Session close = Singleton.deleteInstance();
        System.out.println("Sesión = " + close);

    }

}


/*
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el patrón de diseño "singleton" para representar una clase que
 * haga referencia a la sesión de usuario de una aplicación ficticia.
 * La sesión debe permitir asignar un usuario (id, username, nombre y email),
 * recuperar los datos del usuario y borrar los datos de la sesión.
 */
class Session {

    public int id;
    public String username;
    public String name;
    public String email;

    public Session() {
    }

    public Session(int id, String username, String name, String email) {
        this.id = id;
        this.username = username;
        this.name = name;
        this.email = email;

    }

    public int getId() {
        return id;
    }

    public String getUsername() {
        return username;
    }

    public String getName() {
        return name;
    }

    public String getEmail() {
        return email;
    }

}

class Singleton {

    private static Session session = null;

    public synchronized static Session getInstance(int i, String u, String n, String e) {
        if (session == null) {
            session = new Session(i,u,n,e); // instar el Singleton si no hay todavía
        }
        return session;
    }

    public synchronized static Session deleteInstance() {
        if (session != null) {
            session = null;
        }

        return session;
    }

}
