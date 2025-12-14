import datetime

class Diary:
    def __init__(self, birthday: datetime.date,
                christmas: datetime.date) -> None:
        self.birthday = birthday
        self.christmas = christmas

    def show_birthday(self) -> str:
        return self.birthday.strftime('%d-%b-%y')

    def show_christmas(self) -> str:
        return self.christmas.strftime('%d-%b-%y')

def main() -> None:
    my_diary = Diary(datetime.date(2022, 7, 30), datetime.date(2023, 7, 30))
    print(my_diary.show_birthday())

if __name__ == "__main__":
    main()
