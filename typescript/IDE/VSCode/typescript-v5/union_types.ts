/*
Union types allow a variable to hold values of multiple types using the | operator.
*/

type A = 'A';
type B = 'B';
type C = A | B;

// (!!!) AVOID USING UNION TYPES WITH INCOMPATIBLE TYPES, IT COULD LEAD TO CONFUSION AND INCREASED COMPLEXITY