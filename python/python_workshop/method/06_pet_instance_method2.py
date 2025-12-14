class Pet:
    """A pet class with height-based methods"""
    def __init__(self, height: int) -> None:
        self.height = height

    is_human = False
    owner = 'Tom Misch'

    # Instance method with custom threshold parameter
    def is_tall(self, tall_if_at_least: int) -> bool:
        """Check if pet is tall based on given threshold"""
        return self.height >= tall_if_at_least

def main() -> None:
    sausage = Pet(25)
    # print(sausage.__dict__, sausage.is_human, sausage.owner)
    # Test with threshold of 30
    print(f"[Is it tall?]: {sausage.is_tall(30)}")
    # Update height and test with threshold of 40
    sausage.height = 60
    print(f"[Is it tall?]: {sausage.is_tall(40)}")

if __name__ == "__main__":
    main()
