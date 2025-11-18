"""
Protocol offers a more flexible approach than ABCs, aka structural duck typing,
where an onject is consider valid if it has certain attributes or methods, regardless
of its actual inheritance.

Allows type checking at compile time, it makes programs more robust and easier to debug.
"""

from typing import Protocol

class CanFly(Protocol):
    def fly(self) -> str:
        ... # "This method must exist and return a string."

class Duck:
    def fly(self) -> str:
        return ("Duck flies.")
    def swim(self) -> str:
        return ("Duck swim.")

def make_it_fly(flyer: CanFly) -> None:
    print(flyer.fly())

if __name__ == "__main__":
    my_duck = Duck()
    make_it_fly(my_duck)
