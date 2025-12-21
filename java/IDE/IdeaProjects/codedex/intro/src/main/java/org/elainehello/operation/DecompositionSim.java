package org.elainehello.operation;

public class DecompositionSim {
    // The ratio of the products after decomposition
    double chemicalA = 40.0;
    double chemicalB = 60.0;

    // chemical AB calculation
    double chemicalAB = chemicalA + chemicalB;

    // equation A + B / AB
    double ratio = (chemicalA + chemicalB) / chemicalAB;

    public double getRatio() {
        return (ratio);
    }
    
    /*public static void main(String[] args) {
        DecompositionSim sim = new DecompositionSim();
        System.out.println("Calculation " + sim.ratio);
    }*/

}
