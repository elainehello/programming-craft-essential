package org.elainehello.BankingAppDemoJdbc.config;

import java.io.IOException;
import java.io.InputStream;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.util.Properties;

public class DatabaseConfig {
    // attributes - properties
    private static DatabaseConfig instance;
    private String url;
    private String username;
    private String password;

    private DatabaseConfig() {
        loadProperties();
    }

    public static synchronized DatabaseConfig getInstance() {
        if (instance == null) {
            instance = new DatabaseConfig();
        }
        return instance;
    }

    public void loadProperties() {
        Properties props = new Properties();
        try (InputStream input = getClass().getClassLoader().getResourceAsStream("database.properties")) {
            if (input != null) {
                props.load(input);
                this.url = props.getProperty("db.url");
                this.username = props.getProperty("db.username");
                this.password = props.getProperty("db.password");
            } else {
                // Fallback to default values
                this.url = "jdbc:mysql://localhost:3306/banking_app";
                this.username = "root";
                this.password = "";
            }
        } catch (IOException e) {
            throw new RuntimeException("Failed to load database properties", e);
        }
    }

    public Connection getConnection() throws SQLException {
        return DriverManager.getConnection(url, username, password);
    }
}
