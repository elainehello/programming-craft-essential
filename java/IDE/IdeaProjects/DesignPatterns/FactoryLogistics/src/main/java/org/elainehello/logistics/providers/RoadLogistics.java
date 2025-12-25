package org.elainehello.logistics.providers;

import org.elainehello.logistics.api.LogisticsManager;
import org.elainehello.logistics.api.Transport;
import org.elainehello.logistics.beans.TruckBean;

public class RoadLogistics extends LogisticsManager {
    @Override
    public Transport createTransport() {
        TruckBean truckBean = new TruckBean();
        truckBean.setLicensePlate("TRK-7788");
        truckBean.setCapacity(15.5);
        return truckBean;
    }
}
