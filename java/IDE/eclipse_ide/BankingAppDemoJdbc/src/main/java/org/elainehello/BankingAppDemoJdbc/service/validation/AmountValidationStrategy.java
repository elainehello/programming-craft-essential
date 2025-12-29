package org.elainehello.BankingAppDemoJdbc.service.validation;

import org.elainehello.BankingAppDemoJdbc.dto.TransferRequest;

import java.math.BigDecimal;

/**
 * SOLID - OCP: another validation strategy that extends functionality
 * without modifying existing validation logic
 */
public class AmountValidationStrategy implements ValidationStrategyInterface{
    private static final BigDecimal MIN_TRANSFER_AMOUNT = new BigDecimal("0.01");
    private static final BigDecimal MAX_TRANSFER_AMOUNT = new BigDecimal("10000.00");
    private String errorMessage;

    // Contract methods override due to Interface being implemented
    @Override
    public boolean isValid(TransferRequest request) {
        BigDecimal amount = request.getAmount();
        if (amount == null) {
            errorMessage = "Transfer amount cannot be null";
            return false;
        }
        if (amount.compareTo(MIN_TRANSFER_AMOUNT) < 0) {
            errorMessage = "Transfer amount must be at least" + MIN_TRANSFER_AMOUNT;
            return false;
        }
        if (amount.compareTo(MAX_TRANSFER_AMOUNT) > 0) {
            errorMessage = "Transfer amount cannot exceed" + MAX_TRANSFER_AMOUNT;
            return false;
        }
        return true;
    }

    @Override
    public String getErrorMessage() {
        return errorMessage;
    }
}
