using System;

class Calculator
{
    public int Add(int a, int b)
    {
        return a + b;
    }

    public double Add(double a, double b)
    {
        return a + b;
    }

    public int Add(int a, int b, int c)
    {
        return a + b + c;
    }
}

class Program
{
    static void Main(string[] args)
    {
        Calculator calc = new Calculator();

        Console.WriteLine("Calls Add(int, int)\t\t" + calc.Add(1, 9));
        Console.WriteLine("Calls Add(double, double)\t" + calc.Add(41.0, 1.0));
        Console.WriteLine("Calls Add(int, int, int)\t" + calc.Add(4, 4, 4));
    }
}