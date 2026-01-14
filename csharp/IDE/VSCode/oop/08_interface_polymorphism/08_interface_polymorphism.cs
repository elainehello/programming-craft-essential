using System;

interface IPayment
{
    void Pay(decimal amount);
}

// Implementation 1
class DebitCardPayment : IPayment
{
    public void Pay(decimal amount)
    {
        Console.WriteLine($"Paid {amount} using Debit Card");
    }
}

// Implementation 2
class PaypalPayment : IPayment
{
    public void Pay(decimal amount)
    {
        Console.WriteLine($"Paid {amount} using Paypal");
    }
}

// main
class Program
{
    static void Main()
    {
        IPayment payment;

        payment = new DebitCardPayment();
        payment.Pay(50);

        payment = new PaypalPayment();
        payment.Pay(65);
    }
}