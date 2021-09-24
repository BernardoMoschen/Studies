package entities;

public class Rectangle {
    public double width;
    public  double height;

    public double calculaArea(){
        return width * height;
    }
    public double calculaPerimetro(){
        return 2 * (width + height);
    }

    public double calculaDiagonal(){
        return Math.sqrt(width * width + height * height);
    }
}
