package org.elainehello.BankingAppDemoJdbc.model;

import java.math.BigDecimal;
import java.time.LocalDateTime;

public class Transaction {
    public enum TransactionType {
        TRANSFER,
        DEPOSIT,
        WITHDRAWAL
    }

    // attributes - properties
    private Long transactionId;
    private Long fromCustomerId;
    private Long toCustomerId;
    private BigDecimal amount;
    private TransactionType type;
    private String description;
    private LocalDateTime timestamp;

    // Constructor
    public Transaction(Long transactionId, Long fromCustomerId, Long toCustomerId,
                       BigDecimal amount, TransactionType type, String description,
                       LocalDateTime timestamp) {
        this.transactionId = transactionId;
        this.fromCustomerId = fromCustomerId;
        this.toCustomerId = toCustomerId;
        this.amount = amount;
        this.type = type;
        this.description = description;
        this.timestamp = timestamp;
    }

    // Getter and Setter
    public Long getTransactionId() {
        return transactionId;
    }

    public void setTransactionId(Long transactionId) {
        this.transactionId = transactionId;
    }

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

    public TransactionType getType() {
        return type;
    }

    public void setType(TransactionType type) {
        this.type = type;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public LocalDateTime getTimestamp() {
        return timestamp;
    }

    public void setTimestamp(LocalDateTime timestamp) {
        this.timestamp = timestamp;
    }
}
