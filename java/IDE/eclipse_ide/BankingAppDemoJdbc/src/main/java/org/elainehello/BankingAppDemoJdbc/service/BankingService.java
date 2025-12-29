package org.elainehello.BankingAppDemoJdbc.service;

import org.elainehello.BankingAppDemoJdbc.dto.CustomerRegistrationRequest;
import org.elainehello.BankingAppDemoJdbc.dto.TransferRequest;
import org.elainehello.BankingAppDemoJdbc.model.Customer;
import org.elainehello.BankingAppDemoJdbc.model.Transaction;

import java.math.BigDecimal;

/**
 * SOLID - ISP: main banking service interface
 * Focused on core banking operations
 */
public interface BankingService {
    Customer createAccount(CustomerRegistrationRequest request);
    Customer authenticate(String username, String password);
    BigDecimal getBalance(Long customerId);
    Transaction transferMoney(TransferRequest transferRequest);
}
