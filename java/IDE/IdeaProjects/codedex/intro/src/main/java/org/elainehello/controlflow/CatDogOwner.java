package org.elainehello.controlflow;
import java.util.Scanner;

public class CatDogOwner {

    public static void DogOwner(boolean flag) {
        if (flag) 
            System.out.println("Use the code WOOF for 20% off dog items");
    }

    public static void CatOwner(boolean flag) {
        if (flag)
            System.out.println("Use the code MEOW for 20% off cat items.");
    }

    public static void main(String[] args) {

        boolean isCatOwner = true;
        boolean isDogOwner = true;
        String userResponse;
        Integer petOwner;

        System.out.println("Are you a pet (cat or dog) owner yes | no?");
        Scanner sc = new Scanner(System.in);
        userResponse = sc.nextLine();
        System.out.println("Do you own a cat or dog?\n type a number\n[1] cat\n[2] dog\n[0] none");
        petOwner = sc.nextInt();
        if (userResponse.toLowerCase().equals("yes") 
            && petOwner.equals(1)) {
            CatOwner(isCatOwner);
        } else if (userResponse.toLowerCase().equals("yes") 
            && petOwner.equals(2)) {
                DogOwner(isDogOwner);
        } else {
            System.out.println("Welcome to the pet store!");
        }
        sc.close();
    }
}
