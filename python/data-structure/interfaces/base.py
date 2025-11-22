from abc import ABC, abstractmethod
from typing import Any, Optional
from .protocols import DataStructure, ListOperation

class AbstractList(ABC, DataStructure, ListOperation):
    def __init__(self) -> None:
        self._size: int = 0

    def is_empty(self) -> bool:
        return self._size == 0

    def size(self) -> int:
        return self._size

    def clear(self) -> None:
        self._clear_implementation()
        self._size = 0

    @abstractmethod
    def _clear_implementation(self) -> None:
        pass

    @abstractmethod
    def append(self, data: Any) -> None:
        pass

    @abstractmethod
    def prepend(self, data: Any) -> None:
        pass

    @abstractmethod
    def remove(self, data: Any) -> bool:
        pass

    @abstractmethod
    def find(self, data: Any) -> int:
        pass

    def __len__(self) -> int:
        return self.size()
