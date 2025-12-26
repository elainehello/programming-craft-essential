from typing import Tuple

# ellipsis, variadic number of arguments/types
# tuples are indexed starting from [0] ...[9]...
# once created becomes ummutable, allows duplicates
quotes: Tuple[str, ...] = ("A man is not complete until he is married. Then he is finished.",
                           "As I said before, I never repeat myself",
                           "Behind a successful man is an exhausted woman.",
                           "Black holes really suck...",
                           "Facts are stubborn things.",
                           )

class QuoteModel:
    def get_quote(self, n: int) -> str:
        try:
            value = quotes[n]
        except IndexError as err:
            value = f"Not found! [Error]: {err}"
        return value

class QuoteTerminalView:
    def show(self, quote: str) -> None:
        print(f'And the quote is: {quote}')

    def error(self, msg: str) -> None:
        print(f'{msg}')

    def select_quote(self) -> str:
        return input("Which quote number would you like to see? ")

class QuoteTerminalController:
    def __init__(self) -> None:
        self.model = QuoteModel()
        self.view = QuoteTerminalView()

    def run(self) -> None:
        valid_input = False
        while not valid_input:
            try:
                n = self.view.select_quote()
                n = int(n)
                valid_input = True
            except ValueError as err:
                self.view.error(f"Incorrect index '{n}'. Error: {err}")
        quote = self.model.get_quote(n)
        self.view.show(quote)

def main():
    controller = QuoteTerminalController()
    while True:
        controller.run()

if __name__ == "__main__":
    main()
