"""
In a loosely coupled system, components are independent and interact through well-defined
interfaces aka (ABC/Protocol), making it easier to make changes to oner part without
affecting others.
"""

# Achieving loose coupling by using dependency injection

from typing import Protocol

class Sender(Protocol):
    def send(self, message: str) -> None:
        ...

class MessageService:
    def __init__(self, sender: Sender) -> None:
        self.sender = sender

    def send_message(self, message: str) -> None:
        self.sender.send(message)

class EmailSender:
    def send(self, message: str) -> None:
        print(f"Sending email: {message}")

class SMSSender:
    def send(self, message: str) -> None:
        print(f"Sending SMS: {message}")

if __name__ == "__main__":
    service_email = MessageService(EmailSender())
    service_email.send_message("Hello sending email from service email coupling impl")
    service_sms = MessageService(SMSSender())
    service_sms.send_message("Hello sending sms from service sms coupling impl")
