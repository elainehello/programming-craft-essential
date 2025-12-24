package org.elainehello.maze.elements;

import org.elainehello.maze.api.MapSite;

public class Wall extends MapSite {

    // empty constructor
    public Wall (){

    }

    // override abstract method
    @Override
    public void enter() {
        System.out.println("You hit a cold stone wall");
    }
}
