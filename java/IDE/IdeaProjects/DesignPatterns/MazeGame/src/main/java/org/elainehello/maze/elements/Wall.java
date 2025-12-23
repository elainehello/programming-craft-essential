package org.elainehello.maze.elements;

import org.elainehello.maze.api.MapSite;

public class Wall extends MapSite {

    // public constructor: accessible from anywhere
    // or by subclasses (Factory pattern ready)
   public Wall() {
        
    }

    /**
     * Implementation of the abstract enter() method from MapSite.
     * Defines the behavior when a player attempts to enter a wall -
     * they cannot pass through and receive feedback about hitting the wall.
     */
    @Override
    public void enter() {
        System.out.println("You hit a cold stone wall");
    }

}
