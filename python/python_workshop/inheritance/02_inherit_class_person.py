class Person:
    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name

class Baby(Person):
    def speak(self) -> None:
        print("Blah blah blah")

class Adult(Person):
    def speak(self) -> None:
        print(f"Hello, my name is {self.first_name}")

def main() -> None:
    jess = Baby("Jessie", "McCoy")
    tom = Adult("Tom", "Misch")
    jess.speak()
    tom.speak()

if __name__ == "__main__":
    main()
