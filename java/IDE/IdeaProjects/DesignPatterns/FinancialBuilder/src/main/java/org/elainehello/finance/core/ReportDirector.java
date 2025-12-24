package org.elainehello.finance.core;

import org.elainehello.finance.api.Report;
import org.elainehello.finance.api.ReportBuilder;
import org.elainehello.finance.api.Transaction;

import java.util.List;
/*
*   Controls the sequence of construction (Header -> Data -> Footer)
* */
public class ReportDirector {

    // The Director takes data and the builder to assemble the result
    public Report construct(ReportBuilder builder,
                            String company,
                            List<Transaction> transactions) {
        builder.createNewReport();
        builder.buildHeader(company);
        builder.buildContent(transactions);
        builder.buildFooter();
        return builder.getResult();
    }
}
