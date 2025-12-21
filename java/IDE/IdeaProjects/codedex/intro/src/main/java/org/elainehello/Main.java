package org.elainehello;

import org.elainehello.operation.DecompositionSim;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {
        DecompositionSim sim = new DecompositionSim();
        System.out.println("Testing DecompositionSim class");
        System.out.println("Calculation " + sim.getRatio());
    }
}