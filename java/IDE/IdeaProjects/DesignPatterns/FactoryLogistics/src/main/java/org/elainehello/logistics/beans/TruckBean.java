package org.elainehello.logistics.beans;

import org.elainehello.logistics.api.Transport;

import java.io.Serializable;

// serializable byte stream, save data somewhere else
public class TruckBean implements Transport, Serializable {
    private String licensePlate;
    private double capacity;

    // empty constructor java bean
    public TruckBean() {

    }

    // Getters and Setters
    public String getLicensePlate() {
        return licensePlate;
    }

    public void setLicensePlate(String licensePlate) {
        this.licensePlate = licensePlate;
    }

    public double getCapacity() {
        return capacity;
    }

    public void setCapacity(double capacity) {
        this.capacity = capacity;
    }

    @Override
    public void deliver() {
        System.out.println("Delivering by land in truck: " + licensePlate);
    }
}
