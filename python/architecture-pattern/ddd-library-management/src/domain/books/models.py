from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Optional

class BookStatus(str, Enum):
    PRESENT = "Present"
    MISSING = "Missing"
    BORROWED = "Borrowed"

@dataclass(frozen=True)
class BookLocation:
    cabinet: int
    rack: int
    row: int

    def validate(self, max_cabinet: int=100, max_rack: int=100, max_row: int=100) -> None:
        if not (1 <= self.cabinet <= max_cabinet):
            raise ValueError(f"[{self.cabinet}] Invalid cabinet")
        if not (1 <= self.rack <= max_rack):
            raise ValueError(f"[{self.rack}] Invalid rack")
        if not (1 <= self.row <= max_row):
            raise ValueError(f"[{self}] Invalid row")

@dataclass
class Book:
    id: str
    title: str
    author: Optional[str]
    category: Optional[str]
    location: BookLocation
    signal_strength: int
    timestamp: datetime
    status: BookStatus

    def evaluate_signal(self) -> str:
        if self.signal_strength > -70:
            return "Strong"
        if self.signal_strength <= -70:
            return "Weak"
        return "Critical"

    def borrow(self) -> None:
        if self.status != BookStatus.PRESENT:
            raise ValueError("Book must be PRESENT to borrow.")
        if self.signal_strength <= -90:
            raise ValueError("Signal too weak to confirm presence.")
        self.status = BookStatus.BORROWED
        self.timestamp = datetime.now()
        print(f"{self.timestamp} printing timestamp from class Book method borrow()")

    def return_book(self) -> None:
        if self.status != BookStatus.BORROWED:
            raise ValueError("Book is not borrowed.")
        self.status = BookStatus.PRESENT
        self.timestamp = datetime.now()

    def mark_missing(self) -> None:
        self.status = BookStatus.MISSING
        self.timestamp = datetime.now()