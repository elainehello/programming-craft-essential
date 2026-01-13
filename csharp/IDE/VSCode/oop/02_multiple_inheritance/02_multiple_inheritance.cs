using System;

interface IShape
{
    double GetArea();
}

interface IColor
{
    string GetColor();
}

class Rectangle : IShape, IColor
{
    // attributes
    private double length;
    private double width;
    private string color;

    // constructor
    public Rectangle(double length, double width, string color)
    {
        this.length = length;
        this.width = width;
        this.color = color;
    }

    public double GetArea()
    {
        return length * width;
    }

    public string GetColor()
    {
        return color;
    }
}

class Program
{
    static void Main(string[] args)
    {
        Rectangle rect = new Rectangle(8, 4, "Peach");
        // concatenation
        Console.WriteLine("Area of Rectangle: " + rect.GetArea());
        Console.WriteLine("Color of Rectangle: " + rect.GetColor());

    }
}