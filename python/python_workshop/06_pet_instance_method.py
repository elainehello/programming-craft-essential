class Pet:
    """A pet class with height-based methods"""
    def __init__(self, height: int) -> None:
        self.height = height

    is_human = False
    owner = 'Tom Misch'

    def is_tall(self) -> bool:
        """Check if pet is tall (height >= 50)"""
        return self.height >= 50

def main() -> None:
    sausage = Pet(25)
    # print(sausage.__dict__, sausage.is_human, sausage.owner)
    print(f"[Is it tall?]: {sausage.is_tall()}")
    # Update height and check again
    sausage.height = 60
    print(f"[Is it tall?]: {sausage.is_tall()}")

if __name__ == "__main__":
    main()
