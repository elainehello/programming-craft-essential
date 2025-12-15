class Person:
    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    @full_name.setter
    def full_name(self, name: str) -> None:
        first, last = name.split(" ")
        self.first_name = first
        self.last_name = last

def main() -> None:
    customer = Person("Liu", "Jo")
    print(f"[full name]: {customer}")
    customer.full_name = "Tom Misch"
    print(f"[first name]: {customer.first_name}")
    print(f"[last name]: {customer.last_name}")

if __name__ == "__main__":
    main()
