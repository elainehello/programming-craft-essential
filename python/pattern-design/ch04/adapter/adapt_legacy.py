"""
Adapter Design Pattern - Legacy System Integration

This module demonstrates the Adapter pattern, which allows incompatible 
interfaces to work together. The pattern is particularly useful when 
integrating legacy systems with new components.

Key Components:
- Target Interface: The interface expected by client code
- Adaptee: The existing class with incompatible interface
- Adapter: Converts the adaptee's interface to match the target
- Client: Uses objects through the target interface

Use Case: Adapting a new payment system to work with legacy code
that expects the old payment interface.
"""

from typing import Protocol

class PaymentInterface(Protocol):
    def make_payment(self, amount: float) -> None:
        ...

class OldPaymentSystem:
    def __init__(self, currency: str) -> None:
        self.currency = currency

    def make_payment(self, amount: float) -> None:
        print(f"[OLD] Pay {amount} {self.currency}")

class NewPaymentSystem:
    def __init__(self, currency: str) -> None:
        self.currency = currency

    def execute_payment(self, amount: float) -> None:
        print(f"Execute payment of {amount} {self.currency}")

class PaymentAdapter:
    def __init__(self, new_system: NewPaymentSystem) -> None:
        self.new_system = new_system

    def make_payment(self, amount: float) -> None:
        self.new_system.execute_payment(amount)

def process_payment(payment_system: PaymentInterface, amount: float) -> None:
    payment_system.make_payment(amount)

def main() -> None:
    old_system = OldPaymentSystem("euro")
    new_system = NewPaymentSystem("euro")
    adapter = PaymentAdapter(new_system)

    print("Using old system:")
    process_payment(old_system, 100)

    print("\nUsing new system through adapter:")
    process_payment(adapter, 100)

    print("\nInterface compatibility:")
    print(f"Old System has make_payment: {hasattr(old_system, 'make_payment')}")
    print(f"New System has make_payment: {hasattr(new_system, 'make_payment')}")
    print(f"Adapter has make_payment: {hasattr(adapter, 'make_payment')}")

if __name__ == "__main__":
    main()
