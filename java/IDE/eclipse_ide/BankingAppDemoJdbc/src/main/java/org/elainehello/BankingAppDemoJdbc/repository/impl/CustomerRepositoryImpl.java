package org.elainehello.BankingAppDemoJdbc.repository.impl;

import org.elainehello.BankingAppDemoJdbc.model.Customer;
import org.elainehello.BankingAppDemoJdbc.repository.CustomerRepository;
import org.elainehello.BankingAppDemoJdbc.config.DatabaseConfig;

import java.sql.*;
import java.util.Optional;

public class CustomerRepositoryImpl implements CustomerRepository {

    // attribute - property
    private final DatabaseConfig databaseConfig;

    // attribute initialise
    public CustomerRepositoryImpl(DatabaseConfig databaseConfig) {
        this.databaseConfig = databaseConfig;
    }

    // Implementing from CustomerRepository type 'Interface', contract
    @Override
    public Customer save(Customer customer) {
        String sql = "INSERT INTO customers (username, password_hash, first_name, last_name, email, balance, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?)";

        try (Connection conn = databaseConfig.getConnection();
             PreparedStatement stmt = conn.prepareStatement(sql, Statement.RETURN_GENERATED_KEYS)) {

            stmt.setString(1, customer.getUsername());
            stmt.setString(2, customer.getPasswordHash());
            stmt.setString(3, customer.getFirstName());
            stmt.setString(4, customer.getLastName());
            stmt.setString(5, customer.getEmail());
            stmt.setBigDecimal(6, customer.getBalance());
            stmt.setTimestamp(7, Timestamp.valueOf(customer.getCreatedAt()));
            stmt.setTimestamp(8, Timestamp.valueOf(customer.getUpdatedAt()));

            int affectedRows = stmt.executeUpdate();
            if (affectedRows > 0) {
                try (ResultSet generatedKeys = stmt.getGeneratedKeys()) {
                    if (generatedKeys.next()) {
                        customer.setCustomerId(generatedKeys.getLong(1));
                    }
                }
            }
            return customer;
        } catch (SQLException e) {
            throw new RuntimeException("Error saving customer", e);
        }
    }

    @Override
    public Optional<Customer> findByUsername(String username) {
        String sql = "SELECT * FROM customers WHERE username = ?";

        try (Connection conn = databaseConfig.getConnection();
            PreparedStatement stmt = conn.prepareStatement(sql)) {

            stmt.setString(1, username);
            try (ResultSet rs = stmt.executeQuery()) {
                if (rs.next()) {
                    return Optional.of(mapResultSetToCustomer(rs));
                }
            }
        } catch (SQLException e) {
            throw new RuntimeException("Error finding customer by username", e);
        }
        return Optional.empty();
    }

    // util function called above
    private Customer mapResultSetToCustomer(ResultSet rs) throws SQLException {
        // create new object instance
        Customer customer = new Customer();

        customer.setCustomerId(rs.getLong("customer_id"));
        customer.setUsername(rs.getString("username"));
        customer.setPasswordHash(rs.getString("password_hash"));
        customer.setFirstName(rs.getString("first_name"));
        customer.setLastName(rs.getString("last_name"));
        customer.setEmail(rs.getString("email"));
        customer.setBalance(rs.getBigDecimal("balance"));
        customer.setCreatedAt(rs.getTimestamp("created_at").toLocalDateTime());
        customer.setUpdatedAt(rs.getTimestamp("created_at").toLocalDateTime());
        return customer;
    }

}
