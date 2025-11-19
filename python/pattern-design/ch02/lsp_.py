"""
LSP (Liskov Substitution Principle) - Proper Implementation Example

This demonstrates how subclasses should properly extend their parent class behavior.
All Bird subclasses can be substituted for the base Bird class without breaking
the program's functionality. Each subclass provides its own implementation of move()
while maintaining the expected contract: all birds can move in some way.
"""

class Bird:
    def move(self) -> None:
        print("I'm moving!\n")

class FlyingBird(Bird):
    def move(self) -> None:
        print("I'm flying!\n")

class FlightlessBird(Bird):
    def move(self) -> None:
        print("I'm walking!\n")

def make_bird_move(bird: Bird):
    bird.move()

if __name__ == "__main__":
    generic_bird = Bird()
    eagle = FlyingBird()
    penguin = FlightlessBird()

    make_bird_move(generic_bird)
    make_bird_move(eagle)
    make_bird_move(penguin)
