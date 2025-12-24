package org.elainehello.maze.core;

import org.elainehello.maze.api.*;
import org.elainehello.maze.elements.*;

public class MazeGame {
    
    // The Client method that uses the Abstract Factory
    public Maze createMaze(MazeFactory factory) {
        Maze aMaze = new Maze();
        
        Room r1 = factory.makeRoom(1);
        Room r2 = factory.makeRoom(2);
        Door theDoor = factory.makeDoor(r1, r2);

        aMaze.addRoom(r1);
        aMaze.addRoom(r2);

        r1.setSide(Direction.NORTH, factory.makeWall());
        r1.setSide(Direction.EAST, theDoor);
        
        r2.setSide(Direction.WEST, theDoor);
        r2.setSide(Direction.SOUTH, factory.makeWall());

        return aMaze;
    }
}