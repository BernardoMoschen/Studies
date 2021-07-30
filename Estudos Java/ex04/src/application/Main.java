package application;

import entities.Employee;

import java.util.Locale;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        Employee funcionario = new Employee();

        System.out.println("Enter the employee data: ");
        System.out.print("Name: ");
        funcionario.name = sc.nextLine();
        System.out.print("Gross Salary: ");
        funcionario.grossSalary = sc.nextDouble();
        System.out.print("Tax: ");
        funcionario.tax = sc.nextDouble();

        System.out.println();
        System.out.println("Employee: " + funcionario);
        System.out.println();

        System.out.print("Which percentage to increase salary? ");
        double percentage = sc.nextDouble();
        funcionario.increaseSalary(percentage);

        System.out.println();
        System.out.println("Updated data: " + funcionario);
        sc.close();
    }
}