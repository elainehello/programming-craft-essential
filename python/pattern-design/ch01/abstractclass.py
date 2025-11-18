"""
Program to Interfaces
This principle encorages to code against an interface rather than a concrete class,
making easy to swap or extend implementations without affect the rest of the system

An interface defines a *contract* for classes, specifying a set of methods that must
be implemented
"""

from abc import ABC, abstractmethod

class MyInterface(ABC):
    @abstractmethod
    def do_something(self, foo: str):
        pass

class MyClass(MyInterface):
    def do_something(self, foo: str) -> None:
        print(f"Hello doing something with:\t'{foo}'")

if __name__ == "__main__":
    MyClass().do_something("msg: holaaa")