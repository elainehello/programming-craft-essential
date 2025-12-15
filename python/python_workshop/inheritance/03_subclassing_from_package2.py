import datetime

class MyDate(datetime.date):
    """Custom date class that extends datetime.date with additional functionality"""
    def add_days(self, nbr_days: int) -> "MyDate":
        return self + datetime.timedelta(nbr_days)

def main() -> None:
    d = MyDate(2022, 7, 30)
    print(d.add_days(40))
    print(d.add_days(85))

if __name__ == "__main__":
    main()
