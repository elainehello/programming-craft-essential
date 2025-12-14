class Pet:
    """Docs string documentation for Pet class"""
    is_human = False
    owner = "John"

def main():
    chubby = Pet()
    print(f"[instance creation]: {chubby}")
    print(f"[is_human attribute]: {chubby.is_human}")
    print(f"[owner attribute]: {chubby.owner}")
    print(f"[docstring]:{(chubby.__doc__ or "").replace("\n", " ")}")

if __name__ == "__main__":
    main()
