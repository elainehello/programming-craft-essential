class Pet:
    def __init__(self, name: str, weight: int) -> None:
        self.name = name
        self.weight = weight

class Cat(Pet):
    is_feline = True

class Dog(Pet):
    is_feline = False

def main() -> None:
    my_cat = Cat("Snowflake", 9)
    print(f"{my_cat.name}")

if __name__ == "__main__":
    main()
