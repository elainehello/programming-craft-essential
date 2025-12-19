/*
Decorators are functions that modify or extend the behavior of classes, methods, or properties.
They use the @ syntax and provide a way to add metadata or functionality without changing the original code.
*/

function log(originalMethod: any,
    context: ClassMethodDecoratorContext) {
        function replacementMethod(this: any, ...args: any[]) {
            console.log(`Calling ${String(context.name)}`)
            return originalMethod.call(this, ...args)
        }
        return replacementMethod
    }
class Calculator {
    @log
    add(x: number, y: number): number {
        return x + y
    }
}
new Calculator().add(4, 2)

// the @log decorator is applied to the add method within the Calculator class