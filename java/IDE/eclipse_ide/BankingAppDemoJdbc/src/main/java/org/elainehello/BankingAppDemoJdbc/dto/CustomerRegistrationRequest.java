package org.elainehello.BankingAppDemoJdbc.dto;

import  java.math.BigDecimal;
/**
 * SOLID - SRP: handles ONLY customer registration data transfer
 */
public class CustomerRegistrationRequest {

    // attributes - properties
    private String username;
    private String password;
    private String firstName;
    private String lastName;
    private String email;
    private BigDecimal initialBalance;

    // Empty constructor
    public CustomerRegistrationRequest() {

    }

    // Constructor
    public CustomerRegistrationRequest(String username, String password, String firstName,
                                       String lastName, String email, BigDecimal initialBalance) {
        this.username = username;
        this.password = password;
        this.firstName = firstName;
        this.lastName = lastName;
        this.email = email;
        this.initialBalance = initialBalance;
    }

    // Getters and Setters
    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
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

    public BigDecimal getInitialBalance() {
        return initialBalance;
    }

    public void setInitialBalance(BigDecimal initialBalance) {
        this.initialBalance = initialBalance;
    }
}
