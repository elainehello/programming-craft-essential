class MyInt(int):
    """Custom integer class that extends built-in int with additional methods"""
    def is_divisible_by(self, x: int) -> int:
        return self % x == 0

def main() -> None:
    a = MyInt(8)
    print(f"[is divisible]: {a.is_divisible_by(2)}")

if __name__ == "__main__":
    main()
