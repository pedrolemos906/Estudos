public class exemplo2 {
    public static void main(String[] args) {
        int numeroUm = 1;
        int numeroDois = 2;

        boolean simNao = numeroUm == numeroDois;

        System.out.println("O primeiro numero e igual ao segundo? " + simNao);

        simNao = numeroUm != numeroDois;

        System.out.println("O primeiro numero e diferente do segundo? " + simNao);

        if (numeroUm < numeroDois)
            System.out.println("O primeiro numero e menor que o segundo");
        else
            System.out.println("O primeiro numero e maior que o segundo");

        
    }
}
