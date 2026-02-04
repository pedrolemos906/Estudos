public class usuario {
    public static void main(String[] args) throws Exception {
        
        smartTv smartTv = new smartTv();

        smartTv.ligar();
        smartTv.aumentarVolume();
        smartTv.aumentarVolume();
        smartTv.diminurirVolume();
        smartTv.aumentarCanal();
        smartTv.mudarCanal(10);

        System.out.println("tv ligada? : " + smartTv.ligada);
        System.out.println("canal atual : " + smartTv.canal);
        System.out.println("volume atual : " + smartTv.volume);


        smartTv.ligar();
        System.out.println("tv ligada? : " + smartTv.ligada);


        smartTv.deligar();
        System.out.println("tv ligada? : " + smartTv.ligada);



    }
}
