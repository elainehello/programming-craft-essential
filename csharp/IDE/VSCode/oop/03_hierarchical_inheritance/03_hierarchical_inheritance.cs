using System;

class Animal
{
    public void Eat()
    {
        Console.WriteLine("Animal is eating\n");
    }
}

// Derived class 1
class Cat : Animal
{
    public void Meow()
    {
        Console.WriteLine("Cat is meowing\n");
    }
}

// Derived class 2
class Dog : Animal
{
    public void Bark()
    {
        Console.WriteLine("Dog is barking\n");
    }
}

// Derived class 3
class Cow : Animal
{
    public void Moo()
    {
        Console.WriteLine("Cow is mooing");
    }
}

// main
class Program
{
    static void Main()
    {
        Cat cat = new Cat();
        cat.Eat();
        cat.Meow();

        Dog dog = new Dog();
        dog.Eat();
        dog.Bark();

        Cow cow = new Cow();
        cow.Eat();
        cow.Moo();

    }
}