package org.elainehello.BankingAppDemoJdbc.service.validation;

import org.elainehello.BankingAppDemoJdbc.dto.TransferRequest;
import org.elainehello.BankingAppDemoJdbc.repository.CustomerRepository;

/**
 * SOLID - OCP: validates customer existence without modifying other validations
 */
public class CustomerValidationStrategy implements ValidationStrategyInterface{
    private final CustomerRepository customerRepository;
    private String errorMessage;

    // Constructor
    public CustomerValidationStrategy (CustomerRepository customerRepository) {
        this.customerRepository = customerRepository;
    }

    // Override methods from interface being impl
    @Override
    public boolean isValid(TransferRequest request) {
        // Check if source customer exists
        if (!customerRepository.existsById(request.getFromCustomerId())) {
            errorMessage = "Source customer does not exist";
            return false;
        }

        // Check if destination customer exists
        if (!customerRepository.existsById(request.getToCustomerId())) {
            errorMessage = "Destination customer does not exist";
            return false;
        }

        // Check if trying to transfer to same account
        if (request.getFromCustomerId().equals(request.getToCustomerId())) {
            errorMessage = "Cannot transfer to the same account";
            return false;
        }

        return true;
    }

    @Override
    public String getErrorMessage() {
        return errorMessage;
    }
}
