class Person:
    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

def main() -> None:
    customer = Person("Liu", "Jo")
    print(f"[Full name]: {customer.full_name}")

if __name__ == "__main__":
    main()
