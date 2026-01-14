using System;

class Shape
{
    public virtual void Draw()
    {
        Console.WriteLine("Drawing shape");
    }
}

// Derived class
class Circle : Shape
{
    public override void Draw()
    {
        Console.WriteLine("Drawing circle");
    }
}

// Derived class
class Rectangle : Shape
{
    public override void Draw()
    {
        Console.WriteLine("Drawing rectangle");
    }
}

// main
class Program
{
    static void Main()
    {
        // Base class reference pointing to derived objects
        Shape shape1 = new Circle();
        Shape shape2 = new Rectangle();

        shape1.Draw(); // Calls Circle.Draw() at runtime
        shape2.Draw(); // Calls Rectangle.Draw() at runtime
    }
}