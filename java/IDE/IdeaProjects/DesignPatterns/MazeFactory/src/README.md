# Maze Factory - Abstract Factory Pattern Implementation

## Overview

This project demonstrates the **Abstract Factory Design Pattern** through a maze creation system. The pattern provides an interface for creating families of related objects without specifying their concrete classes.

## Project Structure

### 📁 Package Organization

```
org.elainehello.maze/
├── Main.java                 # Entry point
├── api/                      # Abstract interfaces
│   ├── Direction.java        # Enum for maze directions
│   ├── MapSite.java         # Abstract base for maze components
│   └── MazeFactory.java     # Abstract Factory interface
├── core/                     # Core game logic
│   └── MazeGame.java        # Client that uses the factory
└── elements/                 # Concrete implementations
    ├── Door.java            # Concrete maze door
    ├── Maze.java            # Maze container
    ├── Room.java            # Concrete maze room
    ├── StandardMazeFactory.java # Concrete factory
    └── Wall.java            # Concrete maze wall
```

## 🏗️ Abstract Factory Pattern Components

### 1. Abstract Factory Interface

**[`MazeFactory`](src/main/java/org/elainehello/maze/api/MazeFactory.java)**

- Declares methods for creating maze components
- `makeRoom(int n)` - Creates rooms
- `makeWall()` - Creates walls
- `makeDoor(Room r1, Room r2)` - Creates doors

### 2. Concrete Factory

**[`StandardMazeFactory`](src/main/java/org/elainehello/maze/elements/StandardMazeFactory.java)**

- Implements `MazeFactory` interface
- Creates standard maze components (rooms, walls, doors)
- Encapsulates object creation logic

### 3. Abstract Products

**[`MapSite`](src/main/java/org/elainehello/maze/api/MapSite.java)**

- Base class for all maze components
- Defines common `enter()` behavior

### 4. Concrete Products

- **[`Room`](src/main/java/org/elainehello/maze/elements/Room.java)** - Has 4 sides, room number, enter behavior
- **[`Wall`](src/main/java/org/elainehello/maze/elements/Wall.java)** - Solid barrier with collision message
- **[`Door`](src/main/java/org/elainehello/maze/elements/Door.java)** - Connects rooms, has open/closed state

### 5. Client

**[`MazeGame`](src/main/java/org/elainehello/maze/core/MazeGame.java)**

- Uses factory to create maze without knowing concrete classes
- `createMaze(MazeFactory factory)` method builds complete maze

## 🎯 Pattern Benefits Demonstrated

### ✅ Flexibility

- Easy to add new factory types (EnchantedMazeFactory, BombedMazeFactory)
- Client code remains unchanged when new factories are added

### ✅ Consistency

- Factory ensures all components work together (same family)
- Prevents mixing incompatible maze elements

### ✅ Encapsulation

- Object creation logic isolated in factories
- Client doesn't need to know concrete class details

## 🚀 Running the Application

```bash
# Compile and run
mvn compile exec:java -Dexec.mainClass="org.elainehello.maze.Main"

# Expected Output:
# Maze created with 2 rooms
```

## 🔧 Key Implementation Details

### Room Configuration

Each room has 4 sides (North, South, East, West) that can contain:

- Walls (impassable barriers)
- Doors (connections to other rooms)

### Factory Usage

```java
MazeGame game = new MazeGame();
MazeFactory factory = new StandardMazeFactory();
Maze maze = game.createMaze(factory);
```

### Design Pattern Adherence

- **Single Responsibility**: Each class has one reason to change
- **Open/Closed**: Open for extension (new factories), closed for modification
- **Dependency Inversion**: Client depends on abstractions, not concretions

## 🎨 Future Extensions

- **EnchantedMazeFactory** - Creates magical rooms with spells
- **BombedMazeFactory** - Creates damaged rooms with rubble
- **ThemeMazeFactory** - Creates themed mazes (medieval, sci-fi, etc.)

## 📚 Learning Outcomes

- Understanding Abstract Factory pattern structure
- Separating object creation from business logic
- Building flexible, extensible systems
- Working with inheritance hierarchies and polymorphism
