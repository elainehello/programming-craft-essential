package org.elainehello.maze;

import org.elainehello.maze.core.MazeGame;
import org.elainehello.maze.api.MazeFactory;
import org.elainehello.maze.elements.Maze;
import org.elainehello.maze.elements.StandardMazeFactory;

public class Main {
    public static void main(String[] args) {
        // Create a MazeGame instance
        MazeGame game = new MazeGame();

        // Create a concrete factory (you'll need to choose one of your implementations)
        MazeFactory factory = new StandardMazeFactory();

        // Create the maze using the factory
        Maze maze = game.createMaze(factory);

        System.out.println("Maze created with " + maze.getRoomCount() + " rooms");
    }
}
