from typing import Type

class Country:
    """the class itself is passed as the first argument"""
    is_human = True
    def __init__(self, name: str,
                size_kmsq: float,
                population: str | None = None):
        self.name = name
        self.size_kmsq = size_kmsq
        self.population = population

    # notice the use of 'cls' as first argument
    @classmethod
    def create_with_msq(cls: Type["Country"],
                        name: str, population: str,
                        size_msq: float) -> "Country":
        size_kmsq = size_msq / 0.621371 ** 2
        return cls(name, size_kmsq, population)

def main() -> None:
    mexico = Country.create_with_msq('Mexico', '150e2', 760000)
    print(f"Mexico size: {mexico.size_kmsq} km²")
    print(f"Country name: {mexico.name}")
    print(f"Population: {mexico.population}")

if __name__ == "__main__":
    main()
