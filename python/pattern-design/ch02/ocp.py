"""
OCP (Open-Closed Principle) states that software entities should be open for extension
but closed for modification. You can add new functionality by creating new classes
that implement the same interface, without changing existing code.
"""

import math
from typing import Protocol

class Shape(Protocol):
    def area(self) -> float:
        ...

class Rectangle:
    def __init__(self, width: float, height: float):
        self.width : float = width
        self.height : float = height

    def area(self) -> float:
        return self.width * self.height

class Circle:
    def __init__(self, radius: float):
        self.radius : float = radius

    def area(self) -> float:
        return math.pi * (self.radius**2)

def calculate_area(shape: Shape) -> float:
    return shape.area()

if __name__ == "__main__":
    rectangle = Rectangle(10, 25)
    rect_area = calculate_area(rectangle)
    print(f"Rectangle area: {rect_area}")

    circle = Circle(4.2)
    circle_area = calculate_area(circle)
    print(f"Circle area: {circle_area:.2f}")
