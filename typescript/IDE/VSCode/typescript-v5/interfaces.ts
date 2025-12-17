/*
Interfaces define contracts that specify what properties/attributes and methods a class or object must have.
They provide type checking and enable polymorphism without implementing any functionality.
*/

export interface Comparable<T> {
    compareTo(other: Comparable<T>): -1 | 0 | 1;
}

/*
This interface defines that any object implementing Comparable must have a compareTo method. This
method takes another object of the same type (T) and returns a number indicating the comparison
result (-1 for less than, 0 for equal, 1 for greater than).
Interfaces enforce a consistent structure across objects that implement them.
*/