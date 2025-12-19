/*
NoInfer prevents TypeScript from inferring types in certain generic positions,
forcing explicit type specification for better type safety and control.
*/

class Pet {
    sleep() {}
}

class Kitten extends Pet {
    Meow() {}
}

function petAnimal<T>(value: T, getDefault: () => T): T {
    // ...function logic
    return value || getDefault()
}

petAnimal(new Kitten(), () => new Pet())