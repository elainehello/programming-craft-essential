/* 
Concrete classes are standard classes that can be directly instantiated to create objects.
They define properties and methods that implement the desired behavior.
*/

class User {
    constructor(private readonly name: string) {
        this.name = name
    }

    public getName(): string {
        return this.name
    }
}

const user = new User("Elaine")
console.log(user.getName()) // output: Elaine
