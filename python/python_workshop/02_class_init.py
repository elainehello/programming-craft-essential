class Pet:
    """A class to capture useful information abt my pets,
    in case I lose track"""

    def __init__(self, height: int) -> None:
        self.height = height

    is_human = False
    owner = "John"

def main() -> None:
    chubby = Pet(height=7)
    print(f"[instance creation]: {chubby}")
    print(f"[docstring]: {(chubby.__doc__ or "").replace("\n", "")}")
    print(f"[is_human attribute]: {chubby.is_human}")
    print(f"[owner]: {chubby.owner}")

if __name__ == "__main__":
    main()
