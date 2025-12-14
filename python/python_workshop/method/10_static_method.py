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

def main() -> None:
    my_diary = Diary(datetime.date(2022, 7, 30), datetime.date(2023, 7, 30))
    print(my_diary.show_birthday())
    print(my_diary.show_christmas())

if __name__ == "__main__":
    main()
