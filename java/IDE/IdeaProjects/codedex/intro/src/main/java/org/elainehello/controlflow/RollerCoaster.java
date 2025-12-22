package org.elainehello.controlflow;

import java.util.Scanner;

public class RollerCoaster {

    public static void main(String[] args) {
        int weightLimit = 40;
        int heightLimit = 120;
        int responseWeight;
        int responseHeight;

        Scanner sc = new Scanner(System.in);
        System.out.println("Please enter weight: ");
        responseWeight = sc.nextInt();
        System.out.println("Enter your height: ");
        responseHeight = sc.nextInt();
        if (weightLimit <= responseWeight && heightLimit <= responseHeight) {
            System.out.println("Congrats! You can ride!");
        } else {
            System.out.println("Sorry, You can't ride today.");
        }
        sc.close();
    }

}
