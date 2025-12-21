# Login System

A secure authentication system built with Spring Boot, PostgreSQL, Redis, and Thymeleaf web interface.

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
├── controller/                 # Web interface layer
│   └── WebController.java      # Thymeleaf web pages
├── repository/                 # Data access layer
│   └── UserRepository.java     # User data operations
├── entity/                     # Data models
│   └── User.java              # User entity with Lombok
├── config/                     # Configuration
│   ├── SecurityConfig.java     # Spring Security config
│   ├── PasswordConfig.java     # BCrypt password encoder
│   ├── RedisConfig.java        # Redis template config
│   └── OpenApiConfig.java      # Swagger/OpenAPI configuration
├── exception/                  # Error handling
│   └── GlobalExceptionHandler.java # Centralized exception handling
├── service/
│   └── DataInitializer.java    # Test data creation
└── PortLogger.java            # Application port logger
src/main/resources/templates/    # Thymeleaf templates
├── index.html                  # Home page
├── login.html                  # Login form
└── register.html              # Registration form
compose.yaml                    # Docker Compose services definition
```

## 🚀 Features

- **Complete Authentication Flow**: Registration → Login → Session Management → Logout
- **Web Interface**: Thymeleaf-based login and registration forms
- **REST API**: JSON endpoints for programmatic access
- **Interactive Documentation**: Swagger UI for API testing
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
- **Web Interface**: Thymeleaf templating engine
- **API Documentation**: SpringDoc OpenAPI 3 (Swagger UI)
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
# Clone the repository
git clone <repository-url>
cd loginsystem

# Start Docker services
docker compose down
docker compose up -d

# Start application
./mvnw spring-boot:run
```

**That's it!** The application starts on `http://localhost:9090` with:

- PostgreSQL database automatically created
- Redis session store ready
- Test user: `test@example.com` / `password123`

## 🌐 Access Points

### **Web Interface**

- **🏠 Home Page**: `http://localhost:9090/`
- **🔐 Login Form**: `http://localhost:9090/login`
- **📝 Registration Form**: `http://localhost:9090/register`

### **API Documentation**

- **📖 Swagger UI**: `http://localhost:9090/swagger-ui/index.html`
- **📄 OpenAPI JSON**: `http://localhost:9090/v3/api-docs`

### **REST API Base**: `http://localhost:9090/api/v1/auth`

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
      - "5433:5432" # Expose on localhost:5433
    volumes:
      - postgres_data:/var/lib/postgresql/data # Persistent storage

  redis:
    image: redis:7-alpine # Lightweight Redis
    ports:
      - "6380:6379" # Expose on localhost:6380
    volumes:
      - redis_data:/data # Persistent session data
```

### **Development Workflow**

```bash
# Start Docker services
docker compose down
docker compose up -d

# Start application
./mvnw spring-boot:run

# Stop development
# Ctrl+C (stops application)
# docker compose down (stops containers)

# Reset all data (fresh start)
docker compose down -v
docker compose up -d
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

### **Run Tests**

```bash
./mvnw test
```

### **Web Interface Testing**

1. Go to `http://localhost:9090/`
2. Click "Register" to create a new account
3. Click "Login" to authenticate
4. Test the complete flow through the web forms

### **API Testing with Swagger**

1. Go to `http://localhost:9090/swagger-ui/index.html`
2. Expand the authentication endpoints
3. Click "Try it out" to test each endpoint
4. View request/response examples

### **curl Testing**

```bash
# Test registration
curl -X POST http://localhost:9090/api/v1/auth/register \
  -H "Content-Type: application/json" \
  -d '{"email":"new@user.com","password":"password123","firstName":"New","lastName":"User"}'

# Test login
curl -X POST http://localhost:9090/api/v1/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","password":"password123"}'

# Test logout
curl -X POST http://localhost:9090/api/v1/auth/logout \
  -H "Authorization: Bearer <your-token>"
```

## 🔒 Security Features

- **Password Encryption**: BCrypt with automatic salt generation
- **Input Validation**: Email format, password strength, required fields
- **Session Security**: Redis-based token storage with automatic expiration
- **CSRF Protection**: Configured for web forms, disabled for REST API
- **Error Handling**: No sensitive information in error responses
- **Secure Headers**: Spring Security default security headers

## 📁 Key Components

### **Authentication Services**

- **[`LoginService`](src/main/java/com/elainehello/loginsystem/service/auth/LoginService.java)**: User authentication with BCrypt verification
- **[`SessionService`](src/main/java/com/elainehello/loginsystem/service/auth/SessionService.java)**: Redis-based token management
- **[`RegistrationService`](src/main/java/com/elainehello/loginsystem/service/auth/RegistrationService.java)**: User account creation

### **Controllers**

- **[`WebController`](src/main/java/com/elainehello/loginsystem/controller/WebController.java)**: Thymeleaf web pages
- **[`LoginController`](src/main/java/com/elainehello/loginsystem/api/auth/LoginController.java)**: REST API login endpoint
- **[`RegistrationController`](src/main/java/com/elainehello/loginsystem/api/auth/RegistrationController.java)**: REST API registration endpoint
- **[`LogoutController`](src/main/java/com/elainehello/loginsystem/api/auth/LogoutController.java)**: REST API logout endpoint

### **Configuration & Utils**

- **[`OpenApiConfig`](src/main/java/com/elainehello/loginsystem/config/OpenApiConfig.java)**: Swagger documentation configuration
- **[`SecurityConfig`](src/main/java/com/elainehello/loginsystem/config/SecurityConfig.java)**: Security and CORS configuration
- **[`GlobalExceptionHandler`](src/main/java/com/elainehello/loginsystem/exception/GlobalExceptionHandler.java)**: Centralized error handling
- **[`PortLogger`](src/main/java/com/elainehello/loginsystem/PortLogger.java)**: Application startup port notification

## 🎨 Web Interface

The application includes a complete Thymeleaf-based web interface:

### **Templates**

- **[`index.html`](src/main/resources/templates/index.html)**: Welcome page with navigation
- **[`login.html`](src/main/resources/templates/login.html)**: User login form
- **[`register.html`](src/main/resources/templates/register.html)**: User registration form

### **Features**

- ✅ Responsive design
- ✅ Form validation with error messages
- ✅ AJAX API integration
- ✅ Success/error feedback
- ✅ Navigation between pages

## 🚧 Roadmap

- [x] ~~OpenAPI/Swagger documentation~~
- [x] ~~Thymeleaf web interface~~
- [x] ~~Docker Compose integration~~
- [x] ~~Redis session management~~
- [ ] JWT token implementation
- [ ] Email verification
- [ ] Password reset functionality
- [ ] Role-based authorization (RBAC)
- [ ] Rate limiting
- [ ] Refresh token mechanism
- [ ] Integration tests
- [ ] User profile management

## 🔧 Configuration

### **Application Properties**

```properties
# Server
server.port=9090

# Database (Docker Compose)
spring.datasource.url=jdbc:postgresql://localhost:5433/loginsystem
spring.datasource.username=loginsystem
spring.datasource.password=password123

# Redis (Docker Compose)
spring.data.redis.host=localhost
spring.data.redis.port=6380

# OpenAPI Documentation
springdoc.api-docs.path=/v3/api-docs
springdoc.swagger-ui.path=/swagger-ui.html
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

**Note**: This is a comprehensive learning project demonstrating modern Spring Boot authentication patterns with both web interface and REST API, Docker Compose integration, and interactive API documentation.
