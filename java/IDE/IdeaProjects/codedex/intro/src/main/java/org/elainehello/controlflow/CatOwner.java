package org.elainehello.controlflow;

import java.util.Scanner;

/*
The pet store wants to send you a coupon if you're a cat owner! 🐈

Write a program with a isCatOwner variable, either true or false.

If true, print “20% off select cat items with code MEOW2025”.

Otherwise, print a generic “Welcome to the Pets Pets Pets store!” message.
*/
public class CatOwner {

    public static void getDiscount() {
        System.out.println("20% off select cat items with code MEOW2025");
    }
    
    public boolean boolCatOwner(String answer) {

        if (answer.toLowerCase().equals("yes")) {
            return true;
        } else if (answer.toLowerCase().equals("no")) {
            return false;
        } else {
            System.out.println("Invalid input. Please answer 'yes' or 'no'");
            return false;
        }
    }
    
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Hello, what's your name: ");
        String name = sc.nextLine();
        System.out.println("Nice to meet you " + name);

        System.out.println("Are you a cat owner please answer, yes or no");
        String userAnswer = sc.nextLine();

        CatOwner catOwner = new CatOwner();
        boolean boolAnswer = catOwner.boolCatOwner(userAnswer);
        
        if (boolAnswer) {
            getDiscount();
        } else {
            System.out.println("Welcome to the Pets Pets Pets store!");
        }

        sc.close();
    }
}
