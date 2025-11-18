"""
Different types of logger, create a loggin interface allow for different
types of logging mechanisms
"""

from abc import ABC, abstractmethod

class Logger(ABC):
    @abstractmethod
    def log(self, message: str) -> None:
        pass

class ConsoleLogger(Logger):
    def log(self, message: str) -> None:
        print(f"Console: {message}")

class FileLogger(Logger):
    def log(self, message: str) -> None:
        with open("log.txt", "a") as f:
            f.write(f"File: {message}\n")

def log_message(logger: Logger, message: str) -> None:
    logger.log(message)

if __name__ == "__main__":
    log_message(ConsoleLogger(), "This is a console log message ^^")
    log_message(FileLogger(), "This is a file log message ^^")
