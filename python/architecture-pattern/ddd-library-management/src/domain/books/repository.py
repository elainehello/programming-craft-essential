from abc import abstractmethod
from typing import List, Optional
from .models import Book

class BookRepository:
    @abstractmethod
    def get_by_id(self, book_id: str) -> Optional[Book]:
        ...

    @abstractmethod
    def list_all(self, skip: int = 0, limit: int = 100) -> List[Book]:
        ...

    @abstractmethod
    def save(self, book: Book) -> None:
        ...

    @abstractmethod
    def delete(self, book_id: str) -> None:
        ...