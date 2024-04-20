package ejercicio16;

/*
 * EJERCICIO:
 * Utilizando tu lenguaje, explora el concepto de expresiones regulares,
 * creando una que sea capaz de encontrar y extraer todos los números
 * de un texto.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea 3 expresiones regulares (a tu criterio) capaces de:
 * - Validar un email.
 * - Validar un número de teléfono.
 * - Validar una url.
 */
public class JesusWay69 {

    public static void main(String[] args) {
        String text = "Un año tiene 365 días excepto si es bisiesto que tiene 366 divididos en 12 meses que pueden tener hasta 31 días cada uno.";
        char[] characters = text.toCharArray();
        String nums = "";
        for (int i = 0; i < characters.length; i++) {
            nums = Character.toString(characters[i]);
            if (nums.matches("\\d") == true) {
                System.out.print(nums + " ");
            }

        }
        System.out.println("\n"+emailValidation("jesu.sw.ay69@hotmail.com"));
        System.out.println("\n"+spainPhoneNumberValidation("+34716994941"));
        System.out.println("\n"+ urlValidation("www.moure.dev"));
    }

    private static boolean emailValidation(String email) {
        email = email.toLowerCase();
        return email.matches("[a-z0-9\\.]+(@)[a-z0-9]+\\.[a-z]{2,3}");
    }
    private static boolean spainPhoneNumberValidation(String phoneNumber){
        return phoneNumber.matches("[9||7||6][0-9]{8}||(\\+34)[9||7||6][0-9]{8}");
    }
    private static boolean urlValidation(String url){
        return url.matches("[a-z]{1,63}\\.[a-z]+||(www)\\.[a-z]{1,63}\\.[a-z]+");
    }
}
