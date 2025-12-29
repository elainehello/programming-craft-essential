package org.elainehello.BankingAppDemoJdbc.repository;

import org.elainehello.BankingAppDemoJdbc.model.Customer;

import java.math.BigDecimal;
import java.util.Optional;

public interface CustomerRepository {
    // Contract Interface
    Customer save(Customer customer);
    Optional<Customer> findByUsername(String username);
    Optional<Customer> findById(Long customerId);
    boolean updateBalance(Long customerId, BigDecimal newBalance);
    boolean existsByUsername(String username);
}
