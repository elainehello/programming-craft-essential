def mysum(*numbers: int) -> int:
    """
    *numbers: accepts variadic number of integer arguments
    """
    output = 0
    for number in numbers:
        output += number
    return output

def main() -> None:
    print(mysum(10, 20, 30, 40))

if __name__ == "__main__":
    main()
