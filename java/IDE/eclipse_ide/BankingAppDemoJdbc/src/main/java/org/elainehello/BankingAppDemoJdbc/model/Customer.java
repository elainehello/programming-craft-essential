package org.elainehello.BankingAppDemoJdbc.model;

import java.math.BigDecimal;
import java.time.LocalDateTime;
//(*) look at java.util.Objects Java 21 Docs API
import java.util.Objects;

/**
 * SOLID - SRP: this class is ONLY responsable for representing customer
 * data; It doesn't handle database operation, business logic, or UI concerns
 */

public class Customer {
    // attributes - properties
    private Long customerId;
    private String username;
    private String passwordHash;
    private String firstName;
    private String lastName;
    private String email;
    private BigDecimal balance;
    private LocalDateTime createdAt;
    private LocalDateTime updatedAt;

    // Constructors
    public Customer() {
        this.createdAt = LocalDateTime.now();
        this.updatedAt = LocalDateTime.now();
    }

    public Customer(String username, String passwordHash, String firstName,
                    String lastName, String email, BigDecimal balance) {
        this();
        this.username = username;
        this.passwordHash = passwordHash;
        this.firstName = firstName;
        this.lastName = lastName;
        this.email = email;
        this.balance = balance;
    }

    // Business method following SRP - onlu updates what belongs to Customer
    public void updateBalance(BigDecimal newBalance) {
        this.balance = newBalance;
        this.updatedAt = LocalDateTime.now();
    }

    // Getter and Setter
    public Long getCustomerId() {
        return customerId;
    }

    public void setCustomerId(Long customerId) {
        this.customerId = customerId;
    }

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public String getPasswordHash() {
        return passwordHash;
    }

    public void setPasswordHash(String passwordHash) {
        this.passwordHash = passwordHash;
    }

    public String getFirstName() {
        return firstName;
    }

    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }

    public String getLastName() {
        return lastName;
    }

    public void setLastName(String lastName) {
        this.lastName = lastName;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public BigDecimal getBalance() {
        return balance;
    }

    public void setBalance(BigDecimal balance) {
        this.balance = balance;
    }

    public LocalDateTime getCreatedAt() {
        return createdAt;
    }

    public void setCreatedAt(LocalDateTime createdAt) {
        this.createdAt = createdAt;
    }

    public LocalDateTime getUpdatedAt() {
        return updatedAt;
    }

    public void setUpdatedAt(LocalDateTime updatedAt) {
        this.updatedAt = updatedAt;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) {
            return true;
        }
        if (o == null || getClass() != o.getClass()) {
            return false;
        }
        Customer customer = (Customer) o;
        return Objects.equals(customerId, customer.customerId) &&
                Objects.equals(username, customer.username);
    }

    @Override
    public int hashCode() {
        return Objects.hash(customerId, username);
    }

    @Override
    public String toString() {
        return "Customer{" +
                "customerId=" + customerId +
                ", username=" + username + '\'' +
                ", firstName=" + firstName + '\'' +
                ", lastName=" + lastName + '\'' +
                ", email=" + email + '\'' +
                ", balance=" + balance + '\'' +
                ", createAt=" + createdAt + '\'' +
                '}';
    }
}
