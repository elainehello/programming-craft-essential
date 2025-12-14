class Temperature:
    def __init__(self, celsius: int) -> None:
        self.celsius = celsius

    @property
    def fahrenheit(self) -> float:
        return self.celsius * 9 / 5 + 32

def main() -> None:
    freezing = Temperature(100)
    print(freezing.fahrenheit)

if __name__ == "__main__":
    main()
