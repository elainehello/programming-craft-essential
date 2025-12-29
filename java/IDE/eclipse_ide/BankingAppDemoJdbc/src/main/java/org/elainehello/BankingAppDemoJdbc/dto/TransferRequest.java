package org.elainehello.BankingAppDemoJdbc.dto;

import java.math.BigDecimal;

// Data Transfer Object - (DTO)

/**
 * SOLID - SRP: this DTO class has ONE responsibility - transfer request data
 * It doesn't handle validation logic, business rules, or persistence
 * It's a pure data container with basic validation annotations
 */
public class TransferRequest {

    // attributes - properties
    private Long fromCustomerId;
    private Long toCustomerId;
    private BigDecimal amount;
    private String description;

    // Empty constructor
    public TransferRequest () {

    }

    // Constructor
    public TransferRequest(Long fromCustomerId, Long toCustomerId, BigDecimal amount, String description) {
        this.fromCustomerId = fromCustomerId;
        this.toCustomerId = toCustomerId;
        this.amount = amount;
        this.description = description;
    }

    // Getter and Setter

    public Long getFromCustomerId() {
        return fromCustomerId;
    }

    public void setFromCustomerId(Long fromCustomerId) {
        this.fromCustomerId = fromCustomerId;
    }

    public Long getToCustomerId() {
        return toCustomerId;
    }

    public void setToCustomerId(Long toCustomerId) {
        this.toCustomerId = toCustomerId;
    }

    public BigDecimal getAmount() {
        return amount;
    }

    public void setAmount(BigDecimal amount) {
        this.amount = amount;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }


    // Overriding toString method to output parameters
    @Override
    public String toString() {
        return "TransferRequest {" +
                "fromCustomerId=" + fromCustomerId +
                ", toCustomerId=" + toCustomerId +
                ", amount=" + amount +
                ", description=" + description + '\'' +
                '}';
    }
}
