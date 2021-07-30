package application;

import entities.Rectangle;

import java.util.Locale;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        Rectangle rect = new Rectangle();

        System.out.println("Enter rectangle width and height: ");
        rect.width = sc.nextDouble();
        rect.height = sc.nextDouble();

        System.out.printf("AREA = %.2f%n", rect.calculaArea());
        System.out.printf("PERIMETER = %.2f%n", rect.calculaPerimetro());
        System.out.printf("DIAGONAL = %.2f%n", rect.calculaDiagonal());
        sc.close();
    }
}