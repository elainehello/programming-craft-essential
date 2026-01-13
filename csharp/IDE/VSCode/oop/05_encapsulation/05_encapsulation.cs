using System;
using System.Collections.Generic;
using System.Security.Cryptography.X509Certificates;

class PetAnimal
{
    public string Name { get; }

    public PetAnimal(string name)
    {
        Name = name;
    }

}

// PetOwner class (encapsulates Pets)
class PetOwner
{
    // Restricted: cannot be accessed directly from outside
    private List<PetAnimal> pets = new List<PetAnimal>();

    // public method to control how pets are addeed
    public void AddPet(PetAnimal pet)
    {
        if (pet == null)
            throw new ArgumentNullException(nameof(pet));

        pets.Add(pet);
        Console.WriteLine($"{pet.Name} added to owner.\n");
    }

    // Optional: Read-only access (still encapsulated)
    public IReadOnlyList<PetAnimal> Pets => pets.AsReadOnly();
}

class Program
{
    static void Main()
    {
        PetOwner owner = new PetOwner();

        PetAnimal dog = new PetAnimal("Shakespeare");
        PetAnimal cat = new PetAnimal("SweetCarey");

        owner.AddPet(dog);
        owner.AddPet(cat);

        /*
        Not allowed - pets list is privare
            owner.pets.Add(dog)
        */

        // Allowed - read-only access
        foreach (var pet in owner.Pets)
        {
            Console.WriteLine(pet.Name);
        }
    }
}