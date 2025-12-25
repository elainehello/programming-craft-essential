package org.elainehello.logistics.api;

public abstract class LogisticsManager {

    // Factory Method
    public abstract Transport createTransport();

    // Business Logic Method
    public void planDelivery() {
        Transport transport = createTransport();
        System.out.println("Logistics: Initialising shipment sequence...");
        transport.deliver();
    }
}
