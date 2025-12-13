import math

class Circle:
    """example of an instance method"""
    is_shape = True
    def __init__(self, radius: int, color: str='red') -> None:
        self.radius = radius
        self.color = color

    def area(self) -> float:
        """Calculate the area of a circle: π(pi) × radius²"""
        return math.pi * self.radius ** 2

def main() -> None:
    circle = Circle(42)
    print(f"{(circle.area.__doc__ or "").replace("\n", "")}")
    print(circle.area())

if __name__ == "__main__":
    main()
