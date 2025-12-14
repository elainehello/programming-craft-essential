import math

class Circle:
    """Example of a class with instance methods"""
    is_shape = True
    def __init__(self, radius: int, color: str='red') -> None:
        # Initialize circle with radius and color
        self.radius = radius
        self.color = color

    # self represents the instance (object) within the method
    def area(self) -> float:
        """Calculate the area of a circle: π(pi) × radius²"""
        return math.pi * self.radius ** 2

def main() -> None:
    circle = Circle(42)
    print(f"{(circle.area.__doc__ or "").replace("\n", "")}")
    print(circle.area())
    print(circle.__dict__)
    print(circle.is_shape)

if __name__ == "__main__":
    main()
