"""
Builder Design Pattern Implementation

This module demonstrates the Builder pattern through a pizza ordering system.
The Builder pattern separates the construction of complex objects from their 
representation, allowing the same construction process to create different 
representations.

Key Components:
- Product: Pizza (the complex object being built)
- Builder Protocol: PizzaBuilder (defines the interface)
- Concrete Builders: MargaritaBuilder, CreamyBaconBuilder
- Director: Waiter (orchestrates the building process)
"""

import time
from enum import Enum
from typing import Protocol, Callable, Optional, Mapping

# Define pizza states throughout the cooking process
PizzaProgress = Enum(
    "PizzaProgress",
    "queued preparation baking ready"
)

# Available dough types
PizzaDough = Enum(
    "PizzaDough",
    "thin thick"
)

# Available sauce options
PizzaSauce = Enum(
    "PizzaSauce",
    "tomato creme_fraiche"
)

# Available toppings for pizzas
PizzaTopping = Enum(
    "PizzaTopping",
    "mozzarella double_mozzarella bacon ham mushrooms red_onion oregano"
)

# Simulation delay for each cooking step (in seconds)
STEP_DELAY = 3


class Pizza:
    """
    The Product class - represents the complex object being constructed.
    Contains the pizza's components that will be built step by step.
    """
    
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.sauce: Optional[PizzaSauce] = None
        self.dough: Optional[PizzaDough] = None
        self.topping: list[PizzaTopping] = []

    def __str__(self) -> str:
        return self.name

    def prepare_dough(self, dough: PizzaDough) -> None:
        """Prepare the pizza dough with simulation delay."""
        self.dough = dough
        print(f"preparing the {self.dough.name} dough of your {self}...")
        time.sleep(STEP_DELAY)
        print(f"done with the {self.dough.name} dough")


class PizzaBuilder(Protocol):
    """
    Builder Protocol - defines the interface for concrete builders.
    Using Protocol for duck typing instead of ABC for flexibility.
    All concrete builders must implement these methods.
    """
    
    pizza: Pizza
    
    def prepare_dough(self) -> None: 
        """Prepare the dough for the pizza."""
        ...
    
    def add_sauce(self) -> None: 
        """Add sauce to the pizza."""
        ...
    
    def add_topping(self) -> None: 
        """Add toppings to the pizza."""
        ...
    
    def bake(self) -> None: 
        """Bake the completed pizza."""
        ...


class MargaritaBuilder:
    """
    Concrete Builder for Margarita pizza.
    Implements the PizzaBuilder protocol to create a classic Margarita pizza
    with thin dough, tomato sauce, mozzarella, and oregano.
    """
    
    def __init__(self) -> None:
        self.pizza = Pizza("margarita")
        self.progress = PizzaProgress.queued
        self.baking_time = 5  # Shorter baking time for thin crust

    def prepare_dough(self) -> None:
        """Prepare thin dough for classic Margarita style."""
        self.progress = PizzaProgress.preparation
        self.pizza.prepare_dough(PizzaDough.thin)

    def add_sauce(self) -> None:
        """Add traditional tomato sauce."""
        print(f"adding tomato sauce to your {self.pizza}...")
        self.pizza.sauce = PizzaSauce.tomato
        time.sleep(STEP_DELAY)
        print("done with the tomato sauce")

    def add_topping(self) -> None:
        """Add classic Margarita toppings: mozzarella and oregano."""
        print(f"adding mozzarella and oregano to your {self.pizza}...")
        self.pizza.topping.extend([
            PizzaTopping.mozzarella,
            PizzaTopping.oregano
        ])
        time.sleep(STEP_DELAY)
        print("done with the topping")

    def bake(self) -> None:
        """Bake the Margarita pizza."""
        self.progress = PizzaProgress.baking
        print(f"baking your {self.pizza} for {self.baking_time} seconds...")
        time.sleep(self.baking_time)
        self.progress = PizzaProgress.ready
        print(f"your {self.pizza} is ready")


