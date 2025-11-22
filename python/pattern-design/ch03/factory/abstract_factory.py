"""
Abstract Factory Pattern Implementation

This module demonstrates the Abstract Factory design pattern through a game simulation.
The pattern provides an interface for creating families of related objects without 
specifying their concrete classes.

In this example:
- Two different game worlds (FrogWorld and WizardWorld) serve as concrete factories
- Each factory creates consistent families of objects (characters and obstacles)
- The GameEnvironment uses these factories without knowing the specific implementations

Design Pattern Benefits:
- Ensures related objects are created together (consistency)
- Easy to add new game worlds without modifying existing code
- Encapsulates object creation logic within factories
"""

from typing import Protocol, Union
from typing import Union


class Obstacle(Protocol):
    """Protocol defining the interface for all obstacles."""
    def __str__(self) -> str: ...
    def action(self) -> str: ...

class Character(Protocol):
    """Protocol defining the interface for all characters."""
    def __str__(self) -> str: ...
    def interact_with(self, obstacle: Obstacle) -> None: ...

class Frog:
    """Character class representing a frog in the game."""

    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return self.name

    def interact_with(self, obstacle: Obstacle) -> None:
        """Define how the frog interacts with obstacles."""
        act = obstacle.action()
        msg = f"{self} the Frog encounters {obstacle} and {act}!"
        print(msg)

class Bug:
    """Obstacle class representing a bug that frogs encounter."""

    def __str__(self) -> str:
        return "a bug"

    def action(self) -> str:
        """Define what happens when a frog encounters this obstacle."""
        return "eats it"

class FrogWorld:
    """Concrete Factory for creating frog-themed game objects."""

    def __init__(self, name: str) -> None:
        print(self)
        self.plater_name = name  # Note: This appears to be a typo for 'player_name'

    def __str__(self) -> str:
        return "\n\n\t------ Frog World -------"

    def make_character(self) -> Frog:
        """Factory method to create a frog character."""
        return Frog(self.plater_name)

    def make_obstacle(self) -> Bug:
        """Factory method to create a bug obstacle."""
        return Bug()

class Wizard:
    """Character class representing a wizard in the game."""

    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return self.name

    def interact_with(self, obstacle: Obstacle) -> None:
        """Define how the wizard interacts with obstacles."""
        act = obstacle.action()
        msg = f"{self} the Wizard battles against {obstacle} and {act}!"
        print(msg)

class Ork:
    """Obstacle class representing an ork that wizards battle."""

    def __str__(self) -> str:
        return "an evil ork"

    def action(self) -> str:
        """Define what happens when a wizard encounters this obstacle."""
        return "kills it"

class WizardWorld:
    """Concrete Factory for creating wizard-themed game objects."""

    def __init__(self, name: str) -> None:
        print(self)
        self.player_name = name

    def __str__(self) -> str:
        return "\n\n\t------ Wizard World -------"

    def make_character(self) -> Wizard:
        """Factory method to create a wizard character."""
        return Wizard(self.player_name)

    def make_obstacle(self) -> Ork:
        """Factory method to create an ork obstacle."""
        return Ork()


class GameEnvironment:
    """
    Client class that uses the abstract factory to create game objects.
    This class doesn't need to know which specific factory is being used.
    """

    def __init__(self, factory: Union['FrogWorld', 'WizardWorld']) -> None:
        self.hero = factory.make_character()  # Create character using factory
        self.obstacle = factory.make_obstacle()  # Create obstacle using factory

    def play(self) -> None:
        """Start the game interaction between character and obstacle."""
        self.hero.interact_with(self.obstacle)

def validate_age(name: str) -> tuple[bool, int | None]:
    """
    Validate user input for age and return validation status with age value.
    
    Args:
        name: Player's name for personalized messages
        
    Returns:
        Tuple containing (is_valid, age_value)
    """
    age = None
    try:
        age_input = input(
            f"Welcome {name}. How old are you?\n"
        )
        age = int(age_input)  # int() casting - may raise ValueError
    except ValueError:
        print(
            f"Age {age} is invalid, please try again..."
        )
        return False, age
    return True, age

def main() -> None:
    """
    Main game loop that demonstrates the Abstract Factory pattern.
    
    The factory selection is based on user age:
    - Under 18: FrogWorld (simple, child-friendly theme)
    - 18 and over: WizardWorld (more complex, adult theme)
    """
    name = input("Hello. What's your name?\n")
    valid_input = False
    while not valid_input:
        valid_input, age = validate_age(name)

    # Abstract Factory Pattern in action: 
    # Factory selection based on age determines the entire game theme
    game = FrogWorld if age < 18 else WizardWorld

    # Create game environment using the selected factory
    environment = GameEnvironment(game(name))

    # Start the game
    environment.play()

if __name__ == "__main__":
    main()
