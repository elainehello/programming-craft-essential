# Login System

A secure authentication system built with Spring Boot, PostgreSQL, and Redis for session management.

## 🏗️ Architecture

```
src/main/java/com/elainehello/loginsystem/
├── api/auth/                    # REST API layer
│   ├── LoginController.java     # Login endpoint
│   ├── RegistrationController.java # Registration endpoint
│   ├── LogoutController.java    # Logout endpoint
│   ├── LoginRequest.java        # Auth request DTO (login & registration)
│   └── LoginResponse.java       # Login response DTO
├── service/auth/               # Business logic layer
│   ├── LoginService.java       # Authentication logic
│   ├── RegistrationService.java # User registration logic
│   └── SessionService.java     # Redis token management
├── repository/                 # Data access layer
│   └── UserRepository.java     # User data operations
├── entity/                     # Data models
│   └── User.java              # User entity with Lombok
├── config/                     # Configuration
│   ├── SecurityConfig.java     # Spring Security config
│   ├── PasswordConfig.java     # BCrypt password encoder
│   └── RedisConfig.java        # Redis template config
├── exception/                  # Error handling
│   └── GlobalExceptionHandler.java # Centralized exception handling
└── service/
    └── DataInitializer.java    # Test data creation
compose.yaml                    # Docker Compose services definition
```

## 🚀 Features

- **Complete Authentication Flow**: Registration → Login → Session Management → Logout
- **Security**: BCrypt password hashing, input validation, secure session tokens
- **Redis Session Management**: Token-based authentication with automatic expiration
- **Docker Compose Integration**: One-command development environment setup
- **Input Validation**: Comprehensive validation with detailed error responses
- **Global Exception Handling**: Consistent API error responses
- **Test Data**: Automatic test user creation for development

## 🛠️ Technology Stack

- **Framework**: Spring Boot 4.0.0
- **Security**: Spring Security with BCrypt
- **Database**: PostgreSQL with JPA/Hibernate
- **Session Store**: Redis with Spring Data Redis
- **Containerization**: Docker Compose
- **Validation**: Jakarta Bean Validation
- **Testing**: JUnit 5, Testcontainers
- **Build Tool**: Maven

## 📋 Prerequisites

- Java 21
- Docker & Docker Compose
- Maven 3.6+

## 🚀 Quick Start

```bash
# Clone and start
git clone <repository-url>
cd loginsystem

# Start application (Docker Compose auto-starts PostgreSQL & Redis)
./mvnw spring-boot:run
```

**That's it!** The application starts on `http://localhost:8080` with:

- PostgreSQL database automatically created
- Redis session store ready
- Test user: `test@example.com` / `password123`

## 🐳 Docker Compose Configuration

The [`compose.yaml`](compose.yaml) file defines the development infrastructure:

### **Purpose & Benefits**

- **Zero Setup**: No need to manually install PostgreSQL or Redis
- **Consistent Environment**: All developers use identical database versions
- **Automatic Lifecycle**: Services start/stop with your Spring Boot application
- **Data Persistence**: Database data survives container restarts via volumes
- **Isolation**: No conflicts with existing local database installations

### **Services Defined**

```yaml
services:
  postgres:
    image: postgres:15-alpine # Lightweight PostgreSQL
    environment:
      POSTGRES_USER: loginsystem # Database user
      POSTGRES_PASSWORD: password123 # Database password
      POSTGRES_DB: loginsystem # Database name
    ports:
      - "5432:5432" # Expose on localhost:5432
    volumes:
      - postgres_data:/var/lib/postgresql/data # Persistent storage

  redis:
    image: redis:7-alpine # Lightweight Redis
    ports:
      - "6379:6379" # Expose on localhost:6379
    volumes:
      - redis_data:/data # Persistent session data
```

### **Spring Boot Integration**

Thanks to `spring-boot-docker-compose` dependency:

- **Auto-Detection**: Spring Boot automatically discovers running containers
- **Auto-Configuration**: Database and Redis connections configured automatically
- **No Manual Setup**: No need to start containers manually
- **Smart Management**: Containers start only when needed

### **Development Workflow**

```bash
# Start development (containers auto-start)
./mvnw spring-boot:run

# Stop development (containers auto-stop)
# Ctrl+C

# Reset all data (fresh start)
docker compose down -v
./mvnw spring-boot:run
```

## 📡 API Endpoints

### **POST `/api/v1/auth/register`**

Create a new user account.

```json
{
  "email": "user@example.com",
  "password": "password123",
  "firstName": "John",
  "lastName": "Doe"
}
```

### **POST `/api/v1/auth/login`**

Authenticate and receive access token.

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

### **POST `/api/v1/auth/logout`**

Invalidate session token.

**Headers:** `Authorization: Bearer <access_token>`

## 🧪 Testing

```bash
# Run tests with Testcontainers
./mvnw test

# Test registration
curl -X POST http://localhost:8080/api/v1/auth/register \
  -H "Content-Type: application/json" \
  -d '{"email":"new@user.com","password":"password123","firstName":"New","lastName":"User"}'

# Test login
curl -X POST http://localhost:8080/api/v1/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","password":"password123"}'

# Test logout
curl -X POST http://localhost:8080/api/v1/auth/logout \
  -H "Authorization: Bearer <your-token>"
```

## 🔒 Security Features

- **Password Encryption**: BCrypt with automatic salt generation
- **Input Validation**: Email format, password strength, required fields
- **Session Security**: Redis-based token storage with automatic expiration
- **Error Handling**: No sensitive information in error responses
- **CSRF Protection**: Disabled for stateless API design

## 📁 Key Components

- **[`LoginService`](src/main/java/com/elainehello/loginsystem/service/auth/LoginService.java)**: User authentication with BCrypt verification
- **[`SessionService`](src/main/java/com/elainehello/loginsystem/service/auth/SessionService.java)**: Redis-based token management
- **[`RegistrationService`](src/main/java/com/elainehello/loginsystem/service/auth/RegistrationService.java)**: User account creation
- **[`GlobalExceptionHandler`](src/main/java/com/elainehello/loginsystem/exception/GlobalExceptionHandler.java)**: Centralized error handling

## 🚧 Roadmap

- [ ] JWT token implementation
- [ ] Email verification
- [ ] Password reset functionality
- [ ] Role-based authorization (RBAC)
- [ ] Rate limiting
- [ ] Refresh token mechanism
- [ ] OpenAPI/Swagger documentation
- [ ] Integration tests

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License.

---

**Note**: This is a learning project demonstrating modern Spring Boot authentication patterns with Docker Compose integration.
