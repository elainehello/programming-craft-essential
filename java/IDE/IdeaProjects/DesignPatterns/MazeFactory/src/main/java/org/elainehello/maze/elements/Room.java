package org.elainehello.maze.elements;

import org.elainehello.maze.api.MapSite;
import org.elainehello.maze.api.Direction;

import java.util.EnumMap;
import java.util.Map;

public class Room extends MapSite {
    // attribute
    private final int roomNumber;

    private final Map<Direction, MapSite> sides = new EnumMap<>(Direction.class);

    // constructor
    public Room(int roomNo) {
        this.roomNumber = roomNo;
    }

    // getter/setter
    public void setSide(Direction direction, MapSite site) {
        sides.put(direction, site);
    }

    public MapSite getSide(Direction direction) {
        return sides.get(direction);
    }

    // override abstract method
    @Override
    public void enter() {
        System.out.println("You are in room " + roomNumber);
    }

    public int getRoomNumber() {
        return roomNumber;
    }

}
