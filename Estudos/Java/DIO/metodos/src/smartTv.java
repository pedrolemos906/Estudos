public class smartTv {
    boolean ligada = false;
    int canal = 1;
    int volume = 25;

//Volume
    public void aumentarVolume() {
        volume++;
        System.out.println("aumentando volume para: " + volume);
    }
    public void diminurirVolume() {
        volume--;
        System.out.println("diminuindo volume para: " + volume);
    }

//Canal
    public void mudarCanal(int novoCanal) {
        canal = novoCanal;
        System.out.println("mudando canal para: " + canal);
    }
    public void aumentarCanal() {
        canal++;
        System.out.println("aumentando canal para: " + canal);
    }
    public void diminuirCanal() {
        canal--;
        System.out.println("diminuindo canal para: " + canal);
    }

//ligar e deligar
    public void ligar() {
        ligada = true;
    }

    public void deligar() {
        ligada = false;
    }
}