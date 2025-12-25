# Factory Logistics - Factory Method Pattern Implementation

## Overview

This project demonstrates the **Factory Method Design Pattern** through a logistics management system. The pattern allows creating different types of transport vehicles without specifying their exact classes in the client code.

## Pattern Structure

### Core Components

- **Abstract Creator**: [`LogisticsManager`](src/main/java/org/elainehello/logistics/api/LogisticsManager.java) - Defines the factory method and contains business logic
- **Concrete Creator**: [`RoadLogistics`](src/main/java/org/elainehello/logistics/providers/RoadLogistics.java) - Implements the factory method to create specific transport
- **Product Interface**: [`Transport`](src/main/java/org/elainehello/logistics/api/Transport.java) - Defines the contract for all transport types
- **Concrete Product**: [`TruckBean`](src/main/java/org/elainehello/logistics/beans/TruckBean.java) - Implements specific transport behavior

## Project Structure

```
src/main/java/org/elainehello/logistics/
├── api/                    # Interfaces and abstract classes
│   ├── LogisticsManager.java   # Abstract creator with factory method
│   └── Transport.java          # Product interface
├── beans/                  # Concrete product implementations
│   └── TruckBean.java         # Truck implementation with JavaBean pattern
├── providers/              # Concrete creator implementations
│   └── RoadLogistics.java     # Factory for road transport
└── app/                    # Application entry point
    └── Main.java              # Demonstrates the pattern usage
```

## Key Features

- ✅ **Factory Method Pattern** - Clean separation of object creation logic
- ✅ **JavaBean Compliance** - Serializable objects with getters/setters
- ✅ **Extensible Design** - Easy to add new transport types
- ✅ **Maven Project** - Standard Java project structure
- ✅ **Java 21 Compatible** - Modern Java features support

## How It Works

1. **Client Code** ([`Main.java`](src/main/java/org/elainehello/logistics/app/Main.java)) requests delivery service
2. **Creator** ([`RoadLogistics`](src/main/java/org/elainehello/logistics/providers/RoadLogistics.java)) creates appropriate transport via factory method
3. **Business Logic** ([`LogisticsManager.planDelivery()`](src/main/java/org/elainehello/logistics/api/LogisticsManager.java)) executes generic delivery workflow
4. **Product** ([`TruckBean`](src/main/java/org/elainehello/logistics/beans/TruckBean.java)) performs specific delivery implementation

## Running the Application

### Prerequisites

- Java 21 or higher
- Maven 3.6+

### Build and Run

```bash
# Compile the project
mvn clean compile

# Run the application
mvn exec:java -Dexec.mainClass="org.elainehello.logistics.app.Main"

# Or compile and run manually
mvn clean package
java -cp target/classes org.elainehello.logistics.app.Main
```

### Expected Output

```
Logistics: Initialising shipment sequence...
Delivering by land in truck: TRK-7788
```

## Extending the Pattern

To add new transport types (e.g., Sea Logistics):

1. **Create Product**: `ShipBean implements Transport`
2. **Create Creator**: `SeaLogistics extends LogisticsManager`
3. **Implement Factory Method**: Return new `ShipBean()` instance

## Benefits of This Implementation

- **Loose Coupling**: Client code doesn't depend on concrete classes
- **Open/Closed Principle**: Easy to extend without modifying existing code
- **Single Responsibility**: Each class has one reason to change
- **Maintainable**: Clear separation of concerns

## Technologies Used

- **Java 21** - Programming language
- **Maven 3** - Build and dependency management
- **Factory Method Pattern** - Creational design pattern
- **JavaBean Standard** - Object serialization and property access

---

_Author: elainehello_  
_Version: 1.0_
