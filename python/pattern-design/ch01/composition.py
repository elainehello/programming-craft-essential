# Compose a car using engine

class Engine:
    def start(self) -> None:
        print("Engine Started!")

class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self) -> None:
        self.engine.start()
        print("Car Started!")

if __name__ == "__main__":
    # my_car = Car()
    # my_car.start()
    Car().start()
