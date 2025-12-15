class BetterPerson:
    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    @full_name.setter
    def full_name(self, name: str) -> None:
        names = name.split(' ')
        self.first_name = names[0]
        if len(names) > 2:
            self.last_name = ' '.join(names[1:])
        elif len(names) == 2:
            self.last_name = names[1]

def main() -> None:
    my_person = BetterPerson("Mary", "Lou")
    my_person.full_name = "Mary Lou Misch"
    print(my_person.first_name)
    print(my_person.last_name)

if __name__ == "__main__":
    main()
