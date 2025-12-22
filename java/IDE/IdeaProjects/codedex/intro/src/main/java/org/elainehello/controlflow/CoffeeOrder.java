package org.elainehello.controlflow;

import java.util.Scanner;

public class CoffeeOrder {

    public static void main(String[] args) {
        boolean isLatte = true;
        boolean isIced = true;
        boolean withMatcha = true;
        int itemsOrdered, vanillaPumps;
        int option;
        /*
        e.g Integer option; or int option;
        - **Integer**: Object wrapper, can be `null`, has methods like `.equals()`, `.toString()`, etc.
        - **int**: Primitive type, cannot be `null`, uses operators like `==`, more memory efficient
        */
        Scanner sc = new Scanner(System.in);
        System.out.println("Order drink option:\n[1] Iced Latte\n[2] Latte Matcha\n[3] Latte");
        option = sc.nextInt();

        System.out.println("How many items ordered?");
        itemsOrdered = sc.nextInt();

        System.out.println("How many vanilla pumps");
        vanillaPumps = sc.nextInt();

        if (isIced && option == 1) {
            System.out.println("espresso, milk, ice, syrup.");
        } else if (withMatcha && option == 2) {
            System.out.println("matcha, oat milk, ice, vanilla.");
        } else if (isLatte && option == 3) {
            System.out.println("espresso, steamed milk.");
        }

        if (itemsOrdered > 1) {
            System.out.println("provide cup holder");
        }

        if (vanillaPumps >= 2) {
            System.out.println("charge 1$ extra");
        }
        sc.close();
    }
}
