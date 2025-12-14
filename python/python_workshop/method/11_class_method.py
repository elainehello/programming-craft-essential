class Australian:
    """the class itself is passed as the first argument"""
    is_human = True
    enjoys_sport = True

    @classmethod
    def is_sporty_human(cls) -> bool:
        return cls.is_human and cls.enjoys_sport

def main() -> None:
    aussie = Australian()
    print(aussie.is_sporty_human())
    print(f"[docstring]: {(aussie.__doc__ or "").replace("\n", "")}")

if __name__ == "__main__":
    main()
