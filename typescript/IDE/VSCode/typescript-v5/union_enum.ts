/*
Const enums are inlined at compile time, improving performance by replacing
enum references with their literal values directly in the generated code.
*/

const prefix = '/data';
const enum Routes {
    Parts = `${prefix}/parts`, // translates to "/data/parts"
    Invoices = `${prefix}/invoices`, // translates to "/data/invoices"
}
