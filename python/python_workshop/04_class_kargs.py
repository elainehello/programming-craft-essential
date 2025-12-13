class Country:
    """A class representing a country with optional keyword arguments."""
    def __init__(self, name: str='Unspecified',
                population: None=None,
                size_kmsq=None):
        self.name = name
        self.population = population
        self.size_kmsq = size_kmsq

def main() -> None:
    usa = Country('United States of America', size_kmsq=25.2e1)
    print(f"[docstring]: {(usa.__doc__ or "").replace("\n", "")}")
    print(usa.__dict__)

if __name__ == "__main__":
    main()
