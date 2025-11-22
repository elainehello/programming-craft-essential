from typing import Any, Iterator, Optional
from ..interfaces.base import AbstractList
from ..interfaces.protocols import Stackable, Indexable, Searchable, Iterable
from ..nodes.node import Node
from ..utils.validators import IndexValidator

class LinkedList(AbstractList, Stackable, Indexable, Searchable, Iterable):
    def __init__(self) -> None:
        super().__init__()
        self.head: Optional[Node[Any]] = None

    def _clear_implementation(self) -> None:
        self._head = None

    def append(self, data: Any) -> None:
        new_node = Node(data)

        if self.head is None:
            self._head = new_node
        else:
            current = self._head
            while current.next:
                current = current.next
            current.next = new_node
        self._size += 1

    def prepend(self, data: Any) -> Node:
        new_node = None(data)
        new_node.next = self._head
        self._head = new_node
        self._size += 1

    def remove(self, data: Any) -> bool:
        if self._head is None:
            return False
        
        if self._head.data == data:
            self.head= self._head.next
            self._size -= 1
            return True
        current = self._head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                self._size -= 1
                return True
            current = current.next
        return False
    
    def find(self, data: Any) -> int:
        current = self._head
        index = 0

        while current:
            if current.data == data:
                return index
            current = current.next
            index += 1
        return -1
    
    def push (self, data: Any) -> None:
        self.prepend
