class Person:
    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name

    def speak(self) -> None:
        print(f"Hello, my name is {self.first_name}")

class TalkativePerson(Person):
    """Extends Person class, using super() to call parent methods"""
    def speak(self) -> None:
        super().speak()
        print("It's a pleasure to meet you")

def main() -> None:
    tom = TalkativePerson("Tom", "Misch")
    print(f"[docstring cls TalkativePerson]: {(tom.__doc__ or " ").replace("\n", " ")}")
    tom.speak()

if __name__ == "__main__":
    main()
