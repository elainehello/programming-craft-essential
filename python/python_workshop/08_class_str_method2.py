class Country:
    def __init__(self, name: str,
                population: None | str,
                size_kmsq: None | float):
        self.name = name
        self.population = population
        self.size_kmsq = size_kmsq

    def __str__(self) -> str:
        label = self.name

        if self.population:
            label = f"[name]: {label}, [population]: {self.population}"
        if self.size_kmsq:
            label = f"[name]: {label}, [size_kmsq]: {self.size_kmsq}"
        return label

def main() -> None:
    #chad = Country(name="Chad", population=None, size_kmsq=None)
    #chad = Country(name="Chad", population="USA", size_kmsq=None)
    chad = Country(name="Chad", population=None, size_kmsq=5.25e7)
    print(chad)

if __name__ == "__main__":
    main()
