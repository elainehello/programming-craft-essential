import datetime

class Diary:
    def __init__(self, birthday: datetime.date,
                christmas: datetime.date) -> None:
        self.birthday = birthday
        self.christmas = christmas

    @staticmethod
    def format_date(date: datetime.date) -> str:
        return date.strftime('%d-%b-%y')

    def show_birthday(self) -> str:
        return self.format_date(self.birthday)

    def show_christmas(self) -> str:
        return self.format_date(self.christmas)

class CustomDiary(Diary):
    def __init__(self, birthday: datetime.date,
                christmas: datetime.date,
                date_format: str) -> None:
        self.date_format = date_format
        super().__init__(birthday, christmas)

    def format_date(self, date: datetime.date) -> str:
        return date.strftime(self.date_format)

def main() -> None:
    first_diary = CustomDiary(datetime.date(1996,7,30),
                            datetime.date(1997,6,29),
                            '%d-%b-%y')
    second_diary = CustomDiary(datetime.date(1996,7,30),
                            datetime.date(1997,6,29),
                            '%d/%b/%y')
    print(first_diary.show_birthday())
    print(second_diary.show_christmas())

if __name__ == "__main__":
    main()
