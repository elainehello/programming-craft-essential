package org.elainehello.maze;

import org.elainehello.maze.api.Direction;
import org.elainehello.maze.elements.Door;
import org.elainehello.maze.elements.Room;
import org.elainehello.maze.elements.Wall;


public class Main {
    public static void main(String[] args) {
        System.out.println("=== Maze Game Demo ===");

        // Create rooms
        Room r1 = new Room(1);
        Room r2 = new Room(2);

        // Create door between rooms
        Door theDoor = new Door(r1, r2);

        // Setup Room 1 - all four sides
        r1.setSide(Direction.EAST, theDoor);
        r1.setSide(Direction.WEST, new Wall());
        r1.setSide(Direction.NORTH, new Wall());
        r1.setSide(Direction.SOUTH, new Wall());

        // Setup Room 2 - all four sides
        r2.setSide(Direction.WEST, theDoor);
        r2.setSide(Direction.EAST, new Wall());
        r2.setSide(Direction.NORTH, new Wall());
        r2.setSide(Direction.SOUTH, new Wall());

        // Demonstrate the maze functionality
        System.out.println("\n=== Testing Room Navigation ===");

        // Test entering rooms
        r1.enter();
        r2.enter();

        System.out.println("\n=== Testing Wall Interaction ===");
        // Test hitting walls
        r1.getSide(Direction.WEST).enter(); // Should hit wall
        r1.getSide(Direction.NORTH).enter(); // Should hit wall

        System.out.println("\n=== Testing Door Interaction ===");
        // Test going through door
        r1.getSide(Direction.EAST).enter(); // Should encounter door

        System.out.println("\n=== Maze Demo Complete ===");
    }
}
