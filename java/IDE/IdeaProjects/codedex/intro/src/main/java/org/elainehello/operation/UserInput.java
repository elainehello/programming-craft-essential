package org.elainehello.operation;
import java.util.Scanner;

public class UserInput {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter your name: ");
        String userInput = sc.nextLine();
        System.out.println(userInput);
        sc.close();
    }
}
