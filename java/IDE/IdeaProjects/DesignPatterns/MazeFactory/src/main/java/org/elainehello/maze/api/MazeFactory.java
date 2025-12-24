package org.elainehello.maze.api;

import org.elainehello.maze.elements.*;

public interface MazeFactory {
    // CreateProductA()
    Room makeRoom(int n);

    // CreateProductB()
    Wall makeWall();

    Door makeDoor(Room r1, Room r2);
}
