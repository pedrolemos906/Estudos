import java.util.Locale;
import java.util.Scanner;


public class exercicio1 {

    public static void main(String[] args) {
        //criando o objeto scanner
        Scanner scanner = new Scanner(System.in).useLocale(Locale.US);


        //inserindo os dados
        System.out.println("digite seu nome:");
        String nome = scanner.next();
        System.out.println("digite sua idade:");
        int idade = scanner.nextInt();
        System.out.println("digite sua altura:");
        double altura = scanner.nextDouble();

        //exibindo os dados
        System.out.println("seu nome é: " + nome);
        System.out.println("sua idade é: " + idade);
        System.out.println("sua altura é: " + altura + "cm");
    }
}

        