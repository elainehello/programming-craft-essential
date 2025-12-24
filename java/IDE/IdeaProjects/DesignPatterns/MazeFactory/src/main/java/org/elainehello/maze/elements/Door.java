package org.elainehello.maze.elements;

import org.elainehello.maze.api.MapSite;

public class Door extends MapSite {
    // attributes or properties
    private final Room room1;
    private final Room room2;
    private boolean isOpen;

    // constructor
    public Door(Room r1, Room r2) {
        this.room1 = r1;
        this.room2 = r2;
        this.isOpen = false;

    }

    @Override
    public void enter() {
        if (isOpen) {
            System.out.println("You pass through the door");
        } else {
            System.out.println("The door is shu");
        }
    }

}
