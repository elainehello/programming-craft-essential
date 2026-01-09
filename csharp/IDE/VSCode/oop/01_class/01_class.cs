using System;

namespace OopExercises
{
    public enum PetColor
    {
        Brown,
        Black,
        White,
        Golden
    }

    public class PetAnimal
    {
        // attributes
        private readonly string PetName;
        private readonly PetColor PetColor;

        // constructor
        public PetAnimal(string petName, PetColor petColor)
        {
            PetName = petName;
            PetColor = petColor;
        }

        public string MyPet() => $"My pet is {PetName} and its color is {PetColor}";

        static void Main()
        {
            Console.WriteLine("OOP Exercises");
            PetAnimal pet = new PetAnimal("CareyFurry", PetColor.Brown);
            Console.WriteLine(pet.MyPet());
            Console.ReadLine();
            PetAnimal dog = new PetAnimal("Sparkle", PetColor.Golden);
            Console.WriteLine(dog.MyPet());
            Console.ReadLine();
            PetAnimal rabbit = new PetAnimal("SnowFlake", PetColor.White);
            Console.WriteLine(rabbit.MyPet());
            Console.ReadLine();
        }

    }

    
}

