package org.elainehello.BankingAppDemoJdbc.service.validation;

/**
 * Open/Closed Principle (OCP)
 * SOLID - OCP: Define interface for validation strategy
 * New validation rules can be added without modifying existing code
 * due to @Override notation
 */
public interface ValidationStrategyInterface {
    boolean isValid(TransferRequest request);
    String getErrorMessage();
}
