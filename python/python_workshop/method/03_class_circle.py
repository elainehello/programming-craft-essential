class Circle:
    """A class representing a circle with radius and color attributes/properties."""
    is_shape = True

    def __init__(self, radius: int, color: str) -> None:
        self.radius = radius
        self.color = color

def main() -> None:
    first_circle = Circle(3, 'red')
    second_circle = Circle(6, 'blue')

    print(f"\n**[docstring]: {(first_circle.__doc__ or "").replace("\n", "")}**\n")
    print(f"[first instance]: {first_circle}")
    print(f"[radius attribute]: {first_circle.radius}")
    print(f"[color attribute]: {first_circle.color}")
    print(f"[shape attribute]: {first_circle.is_shape}\n")

    print(f"[second instance]: {second_circle}")
    print(f"[radius attribute]: {second_circle.radius}")
    print(f"[color attribute]: {second_circle.color}")
    print(f"[shape attribute]: {second_circle.is_shape}")

if __name__ == "__main__":
    main()