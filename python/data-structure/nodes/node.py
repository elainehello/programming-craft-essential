from typing import Any, Optional, Generic, TypeVar

T = TypeVar('T')

class Node(Generic[T]):
    def __init__(self, data: T) -> None:
        self.data: T = data
        self.next: Optional['Node[T]'] = None

    def __str__(self) -> str:
        return str(self.data) # type casting(?)

    def __repr__(self) -> str:
        return f"Node({self.data})"

class DoublyNode(Generic[T]):
    def __init__(self, data: T) -> None:
        self.data: T = data
        self.next: Optional['DoublyNode[T]'] = None
        self.prev: Optional['DoublyNode[T]'] = None

    def __str__(self) -> str:
        return str(self.data)

    def __repr__(self) -> str:
        return f"DoublyNode({self.data})"
