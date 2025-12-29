package org.elainehello.BankingAppDemoJdbc.service.validation;

import org.elainehello.BankingAppDemoJdbc.dto.TransferRequest;
import org.elainehello.BankingAppDemoJdbc.repository.CustomerRepository;

/**
 * Open/Closed Principle (OCP)
 * SOLID - OCP: Concrete validation strategy for balance checking
 * Extends functionality without modifying existing validation logic
 */

public class BalanceValidationStrategy implements ValidationStrategyInterface {
    // attributes - properties
    private final CustomerRepository customerRepository;
    private String errorMessage;

    // Constructor
    public BalanceValidationStrategy(CustomerRepository customerRepository) {
        this.customerRepository = customerRepository;
    }

    @Override
    public boolean isValid(TransferRequest request) {
        var customer = customerRepository.findById(request.getFromCustomerId());
        if (customer.isEmpty()) {
            errorMessage = "Source customer not found";
            return false;
        }

        if (customer.get().getBalance().compareTo(request.getAmount()) < 0) {
            errorMessage = "Insufficient funds";
            return false;
        }

        return true;
    }

    @Override
    public String getErrorMessage() {
        return errorMessage;
    }
}
