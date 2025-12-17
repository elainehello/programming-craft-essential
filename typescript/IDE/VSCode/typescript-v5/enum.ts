/*
Enums define sets of named constants that improve code readability
and provide compile-time type safety.
*/

enum Direction {
    Up = 0,
    Down, // Implicitly assigned value 1
    Left, // Implicitly assigned value 2
    Right, // Implicitly assigned value 3
}
let userDirection: Direction = Direction.Up
