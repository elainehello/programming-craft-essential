from typing import Type
import random

class Pet:
    """the class itself is passed as the first argument"""
    def __init__(self, height: int) -> None:
        self.height: int = height

    is_human = False
    owner = "Tom Misch"

    @classmethod
    def owned_by_misch_family(cls) -> bool:
        return "Misch" in cls.owner

    @classmethod
    def create_random_height_pet(cls: Type["Pet"]) -> "Pet":
        height = random.randrange(0, 100)
        return cls(height)

def main() -> None:
    for _ in range(5):
        pet = Pet.create_random_height_pet()
        print(f"[height]: {pet.height}")

if __name__ == "__main__":
    main()
