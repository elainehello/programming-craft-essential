import datetime

class Diary:
    def __init__(self,
        birthday: datetime.date,
        christmas: datetime.date) -> None:
        self.birthday = birthday
        self.christmas = christmas

    def format_date(self, date: datetime.date) -> str:
        """Default formatting method"""
        return date.strftime("%d-%b-%y")

    def show_birthday(self) -> str:
        return self.format_date(self.birthday)

    def show_christmas(self) -> str:
        return self.format_date(self.christmas)

class CustomDiary(Diary):
    """Demonstrates method overriding"""
    def __init__(self,
        birthday: datetime.date,
        christmas: datetime.date,
        date_format: str = "%d/%m/%y") -> None:
        super().__init__(birthday, christmas)
        self.date_format = date_format

    def format_date(self, date: datetime.date) -> str:
        """Override parent's format_date method with custom formatting"""
        return date.strftime(self.date_format)

def main() -> None:
    # Regular diary with default formatting
    regular_diary = Diary(
        datetime.date(1996, 7, 30),
        datetime.date(1997, 12, 25)
    )

    # Custom diary that overrides the format_date method
    custom_diary = CustomDiary(
        datetime.date(1996, 7, 30),
        datetime.date(1997, 12, 25),
        "%d/%m/%y"
    )

    print("Regular Diary:")
    print(f"Birthday: {regular_diary.show_birthday()}")
    print(f"Christmas: {regular_diary.show_christmas()}")

    print("\nCustom Diary (overridden method):")
    print(f"Birthday: {custom_diary.show_birthday()}")
    print(f"Christmas: {custom_diary.show_christmas()}")

if __name__ == "__main__":
    main()
