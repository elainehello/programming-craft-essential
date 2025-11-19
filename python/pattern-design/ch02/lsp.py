"""
LSP dictates how subclasses should relate to their superclasses, if a program uses of
a superclass, then the substitution of these objects with the objects of a subclass
should not change the correctness and expected behaviour of the program
"""

from typing import Protocol

class Greeter(Protocol):
    def greet(self) -> str:
        ...

class EnglishGreeter:
    def greet(self) -> str:
        return "Hello!"

class SpanishGreeter:
    def greet(self) -> str:
        return "¡Hola!"

def welcome(g: Greeter) -> None:
    print(g.greet())

if __name__ == "__main__":
    welcome(EnglishGreeter())
    welcome(SpanishGreeter())
