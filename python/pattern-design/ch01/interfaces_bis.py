"""
Different types of logger, now using Protocols
"""
from typing import Protocol

class Logger(Protocol):
    def log(self, message: str) -> None:
        ... # Elipses stand for method must exist, if applicable return the type
    
class ConsoleLogger:
    def log(self, message: str) -> None:
        print(f"Console msg: {message}")

class FileLogger:
    def log(self, message: str) -> None:
        with open("log.txt", "a") as f:
            f.write(f"File msg: {message}\n")

def log_message(logger: Logger, message: str) -> None:
    logger.log(message)

if __name__ == "__main__":
    log_message(ConsoleLogger(), "This is a console protocol message\n")
    log_message(FileLogger(), "This is a file protocol message\n")
