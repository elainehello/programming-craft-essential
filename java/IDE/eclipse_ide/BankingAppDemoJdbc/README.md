# Banking Application Demo - JDBC Implementation

A console-based banking application demonstrating **SOLID principles**, **layered architecture**, and **enterprise-level design patterns** using Java and JDBC.

## 🏗️ Architecture Overview

This application follows a **clean layered architecture** with strict separation of concerns:

```
┌─────────────────────────────────────────┐
│              Console UI                 │  ← User Interface Layer
├─────────────────────────────────────────┤
│             Service Layer               │  ← Business Logic
├─────────────────────────────────────────┤
│           Repository Layer              │  ← Data Access
├─────────────────────────────────────────┤
│            Database Layer               │  ← MySQL Database
└─────────────────────────────────────────┘
```

## 📦 Package Structure

```
org.elainehello.BankingAppDemoJdbc/
├── model/                    # Domain Models (SRP)
│   ├── Customer.java         # Customer entity
│   └── Transaction.java      # Transaction entity
├── dto/                      # Data Transfer Objects (SRP)
│   ├── TransferRequest.java  # Transfer operation data
│   └── CustomerRegistrationRequest.java
├── repository/               # Data Access Layer (DIP)
│   ├── Repository.java       # Base repository interface
│   ├── CustomerRepository.java
│   └── impl/                 # Repository implementations
├── service/                  # Business Logic Layer (ISP)
│   ├── BankingService.java   # Main banking operations
│   ├── AuthenticationService.java
│   ├── BalanceService.java
│   ├── TransferService.java
│   ├── validation/           # Validation Strategies (OCP)
│   │   ├── ValidationStrategyInterface.java
│   │   ├── BalanceValidationStrategy.java
│   │   ├── AmountValidationStrategy.java
│   │   ├── CustomerValidationStrategy.java
│   │   └── TransferValidationComposite.java
│   └── impl/                 # Service implementations
├── config/                   # Configuration Management
│   ├── DatabaseConfig.java  # Database connection & pooling
│   └── ApplicationContext.java # Dependency injection
├── exception/                # Custom Exception Handling
├── util/                     # Utility Classes
└── ui/                       # Console Interface
```

## 🎯 SOLID Principles Implementation

### **Single Responsibility Principle (SRP)**

- **Models**: Only represent data structures
- **DTOs**: Only transfer data between layers
- **Repositories**: Only handle data persistence
- **Services**: Each service handles one business domain

### **Open/Closed Principle (OCP)**

- **Validation System**: Add new validation rules without modifying existing code
- **Strategy Pattern**: `ValidationStrategyInterface` allows extending validation logic
- **Repository Pattern**: New data sources can be added through new implementations

### **Liskov Substitution Principle (LSP)**

- **Repository Interfaces**: Any implementation can substitute the interface
- **Service Interfaces**: All implementations honor the same contracts
- **Validation Strategies**: All strategies are interchangeable

### **Interface Segregation Principle (ISP)**

- **Focused Services**: `AuthenticationService`, `BalanceService`, `TransferService`
- **Small Interfaces**: Clients depend only on methods they use
- **Specific DTOs**: Each DTO serves a single purpose

### **Dependency Inversion Principle (DIP)**

- **High-level modules** depend on abstractions (interfaces)
- **Dependency Injection** through `ApplicationContext`
- **Configuration Management** abstracts infrastructure concerns

## 🛠️ Technology Stack

- **Java 17** - Programming Language
- **Maven** - Build Management
- **MySQL Connector/J** - Database Driver
- **HikariCP** - Connection Pooling
- **SLF4J + Logback** - Logging Framework
- **Hibernate Validator** - Bean Validation
- **JUnit 5** - Testing Framework

## 🏗️ Design Patterns Used

1. **Repository Pattern** - Data access abstraction
2. **Strategy Pattern** - Validation logic
3. **Composite Pattern** - Multiple validation strategies
4. **Singleton Pattern** - Database configuration
5. **Dependency Injection** - Service wiring
6. **DTO Pattern** - Data transfer between layers

## 🚀 Core Features

- **Account Creation** - Register new banking customers
- **User Authentication** - Secure login system
- **Balance Inquiry** - View account balance
- **Money Transfer** - Transfer funds between accounts
- **Transaction History** - Track all financial operations
- **Input Validation** - Comprehensive data validation
- **Error Handling** - Robust exception management
- **Logging** - Comprehensive application logging

## 🔧 Key Components

### **Validation System (Strategy Pattern)**

```java
// Extensible validation without code modification
ValidationComposite validator = new ValidationComposite();
validator.addStrategy(new BalanceValidationStrategy(repository));
validator.addStrategy(new AmountValidationStrategy());
validator.addStrategy(new CustomerValidationStrategy(repository));
```

### **Database Configuration (Singleton + DIP)**

```java
// Centralized database management with connection pooling
DatabaseConfig config = DatabaseConfig.getInstance();
Connection conn = config.getConnection();
```

### **Service Layer (ISP + DIP)**

```java
// Focused, injectable services
BankingService bankingService = context.getBankingService();
TransferService transferService = context.getTransferService();
```

## 🗃️ Database Schema

```sql
-- Core tables supporting the banking operations
customers (customer_id, username, password_hash, first_name, last_name, email, balance, created_at, updated_at)
transactions (transaction_id, from_customer_id, to_customer_id, amount, type, description, timestamp)
```

## ⚡ Architecture Benefits

- **Maintainability** - Clear separation of concerns
- **Testability** - Each layer can be tested independently
- **Extensibility** - New features can be added easily
- **Scalability** - Modular design supports growth
- **Reliability** - Robust error handling and validation
- **Performance** - Connection pooling and optimized queries

## 🔄 Data Flow

1. **UI Layer** captures user input
2. **Service Layer** applies business rules and validation
3. **Repository Layer** handles database operations
4. **Database Layer** persists/retrieves data
5. **Response flows back** through the same layers

## 🎯 Enterprise Patterns

- **Layered Architecture** for separation of concerns
- **Clean Code Principles** for maintainability
- **SOLID Principles** for robust design
- **Design Patterns** for proven solutions
- **Exception Handling** for reliability
- **Configuration Management** for flexibility

This architecture demonstrates professional-grade Java application design suitable for enterprise environments while maintaining simplicity and clarity.
