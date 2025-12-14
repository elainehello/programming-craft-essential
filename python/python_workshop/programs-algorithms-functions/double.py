def double(number: int) -> int:
    result: int = number * 2
    return result

def main() -> None:
    print("Enter number:")
    user_input = int(input())
    rs = double(user_input)
    print(rs)

if __name__ == "__main__":
    main()
