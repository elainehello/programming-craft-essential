package org.elainehello.operation;
import java.util.Scanner;

public class ConversionCoin {

    public double getConversionCoin(int coin) {
        double usdRate = 0.0045;

        return coin * usdRate;
    }
    public static void main(String[] args) {
        System.out.println("Enter coin to be converted to usd exchange: ");
        Scanner sc = new Scanner(System.in);
        int playerInput = sc.nextInt();
        ConversionCoin converCoin = new ConversionCoin();

        double result = converCoin.getConversionCoin(playerInput);
        System.out.println("Result: " + result);
        sc.close();
    }
}
