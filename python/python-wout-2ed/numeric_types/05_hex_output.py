def hex_output() -> None:
    decnum = 0
    hexnum = input('Enter a hex number to convert: ')
    for power, digit in enumerate(reversed(hexnum)):
        decnum += int(digit, 16) * (16 ** power)
    print(decnum)

def main() -> None:
    hex_output()

if __name__ == "__main__":
    main()
