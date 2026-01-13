using System;

// Base class (lvl 1) parent
class Vehicle
{
    public void Start()
    {
        Console.WriteLine("Vehicle is starting\n");
    }
}

// Derived class (lvl 2)
class Car : Vehicle
{
    public void Drive()
    {
        Console.WriteLine("Car is driving\n");
    }
}

// Derived class (lvl 3)
class ElectricCar : Car
{
    public void Charge()
    {
        Console.WriteLine("Car is charging\n");
    }
}

// main
class Program
{
    static void Main(string[] args)
    {
        ElectricCar tesla = new ElectricCar();
        tesla.Start(); // From Vehicle
        tesla.Drive(); // From Car
        tesla.Charge(); // From ElectricCar
    }
}