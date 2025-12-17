/*
Abstract classes serve as templates for subclasses and cannot be directly instantiated.
They define abstract methods (without implementation) that subclasses must implement
to provide specific functionality. This enforces a common interface across derived classes.
*/

abstract class Animal {
    abstract makeSound(): void;
}

class Dog extends Animal {
    makeSound(): void {
        console.log("Woof!");
    }
}

class Cat extends Animal {
    makeSound(): void {
        console.log("Meow!")
    }
}