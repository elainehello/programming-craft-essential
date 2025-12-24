package org.elainehello.finance.api;

import java.util.List;
/*
*   The interface (or abstract class) defining the construction steps
* */
public abstract class ReportBuilder {
    protected Report report;

    public void createNewReport() {
        report = new Report();
    }

    public abstract void buildHeader(String companyName);

    // this now buildContent() accepts the real data
    public abstract void buildContent(List<Transaction> data);

    public abstract void buildFooter();

    public Report getResult() {
        return report;
    }
}
