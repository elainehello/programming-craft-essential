package org.elainehello.BankingAppDemoJdbc.model;

import java.math.BigDecimal;
import java.time.LocalDateTime;
import java.util.Objects;

/**
 * SOLID - SRP: Transaction model has ONE responsibility - representing
 * transaction data
 * No business logic, no database operations, no UI concerns
 */
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
    private String status;

    // Default Constructor
    public Transaction() {
        this.timestamp = LocalDateTime.now();
        this.status = "PENDING";
    }

    // Constructor with parameters - Fixed: Now properly calls default constructor
    public Transaction(Long fromCustomerId, Long toCustomerId,
            BigDecimal amount, TransactionType type, String description) {
        this(); // Calls default constructor to set timestamp and status
        this.fromCustomerId = fromCustomerId;
        this.toCustomerId = toCustomerId;
        this.amount = amount;
        this.type = type;
        this.description = description;
    }

    // Full Constructor (usually used when loading from database)
    public Transaction(Long transactionId, Long fromCustomerId, Long toCustomerId,
            BigDecimal amount, TransactionType type, String description,
            LocalDateTime timestamp, String status) {
        this.transactionId = transactionId;
        this.fromCustomerId = fromCustomerId;
        this.toCustomerId = toCustomerId;
        this.amount = amount;
        this.type = type;
        this.description = description;
        this.timestamp = timestamp;
        this.status = status;
    }

    // Business methods following SRP
    public void markAsCompleted() {
        this.status = "COMPLETED";
    }

    public void markAsFailed() {
        this.status = "FAILED";
    }

    public boolean isPending() {
        return "PENDING".equals(this.status);
    }

    public boolean isCompleted() {
        return "COMPLETED".equals(this.status);
    }

    // Getters and Setters
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

    // Fixed: Added missing getter and setter for status
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    // Override equals and hashCode for proper object comparison
    @Override
    public boolean equals(Object o) {
        if (this == o)
            return true;
        if (o == null || getClass() != o.getClass())
            return false;
        Transaction that = (Transaction) o;
        return Objects.equals(transactionId, that.transactionId) &&
                Objects.equals(fromCustomerId, that.fromCustomerId) &&
                Objects.equals(toCustomerId, that.toCustomerId) &&
                Objects.equals(amount, that.amount) &&
                type == that.type &&
                Objects.equals(timestamp, that.timestamp);
    }

    @Override
    public int hashCode() {
        return Objects.hash(transactionId, fromCustomerId, toCustomerId, amount, type, timestamp);
    }

    @Override
    public String toString() {
        return "Transaction{" +
                "transactionId=" + transactionId +
                ", fromCustomerId=" + fromCustomerId +
                ", toCustomerId=" + toCustomerId +
                ", amount=" + amount +
                ", type=" + type +
                ", description='" + description + '\'' +
                ", timestamp=" + timestamp +
                ", status='" + status + '\'' +
                '}';
    }
}
