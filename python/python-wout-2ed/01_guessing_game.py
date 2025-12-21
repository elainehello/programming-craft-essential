import random

def guessing_game() -> None:
    answer = random.randint(0, 100)

    while True:
        user_guess = int(input('What is your guess? '))
        if user_guess == answer:
            print(f'Right! The asnwer is {user_guess}')
        if user_guess < answer:
            print(f'Your guess of {user_guess} is too low!')
        else:
            print(f'Your guess of {user_guess} is too high!')

def main() -> None:
    guessing_game()

if __name__ == "__main__":
    main()
