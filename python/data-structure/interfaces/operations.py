from typing import Any, Protocol

class PushSwapOperations(Protocol):
    """Protocol for the 11 core push_swap operations"""

    # Swap operations
    def sa(self) -> bool:
        """Swap the first 2 elements at the top of stack a"""
        ...

    def sb(self) -> bool:
        """Swap the first 2 elements at the top of stack b"""
        ...

    def ss(self) -> bool:
        """sa and sb at the same time"""
        ...

    # Push operations
    def pa(self) -> bool:
        """Take the first element at the top of b and put it at the top of a"""
        ...

    def pb(self) -> bool:
        """Take the first element at the top of a and put it at the top of b"""
        ...

    # Rotate operations
    def ra(self) -> bool:
        """Shift up all elements of stack a by 1. First element becomes the last one"""
        ...

    def rb(self) -> bool:
        """Shift up all elements of stack b by 1. First element becomes the last one"""
        ...

    def rr(self) -> bool:
        """ra and rb at the same time"""
        ...

    # Reverse rotate operations
    def rra(self) -> bool:
        """Shift down all elements of stack a by 1. Last element becomes the first one"""
        ...

    def rrb(self) -> bool:
        """Shift down all elements of stack b by 1. Last element becomes the first one"""
        ...

    def rrr(self) -> bool:
        """rra and rrb at the same time"""
        ...
