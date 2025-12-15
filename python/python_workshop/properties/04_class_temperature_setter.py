class Temperature:
    def __init__(self, celcius: int) -> None:
        self.celsius = celcius

    @property
    def fahrenheit(self) -> float:
        return self.celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value: int) -> None:
        if value < -460:
            raise ValueError("Temperatures less than -460F are not possible")
        self.celcius = (value - 32) * 5 / 9

def main() -> None:
    temp = Temperature(5)
    print(temp.fahrenheit)
    temp.fahrenheit = 32
    print(temp.celcius)

if __name__ == "__main__":
    main()
