package org.elainehello.logistics.app;

import org.elainehello.logistics.api.LogisticsManager;
import org.elainehello.logistics.providers.RoadLogistics;

public class Main {
    public static void main(String[] args) {
        // Business Requirement: Deliver items via Road
        LogisticsManager roadLogistics = new RoadLogistics();

        // Execute the generic business logic
        roadLogistics.planDelivery();
    }
}