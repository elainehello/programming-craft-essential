/*
Intersection types combine multiple types into one using the & (ampersand) operator.
The resulting type has all properties from both types.
*/

type Person = {
    name: string
}

type ExtendedPerson = Person & {
    age: number
}

let person: ExtendedPerson = {
    name: "Tom",
    age: 21,
}