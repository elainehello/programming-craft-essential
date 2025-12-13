class Country:
    def __init__(self, name: str,
                size_kmsq: float,
                population: str | None = None):
        self.name = name
        self.population = population
        self.size_kmsq = size_kmsq

    def size_miles_sq(self, conversio_rate: float=0.621371) -> float:
        # miles_sq = size_kmsq * 0.621371^2
        return self.size_kmsq * conversio_rate ** 2

def main() -> None:
    algeria = Country("Algeria", size_kmsq=2.382e6)
    print(algeria.size_miles_sq())

if __name__ == "__main__":
    main()
