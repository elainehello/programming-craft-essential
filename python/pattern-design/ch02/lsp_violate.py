"""
LSP (Liskov Substitution Principle) dictates how subclasses should relate to their superclasses.
If a program uses objects of a superclass, then substituting these objects with objects of a 
subclass should not alter the correctness and expected behavior of the program.

In other words: derived classes must be substitutable for their base classes without breaking
the application's functionality or violating the contract established by the base class.
"""

from typing import Protocol

# Protocol defines the expected contract/behavior
class Notifier(Protocol):
    def send(self, message: str) -> None:
        ...

"""
The Notifier protocol establishes a contract: any implementation must actually notify the user.
The expectation is that calling send() will deliver the message in some form.
"""

class EmailNotifier:
    def send(self, message: str) -> None:
        print(f"[EMAIL] Sent: {message}")

# *LSP Violation Example*
class SilentNotifier:
    def send(self, message: str) -> None:
        # LSP VIOLATION: This breaks the contract established by the Notifier protocol
        # The expectation is that messages get sent, but this implementation silently ignores them
        print("Doing nothing...\t(message ignored)")

def notify_user(notifier: Notifier) -> None:
    notifier.send("Welcome!")

if __name__ == "__main__":
    notify_user(EmailNotifier())   # ✔ behaves correctly
    notify_user(SilentNotifier())  # ❌ violates expectation
