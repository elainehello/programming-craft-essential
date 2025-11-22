from typing import Optional, Any, Protocol, Iterator
from abc import abstractmethod

class nodeCreation:
    def __init__(self, data: Any) -> None:
        self.data = data
        self.next = None

    def __str__(self) -> str:
        return str(self.data) # type casting



