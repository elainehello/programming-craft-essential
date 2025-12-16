# Login System

A secure login system built with Spring Boot, PostgreSQL, and Redis for session management.

## 🏗️ Architecture

This project follows a clean architecture pattern with clear separation of concerns:

```
src/main/java/com/elainehello/loginsystem/
├── api/auth/                 # REST API layer
│   ├── LoginController.java  # Login endpoint
│   ├── LogoutController.java # Logout endpoint
│   ├── LoginRequest.java     # Login request DTO
│   └── LoginResponse.java    # Login response DTO
├── service/auth/            # Business logic layer
│   ├── LoginService.java    # Authentication logic
│   └── SessionService.java  # Token management
├── repository/              # Data access layer
│   └── UserRepository.java  # User data operations
├── entity/                  # Data models
│   └── User.java           # User entity
├── config/                  # Configuration
│   ├── SecurityConfig.java  # Spring Security config
│   └── PasswordConfig.java  # Password encoder config
└── exception/               # Exception handling
    └── GlobalExceptionHandler.java
```

## 🚀 Features

- **User Authentication**: Email/password login with BCrypt encryption
- **Session Management**: Token-based authentication with configurable expiration
- **Input Validation**: Request validation with detailed error messages
- **Security**: Spring Security integration with CSRF protection disabled for API
- **Database**: PostgreSQL with JPA/Hibernate for user persistence
- **Testing**: Testcontainers integration for isolated testing
- **Exception Handling**: Global exception handler for consistent API responses

## 🛠️ Technology Stack

- **Framework**: Spring Boot 4.0.0
- **Security**: Spring Security
- **Database**: PostgreSQL
- **Cache/Session**: Redis
- **ORM**: JPA/Hibernate
- **Validation**: Jakarta Bean Validation
- **Testing**: JUnit 5, Testcontainers
- **Build Tool**: Maven

## 📋 Prerequisites

- Java 21
- PostgreSQL 12+
- Redis 6+
- Maven 3.6+

## 🔧 Setup & Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd loginsystem
```

### 2. Configure Database

Update [`application.properties`](src/main/resources/application.properties):

```properties
# Database Configuration
spring.datasource.url=jdbc:postgresql://localhost:5432/loginsystem
spring.datasource.username=your_username
spring.datasource.password=your_password

# Redis Configuration
spring.data.redis.host=localhost
spring.data.redis.port=6379
```

### 3. Create Database

```bash
sudo -u postgres createdb loginsystem
```

### 4. Run the application

```bash
./mvnw spring-boot:run
```

The application will start on `http://localhost:8080`

## 📡 API Endpoints

### Authentication

#### POST `/api/v1/auth/login`

Authenticate a user and return access token.

**Request:**

```json
{
  "email": "user@example.com",
  "password": "password123"
}
```

**Response:**

```json
{
  "access_token": "1-uuid-string",
  "expires_in": 3600
}
```

**Status Codes:**

- `200 OK` - Login successful
- `400 Bad Request` - Invalid credentials or validation errors
- `401 Unauthorized` - Authentication failed

#### POST `/api/v1/auth/logout`

Logout user and invalidate token.

**Headers:**

```
Authorization: Bearer <access_token>
```

**Response:**

```
200 OK
```

## 🗄️ Database Schema

### Users Table

```sql
CREATE TABLE users (
    id BIGSERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    active BOOLEAN NOT NULL DEFAULT true
);
```

## 🧪 Testing

### Run Tests

```bash
./mvnw test
```

### Test with cURL

```bash
# Login
curl -X POST http://localhost:8080/api/v1/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "password": "password123"
  }'

# Logout
curl -X POST http://localhost:8080/api/v1/auth/logout \
  -H "Authorization: Bearer <your-token>"
```

## 🔒 Security Features

- **Password Encryption**: BCrypt with salt rounds
- **Input Validation**: Email format, password strength validation
- **CSRF Protection**: Disabled for stateless API
- **Error Handling**: Consistent error responses without sensitive information leakage
- **Token Expiration**: Configurable session timeout (default: 1 hour)

## 📁 Key Components

### [`LoginService`](src/main/java/com/elainehello/loginsystem/service/auth/LoginService.java)

Handles user authentication logic:

- Email/password verification
- Password hash validation using BCrypt
- Token generation via SessionService

### [`SessionService`](src/main/java/com/elainehello/loginsystem/service/auth/SessionService.java)

Manages user sessions:

- Access token creation
- Token expiration handling
- Future: Redis integration for distributed sessions

### [`UserRepository`](src/main/java/com/elainehello/loginsystem/repository/UserRepository.java)

Data access layer:

- Find user by email
- Check email existence
- JPA integration

### [`GlobalExceptionHandler`](src/main/java/com/elainehello/loginsystem/exception/GlobalExceptionHandler.java)

Centralized exception handling:

- Validation error formatting
- Runtime exception handling
- Consistent API error responses

## 🚧 Roadmap

- [ ] User Registration endpoint
- [ ] JWT token implementation
- [ ] Redis session integration
- [ ] Email verification
- [ ] Password reset functionality
- [ ] Role-based authorization
- [ ] Rate limiting
- [ ] Refresh token mechanism
- [ ] API documentation with OpenAPI/Swagger

## 🔧 Configuration

### Application Properties

```properties
# Application
spring.application.name=loginsystem

# Database
spring.jpa.hibernate.ddl-auto=update
spring.jpa.show-sql=true

# Security
# (Configure additional security settings as needed)
```

## 🐳 Docker Support

### Using Testcontainers

The project includes [`TestcontainersConfiguration`](src/test/java/com/elainehello/loginsystem/TestcontainersConfiguration.java) for isolated testing with PostgreSQL containers.

### Run Tests with Testcontainers

```bash
./mvnw test
```

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License.

---

**Note**: This is a learning project demonstrating Spring Boot authentication patterns. For production use, consider additional security measures such as:

- JWT tokens with proper signing
- Rate limiting
- HTTPS enforcement
- Comprehensive logging
- Monitoring and alerting
