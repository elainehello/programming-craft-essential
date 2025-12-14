class Pet:
    def __init__(self, height: int, name: str) -> None:
        self.height = height
        self.name = name

    is_human = False
    owner = 'Tom Misch'

    def __str__(self) -> str:
        return f"[height]: {self.height} [name]: {self.name}"

def main() -> None:
    my_pet = Pet(40, 'mike')
    print(my_pet)

if __name__ == "__main__":
    main()
