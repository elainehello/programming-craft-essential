"""
Prototype Design Pattern Implementation

This module demonstrates the Prototype pattern, which creates new objects by
cloning existing instances rather than creating them from scratch. This pattern
is particularly useful when:

1. Object creation is expensive (complex initialization, database calls, etc.)
2. You need to create many similar objects with slight variations
3. You want to avoid subclasses of an object creator in the client application
4. Classes to instantiate are specified at run-time

Key Components:
- Prototype Interface: Defines the cloning interface (copy/deepcopy)
- Concrete Prototype: Website class that can be cloned
- Prototype Registry: Stores and manages prototype instances
- Client: Uses the registry to clone objects with modifications

Example Usage:
    # Create a prototype
    original_site = Website("Python", "python.org", "Programming language")
    
    # Register it
    registry = Prototype()
    registry.register("python-template", original_site)
    
    # Clone with modifications
    new_site = registry.clone("python-template", name="PyPI", domain="pypi.org")

Benefits:
- Reduces object creation overhead
- Allows runtime configuration of object creation
- Eliminates need for complex initialization logic duplication
- Supports adding/removing objects at runtime
"""

import copy
from typing import Any, Dict


class Website:
    """
    Concrete Prototype class representing a website configuration.
    
    This class serves as a prototype that can be cloned to create new
    website instances with similar configurations but different properties.
    Uses Python's built-in copy module for cloning operations.
    """

    def __init__(self, name: str,
                domain: str,
                description: str,
                **kwargs: Any):
        """
        Initialize a website prototype.
        
        Args:
            name: The website name
            domain: The website domain (e.g., 'example.com')
            description: Brief description of the website
            **kwargs: Additional properties (category, keywords, etc.)
        """
        self.name: str = name
        self.domain: str = domain
        self.description: str = description
        # Dynamically add any additional properties
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self) -> str:
        """
        Return a formatted string representation of the website.
        
        Shows the website name with its unique ID, followed by all
        attributes in alphabetical order (excluding name to avoid duplication).
        """
        summary = [
            f"- {self.name} (ID: {id(self)})\n",
        ]
        # Get all instance attributes and sort them for consistent output
        infos = vars(self).items()
        ordered_infos = sorted(infos)
        for attr, val in ordered_infos:
            if attr == "name":  # Skip name as it's already in the header
                continue
            summary.append(f"{attr}: {val}\n")
        return "".join(summary)


class Prototype:
    """
    Prototype Registry - manages a collection of prototype objects.
    
    This class implements the Prototype pattern by maintaining a registry
    of prototype objects that can be cloned on demand. It uses deep copy
    to ensure complete independence between original and cloned objects.
    """

    def __init__(self) -> None:
        """Initialize an empty prototype registry."""
        self.registry: Dict[str, object] = {}

    def register(self, identifier: str, obj: object) -> None:
        """
        Register a prototype object in the registry.
        
        Args:
            identifier: Unique string key for the prototype
            obj: The prototype object to register
        """
        self.registry[identifier] = obj

    def clone(self, identifier: str, **attrs: Any) -> object:
        """
        Clone a registered prototype with optional attribute modifications.
        
        Args:
            identifier: The key of the prototype to clone
            **attrs: Attributes to override in the cloned object
            
        Returns:
            A deep copy of the prototype with applied modifications
            
        Raises:
            ValueError: If the identifier is not found in the registry
        """
        found = self.registry.get(identifier)
        if not found:
            raise ValueError(
                f"Incorrect object identifier: {identifier}"
            )
        # Create a deep copy to ensure complete independence
        obj = copy.deepcopy(found)
        # Apply any attribute overrides
        for key, value in attrs.items():
            setattr(obj, key, value)
        return obj


def main() -> None:
    """
    Demonstrate the Prototype pattern with website objects.
    
    Creates a prototype website, registers it, then clones it with
    modifications to create a related but different website.
    """
    # Common keywords for Python-related websites
    keywords = (
        "python",
        "programming",
        "scripting",
        "data",
        "automation",
    )

    # Create the original prototype
    site1 = Website(
        "Python",
        domain="python.org",
        description="Programming language and ecosystem",
        category="Open Source Software",
        keywords=keywords,
    )

    # Set up prototype registry and register our template
    proto = Prototype()
    proto.register("python-001", site1)

    # Clone the prototype with modifications to create a related website
    site2 = proto.clone(
        "python-001",
        name="Python Package Index",
        domain="pypi.org",
        description="Repository for published packages",
        category="Open Source Software",
    )

    # Display both websites to show the prototype pattern in action
    print("Original prototype:")
    print(site1)
    print("\nCloned and modified:")
    print(site2)


if __name__ == "__main__":
    main()
