def get_user_input() -> None:
    user_name = str(input("Hello what's is your name? "))
    print(f"Hello, welcome {user_name}!")
    x = 100
    y = 'abcd'
    print(f"x * 2 = {x*2}, and y.capitalize() is {y.capitalize()}")

def main() -> None:
    get_user_input()

if __name__ == "__main__":
    main()
