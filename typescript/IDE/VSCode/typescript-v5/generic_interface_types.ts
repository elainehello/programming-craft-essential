/*
Generic interfaces allow you to create reusable type-safe data structures
that work with different types while maintaining type safety.
*/

interface Box<T> {
    content: T;
}

const numberBox: Box<number> = {
    content: 10
};