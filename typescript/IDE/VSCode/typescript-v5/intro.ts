/*
Type safety ensures that variables and data structures have well-defined types
that specify what kind of values they can contain. Think of it like labeling
containers to clearly describe their contents and prevent misuse.
*/

const one: string = "one"
const two: boolean = false
const three: number = 3
const four: null = null
const five: unknown = 5
const six: any = 6
const seven = Symbol("seven")

function neverReturningFunction(): never {
    throw new Error("This function never returns")
}