# MazeGame - Design Patterns Demo

A Java implementation demonstrating object-oriented design patterns through a simple maze game. This project showcases the use of abstract classes, polymorphism, and encapsulation in creating a flexible maze structure.

## 🏗️ Architecture

### Design Patterns Used

- **Abstract Factory Pattern**: Ready for maze component creation
- **Strategy Pattern**: Different behaviors for maze elements via polymorphism
- **Composite Pattern**: Maze elements can contain other elements

### Project Structure

```
src/main/java/org/elainehello/maze/
├── Main.java                 # Demo application entry point
├── api/
│   ├── MapSite.java         # Abstract base class for all maze elements
│   └── Direction.java       # Enum for cardinal directions
└── elements/
    ├── Room.java            # Room implementation with sides
    ├── Wall.java            # Wall implementation (blocks movement)
    └── Door.java            # Door implementation (conditional passage)
```

## 🎮 Features

### Maze Elements

- **Rooms**: Numbered spaces that can be entered
- **Walls**: Impassable barriers that block movement
- **Doors**: Conditional passages between rooms (can be open/closed)

### Navigation System

- **4-Direction Movement**: NORTH, SOUTH, EAST, WEST
- **Polymorphic Behavior**: Each element responds differently to `enter()` calls
- **Type Safety**: Using `EnumMap` for direction-based storage

## 🚀 Getting Started

### Prerequisites

- Java 21 or higher
- Maven 3.6+

### Building and Running

```bash
# Navigate to project directory
cd /path/to/MazeGame

# Compile the project
mvn compile

# Run the demo
mvn exec:java -Dexec.mainClass="org.elainehello.maze.Main"
```

### Expected Output

```
=== Maze Game Demo ===

=== Testing Room Navigation ===
You are in room 1
You are in room 2

=== Testing Wall Interaction ===
You hit a cold stone wall
You hit a cold stone wall

=== Testing Door Interaction ===
The door is shut

=== Maze Demo Complete ===
```

## 🏛️ Core Components

### MapSite (Abstract Base Class)

```java
public abstract class MapSite {
    public abstract void enter();
}
```

- Defines the common interface for all maze elements
- Enforces implementation of `enter()` behavior

### Room

- Contains 4 sides (one for each direction)
- Uses `EnumMap<Direction, MapSite>` for type-safe storage
- Displays room number when entered

### Wall

- Blocks movement attempts
- Provides feedback when hit
- Immutable barrier element

### Door

- Connects two rooms
- Has open/closed state (currently defaults to closed)
- Conditional passage behavior

## 🔧 Key Design Features

### Encapsulation

- Private fields with controlled access
- `EnumMap` prevents invalid direction assignments
- Immutable room numbers and door connections

### Polymorphism

- All elements implement `MapSite.enter()`
- Runtime behavior varies by concrete type
- Enables flexible maze composition

### Type Safety

- `Direction` enum prevents invalid directions
- Compile-time checking for direction assignments
- No magic numbers or strings

## 🛠️ Extension Points

### Adding New Elements

1. Extend `MapSite` abstract class
2. Implement `enter()` method with desired behavior
3. Add to maze using `Room.setSide()`

### Example: Treasure Chest

```java
public class Treasure extends MapSite {
    @Override
    public void enter() {
        System.out.println("You found a treasure chest!");
    }
}
```

### Adding Door Controls

The `Door` class is ready for extended functionality:

```java
// Add to Door.java
public void setOpen(boolean open) {
    this.isOpen = open;
}

public Room getOtherRoom(Room currentRoom) {
    return (currentRoom == room1) ? room2 : room1;
}
```

## 🧪 Testing

The current demo tests:

- ✅ Room entry and identification
- ✅ Wall collision detection
- ✅ Door state checking
- ✅ Polymorphic behavior verification

## 📚 Learning Objectives

This project demonstrates:

- **Abstract Classes**: Defining common interfaces
- **Inheritance**: Extending base functionality
- **Polymorphism**: Runtime behavior selection
- **Encapsulation**: Data hiding and controlled access
- **Enum Usage**: Type-safe constants
- **Collection Framework**: Using `EnumMap` effectively

## 🔮 Future Enhancements

- [ ] Player movement system
- [ ] Maze generation algorithms
- [ ] Save/load maze configurations
- [ ] GUI interface
- [ ] Multiple maze levels
- [ ] Interactive door controls
- [ ] Maze solving algorithms

## 📄 License

This project is for educational purposes demonstrating Java design patterns and object-oriented programming concepts.

## 🤝 Contributing

Feel free to fork this project and experiment with:

- New maze element types
- Different maze layouts
- Enhanced player interactions
- Alternative design patterns

---

_Built with Java 21 and Maven_
