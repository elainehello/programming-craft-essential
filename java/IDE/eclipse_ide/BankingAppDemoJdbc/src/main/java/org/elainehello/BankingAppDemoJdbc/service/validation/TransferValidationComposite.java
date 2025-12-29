package org.elainehello.BankingAppDemoJdbc.service.validation;


import org.elainehello.BankingAppDemoJdbc.dto.TransferRequest;

import java.util.ArrayList;
import java.util.List;

/**
 * SOLID - SRP & OCP combined:
 * SRP: only responsable for orchestrating multiple validations
 * OCP: can add new validation strategies without modifying this class

 * Composite pattern: Treats individual validations and groups uniformly
 */
public class TransferValidationComposite implements ValidationStrategyInterface {
    // attribute - properties
    private final List<ValidationStrategyInterface> validationStrategies;
    private String errorMessage;

    // initialise attribute
    public TransferValidationComposite() {
        this.validationStrategies = new ArrayList<>();
    }

    /**
     * Adds a validation strategy to the composite
     * Demostrates OCP - extending behaviour through composition
     */
    @Override
    public boolean isValid(TransferRequest request) {
        for (ValidationStrategyInterface strategy : validationStrategies) {
            if (!strategy.isValid(request)) {
                this.errorMessage = strategy.getErrorMessage();
                return false;
            }
        }
        return true;
    }

    @Override
    public String getErrorMessage() {
        return errorMessage;
    }
}
