"""
Object Pool Design Pattern Implementation

This module demonstrates the Object Pool pattern, which manages a pool of 
reusable objects to improve performance and resource utilization.

The Object Pool pattern is useful when:
1. Object creation is expensive (database connections, heavy objects)
2. You need to limit the number of objects (memory constraints)
3. Objects can be reused after being returned to the pool
4. You want to avoid frequent allocation/deallocation overhead

Key Components:
- Pooled Object: Car (represents expensive-to-create objects)
- Object Pool: CarPool (manages available and in-use objects)
- Acquire/Release: Methods to get and return objects

Benefits:
- Reduces object creation overhead
- Controls resource usage
- Improves performance for expensive objects
- Memory management optimization

Example Use Cases:
- Database connection pools
- Thread pools
- Graphics object pools (sprites, textures)
- Network connection pools
"""
from typing import Dict

class Car:
    """
    Represents a pooled object - a car that can be borrowed and returned.
    
    This is the object that gets pooled. In real applications, this might
    be a database connection, network socket, or other expensive resource.
    """

    def __init__(self, make: str, model: str) -> None:
        """
        Initialize a car object.
        
        Args:
            make: The car manufacturer (e.g., "BMW", "Toyota")
            model: The car model (e.g., "M3", "Camry")
        """
        self.make = make
        self.model = model
        self.in_use: bool = False  # Track whether this car is currently borrowed

    def __str__(self) -> str:
        """Return a string representation of the car."""
        return f"{self.make} {self.model}"


class CarPool:
    """
    Object Pool implementation that manages a collection of Car objects.
    
    Maintains two lists:
    - _available: Cars ready to be borrowed
    - _in_use: Cars currently borrowed by clients
    
    This pattern ensures efficient reuse of Car objects without constantly
    creating and destroying them.
    """

    def __init__(self) -> None:
        """Initialize an empty car pool."""
        self._available: list[Car] = []  # Pool of available cars
        self._in_use: list[Car] = []     # Cars currently being used

    def acquire_car(self) -> Car:
        """
        Acquire a car from the pool for use.
        
        If no cars are available, creates a new one. Otherwise, reuses
        an existing car from the available pool.
        
        Returns:
            Car: A car object ready for use
        """
        # Check if we need to create a new car
        if len(self._available) == 0:
            print("No cars available, creating a new one...")
            new_car = Car("BMW", "M3")  # Create expensive object
            self._available.append(new_car)

        # Get a car from the available pool
        car = self._available.pop()

        # Move it to the in-use pool and mark as busy
        self._in_use.append(car)
        car.in_use = True

        print(f"Acquired car: {car} (Total available: {len(self._available)}, In use: {len(self._in_use)})")
        return car

    def release_car(self, car: Car) -> None:
        """
        Return a car to the pool for reuse.
        
        Args:
            car: The car object to return to the pool
            
        Raises:
            ValueError: If the car is not currently in use
        """
        if car not in self._in_use:
            raise ValueError("Car is not currently in use")

        # Mark car as available and move it back to available pool
        car.in_use = False
        self._in_use.remove(car)
        self._available.append(car)

        print(f"Released car: {car} (Total available: {len(self._available)}, In use: {len(self._in_use)})")
    def get_pool_stats(self) -> Dict[str, int]:
        """
        Get current pool statistics.
        
        Returns:
            Dict[str, int]: Statistics about the pool state
        """
        return {
            "available_cars": len(self._available),
            "cars_in_use": len(self._in_use),
            "total_cars": len(self._available) + len(self._in_use)
        }

def main() -> None:
    """
    Demonstrate the Object Pool pattern with multiple car acquisitions.
    
    Shows how the pool creates new objects when needed and reuses
    existing objects when they're returned.
    """
    print("=== Object Pool Pattern Demonstration ===\n")
    
    # Create the pool
    pool = CarPool()
    
    print("Initial pool state:")
    print(f"Pool stats: {pool.get_pool_stats()}\n")
    
    # Acquire first car
    print("Step 1: Acquire first car")
    car1 = pool.acquire_car()
    print(f"Car 1 in use: {car1.in_use}")
    print(f"Pool stats: {pool.get_pool_stats()}\n")
    
    # Acquire second car (will create new one)
    print("Step 2: Acquire second car")
    car2 = pool.acquire_car()
    print(f"Car 2 in use: {car2.in_use}")
    print(f"Pool stats: {pool.get_pool_stats()}\n")
    
    # Release first car
    print("Step 3: Release first car")
    pool.release_car(car1)
    print(f"Car 1 in use: {car1.in_use}")
    print(f"Pool stats: {pool.get_pool_stats()}\n")
    
    # Acquire third car (will reuse car1)
    print("Step 4: Acquire third car (should reuse existing)")
    car3 = pool.acquire_car()
    print(f"Car 3 in use: {car3.in_use}")
    print(f"Car 3 is same object as Car 1: {car3 is car1}")
    print(f"Pool stats: {pool.get_pool_stats()}\n")
    
    # Clean up - release all cars
    print("Step 5: Release all remaining cars")
    pool.release_car(car2)
    pool.release_car(car3)
    print(f"Final pool stats: {pool.get_pool_stats()}")


if __name__ == "__main__":
    main()

