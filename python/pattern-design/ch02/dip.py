"""
DIP (Dependency Inversion Principle) states that high-level modules should not depend
on low-level modules. Both should depend on abstractions (interfaces/protocols).
Also, abstractions should not depend on details; details should depend on abstractions.

This example shows how the Notification class (high-level) depends on the MessageSender
protocol (abstraction) rather than concrete implementations like Email (low-level).
This makes the code flexible and easily testable.
"""

from typing import Protocol

class MessageSender(Protocol):
    def send(self, message: str) -> None:
        ...

class Email:
    def send(self, message: str) -> None:
        print(f"Sending email: {message}")

class Notification:
    def __init__(self, sender: MessageSender):
        self.sender = sender

    def send(self, message: str) -> None:
        self.sender.send(message)

if __name__ == "__main__":
    email = Email()
    notif = Notification(sender=email) # initialise/instantiate object
    notif.send(message="This is the message")
