package org.elainehello.maze.elements;

import org.elainehello.maze.api.MazeFactory;

public class StandardMazeFactory implements MazeFactory {
    @Override
    public Room makeRoom(int n) {
        // return new object creation
        return new Room(n);
    }

    @Override
    public Wall makeWall() {
        // return new object creation
        return new Wall();
    }

    @Override
    public Door makeDoor(Room r1, Room r2) {
        // return new object creation
        return new Door(r1, r2);
    }
}