class CreamyBaconBuilder:
    """
    Concrete Builder for Creamy Bacon pizza.
    Implements the PizzaBuilder protocol to create a rich, meat-loaded pizza
    with thick dough, crème fraîche sauce, and multiple toppings.
    """
    
    def __init__(self) -> None:
        self.pizza = Pizza("creamy bacon")
        self.progress = PizzaProgress.queued
        self.baking_time = 7  # Longer baking time for thick crust and more toppings

    def prepare_dough(self) -> None:
        """Prepare thick dough for hearty Creamy Bacon style."""
        self.progress = PizzaProgress.preparation
        self.pizza.prepare_dough(PizzaDough.thick)

    def add_sauce(self) -> None:
        """Add rich crème fraîche sauce."""
        print(f"adding crème fraîche sauce to your {self.pizza}...")
        self.pizza.sauce = PizzaSauce.creme_fraiche
        time.sleep(STEP_DELAY)
        print("done with the crème fraîche sauce")

    def add_topping(self) -> None:
        """Add premium toppings: double mozzarella, bacon, ham, mushrooms, red onion, oregano."""
        print(f"adding double mozzarella, bacon, ham, mushrooms, red onion, oregano to your {self.pizza}...")
        self.pizza.topping.extend([
            PizzaTopping.double_mozzarella,
            PizzaTopping.bacon,
            PizzaTopping.ham,  # Added to match the print statement
            PizzaTopping.mushrooms,
            PizzaTopping.red_onion,
            PizzaTopping.oregano
        ])
        time.sleep(STEP_DELAY)
        print("done with the topping")

    def bake(self) -> None:
        """Bake the Creamy Bacon pizza (longer time for thick crust)."""
        self.progress = PizzaProgress.baking
        print(f"baking your {self.pizza} for {self.baking_time} seconds...")
        time.sleep(self.baking_time)
        self.progress = PizzaProgress.ready
        print(f"your {self.pizza} is ready")


class Waiter:
    """
    Director class - orchestrates the pizza building process.
    The Waiter knows the steps to build a pizza but delegates the actual
    construction to the specific builder. This separates the construction
    algorithm from the product representation.
    """
    
    def __init__(self) -> None:
        self.builder: Optional[PizzaBuilder] = None

    def construct_pizza(self, builder: PizzaBuilder) -> None:
        """
        Execute the pizza construction process in the correct order.
        This method defines the algorithm for building any pizza type.
        """
        self.builder = builder
        # Define the construction steps in order
        steps: tuple[Callable[[], None], ...] = (
            builder.prepare_dough,
            builder.add_sauce,
            builder.add_topping,
            builder.bake,
        )
        # Execute each step sequentially
        for step in steps:
            step()

    @property
    def pizza(self) -> Pizza:
        """Get the completed pizza from the builder."""
        assert self.builder is not None, "No builder assigned"
        return self.builder.pizza   


def validate_style(builders: Mapping[str, Callable[[], PizzaBuilder]]) -> tuple[bool, Optional[PizzaBuilder]]:
    """
    Validate user input and return appropriate builder.
    
    Args:
        builders: Dictionary mapping user input keys to builder classes
        
    Returns:
        Tuple of (is_valid, builder_instance or None)
    """
    try:
        input_msg = "What pizza would you like, [m]argarita or [c]reamy bacon? "
        pizza_style = input(input_msg)
        # Create builder instance from user choice
        pizza_builder = builders[pizza_style]()
    except KeyError:
        # Handle invalid user input
        error_msg = "Sorry, only margarita (key m) and creamy bacon (key c) are available"
        print(error_msg)
        return (False, None)
    return (True, pizza_builder)


def main():
    """
    Main application entry point.
    Demonstrates the Builder pattern by allowing users to order pizzas.
    """
    # Registry of available pizza builders
    builders = dict(m=MargaritaBuilder, c=CreamyBaconBuilder)
    
    # Get valid user input
    valid_input = False
    builder: Optional[PizzaBuilder] = None
    while not valid_input:
        valid_input, builder = validate_style(builders)
    
    assert builder is not None, "Builder should not be None after validation"
    
    # Build and serve the pizza
    print()
    waiter = Waiter()
    waiter.construct_pizza(builder)
    pizza = waiter.pizza
    print()
    print(f"Enjoy your {pizza}!")


if __name__ == "__main__":
    main()
