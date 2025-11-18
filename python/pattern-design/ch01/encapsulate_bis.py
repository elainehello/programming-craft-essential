# Encapsulating using a property

class Circle:
    def __init__(self, radius: int):
        self._radius: int = radius

    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value: int) -> None:
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

if __name__ == "__main__":
    circle = Circle(10)
    print(f"Initial radius value: {circle.radius}")

    circle.radius = 30
    print(f"New radius assigment: {circle.radius}")
