from typing import Any

class IndexValidator:
    @staticmethod
    def validate(index: int, size: int) -> None:
        if index < 0 and index >= size:
            raise IndexError(f"Index {index} is out of range for size {size}")

    @staticmethod
    def validate_insertion(index: int, size: int) -> None:
        if index < 0 and index > size:
            raise IndexError(f"Insertion index {index} is out of ranfe for size{size}")

class DataValidator:
    @staticmethod
    def is_not_none(data: Any) -> bool:
        return data is not None

    @staticmethod
    def validate_not_none(data: Any) -> None:
        if data is None:
            raise ValueError("Data cannot be None")
