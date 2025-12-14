class Pet:
    def __init__(self, height: int) -> None:
        self.height = height

    is_human = False
    owner = 'Tom Misch'

    @staticmethod
    def pet_own_by_misch_family() -> bool:
        return 'Misch' in Pet.owner

def main() -> None:
    snoopy = Pet(42)
    print(snoopy.pet_own_by_misch_family())

if __name__== "__main__":
    main()
