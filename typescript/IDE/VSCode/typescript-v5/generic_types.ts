/*
Generic types allow functions to work with any type while preserving type information.
The type parameter <T> acts as a placeholder that gets replaced with the actual type.
*/

function callMe<T>(parameter: T) : T {
    return parameter
}