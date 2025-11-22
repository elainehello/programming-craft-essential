from typing import Any, Protocol, Iterator

class DataStructure(Protocol):
    def is_empty(self) -> bool:
        ...

    def size(self) -> int:
        ...

    def clear(self) -> None:
        ...

class ListOperation(Protocol):
    def append(self, data: Any) -> None:
        ...

    def prepend(self, data: Any) -> None:
        ...

    def remove(self, data: Any) -> bool:
        ...

    def find(self, data: Any) -> int:
        ...

class Stackable(Protocol):
    def push(self, data: Any) -> None:
        ...

    def pop(self) -> Any:
        ...

    def peek(self) -> Any:
        ...

class Searchable(Protocol):
    def find(self, data: Any) -> int:
        ...

    def contains(self, data: Any) -> bool:
        ...

class Indexable(Protocol):
    def get_at(self, index: int) -> Any:
        ...

    def set_at(self, index: int, data: Any) -> None:
        ...

    def insert_at(self, index: int, data: Any) -> None:
        ...

    def remove_at(self, index: int) -> Any:
        ...

class Iterable(Protocol):
    def __iter__(self) -> Iterator[Any]:
        ...
