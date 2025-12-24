package org.elainehello.maze.elements;

import java.util.HashMap;
import java.util.Map;

public class Maze {
    private final Map<Integer, Room> rooms = new HashMap<>();
    
    public void addRoom(Room room) {
        rooms.put(room.getRoomNumber(), room);
    }

    public Room getRoom(int roomNumber) {
        return rooms.get(roomNumber);
    }

    public int getRoomCount() {
        return rooms.size();
    }
}
