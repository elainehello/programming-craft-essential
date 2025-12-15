class Temperature:
    def __init__(self, celsius: int) -> None:
        self.celsius = celsius

    @property
    def fahrenheit(self) -> float:
        return self.celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value: int) -> None:
        if value < -460:
            raise ValueError("Temperatures less than -460F are not possible")
        self.celsius = (value - 32) * 5 / 9

def main() -> None:
    temp = Temperature(5)
    print(temp.fahrenheit)
    temp.fahrenheit = 32
    print(temp.celsius)

if __name__ == "__main__":
    main()
