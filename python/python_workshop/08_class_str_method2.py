class Country:
    def __init__(self, name: str,
                population: None | str,
                size_kmsq: None | float):
        self.name = name
        self.population = population
        self.kmsq = size_kmsq

    def __str__(self) -> str:
        return self.name

def main() -> None:
    chad = Country(name="Chad", population=None, size_kmsq=None)
    print(chad)

if __name__ == "__main__":
    main()
