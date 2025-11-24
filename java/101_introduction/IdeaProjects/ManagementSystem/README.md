# Management System

A Spring Boot REST API application for managing users with full CRUD operations, API documentation, and database integration.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [API Endpoints](#api-endpoints)
- [Database Configuration](#database-configuration)
- [API Documentation](#api-documentation)
- [Testing](#testing)
- [Development](#development)
- [Contributing](#contributing)

## 🔍 Overview

This Management System is a RESTful web service built with Spring Boot that provides comprehensive user management capabilities. It features a clean architecture with separate layers for controllers, services, repositories, and entities, following Spring Boot best practices.

## ✨ Features

- **User Management**: Complete CRUD operations for user entities
- **Search Functionality**: Search users by ID, email, first name, last name, or full name
- **REST API**: RESTful endpoints following HTTP standards
- **API Documentation**: Integrated Swagger UI for interactive API documentation
- **Database Integration**: H2 in-memory database with JPA/Hibernate
- **Data Validation**: Entity validation and error handling
- **Clean Architecture**: Layered architecture with separation of concerns

## 🛠 Tech Stack

- **Java**: 21
- **Framework**: Spring Boot 4.0.0
- **Database**: H2 (in-memory)
- **ORM**: Spring Data JPA / Hibernate
- **API Documentation**: SpringDoc OpenAPI (Swagger)
- **Build Tool**: Maven
- **Testing**: Spring Boot Test Framework

## 📁 Project Structure

```
src/
├── main/
│   ├── java/com/elainehello/ManagementSystem/
│   │   ├── ManagementSystemApplication.java    # Main application class
│   │   ├── config/
│   │   │   └── SwaggerConfig.java             # Swagger configuration
│   │   ├── controller/
│   │   │   └── UserController.java            # REST API endpoints
│   │   ├── model/entity/
│   │   │   └── User.java                      # User entity
│   │   ├── repository/
│   │   │   └── UserRepository.java            # Data access layer
│   │   └── service/
│   │       └── UserService.java               # Business logic layer
│   └── resources/
│       └── application.properties             # Application configuration
└── test/
    └── java/com/elainehello/ManagementSystem/
        └── ManagementSystemApplicationTests.java
```

## 🚀 Getting Started

### Prerequisites

- Java 21 or higher
- Maven 3.8+

### Installation & Running

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd ManagementSystem
   ```

2. **Build the project**

   ```bash
   ./mvnw clean install
   ```

3. **Run the application**

   ```bash
   ./mvnw spring-boot:run
   ```

4. **Access the application**
   - Application: http://localhost:9090
   - Swagger UI: http://localhost:9090/swagger-ui.html
   - H2 Database Console: http://localhost:9090/h2-console

## 📡 API Endpoints

### User Management

| Method | Endpoint                                                  | Description               |
| ------ | --------------------------------------------------------- | ------------------------- |
| POST   | `/users`                                                  | Create a new user         |
| GET    | `/users`                                                  | Get all users             |
| GET    | `/users/{id}`                                             | Get user by ID            |
| GET    | `/users/email?email={email}`                              | Get user by email         |
| GET    | `/users/firstname/{firstName}`                            | Get users by first name   |
| GET    | `/users/lastname/{lastName}`                              | Get users by last name    |
| GET    | `/users/search?firstName={firstName}&lastName={lastName}` | Search users by full name |
| DELETE | `/users/{id}`                                             | Delete user by ID         |

### Example Requests

**Create User:**

```bash
curl -X POST http://localhost:9090/users \
  -H "Content-Type: application/json" \
  -d '{
    "firstName": "John",
    "lastName": "Doe",
    "email": "john.doe@example.com"
  }'
```

**Get All Users:**

```bash
curl http://localhost:9090/users
```

**Search by Email:**

```bash
curl http://localhost:9090/users/email?email=john.doe@example.com
```

## 🗄️ Database Configuration

The application uses H2 in-memory database with the following configuration:

- **URL**: `jdbc:h2:mem:managementdb`
- **Username**: `sa`
- **Password**: (empty)
- **DDL**: `create-drop` (recreates schema on restart)

### User Entity Schema

```sql
CREATE TABLE User (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    email VARCHAR(255)
);
```

## 📖 API Documentation

Interactive API documentation is available through Swagger UI:

- **Swagger UI**: http://localhost:9090/swagger-ui.html
- **OpenAPI JSON**: http://localhost:9090/v3/api-docs

The API documentation includes:

- Complete endpoint descriptions
- Request/response schemas
- Try-it-out functionality
- Authentication details (if applicable)

## 🧪 Testing

Run the test suite:

```bash
# Run all tests
./mvnw test

# Run with coverage
./mvnw test jacoco:report
```

### Test Database

Tests use the same H2 in-memory database configuration for consistency and speed.

## 💻 Development

### Code Quality

The project includes:

- SonarQube integration for code quality analysis
- Maven compiler plugin for Java 21 compatibility

### Development Profile

For development with hot reload:

```bash
./mvnw spring-boot:run -Dspring-boot.run.profiles=dev
```

### Adding New Features

1. **Entity Layer**: Add new entities in `model/entity/`
2. **Repository Layer**: Create repositories in `repository/`
3. **Service Layer**: Implement business logic in `service/`
4. **Controller Layer**: Add REST endpoints in `controller/`
5. **Configuration**: Update configurations in `config/`

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

- **Developer**: Elaine Hello
- **Group ID**: com.elainehello
- **Artifact**: ManagementSystem

---

**Note**: This is a demo project for learning Spring Boot development. For production use, consider implementing additional features like authentication, input validation, error handling, and production database configuration.
