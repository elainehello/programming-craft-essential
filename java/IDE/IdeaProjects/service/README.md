# Spring Boot Service with GraalVM Native Image

A Spring Boot REST API service demonstrating native compilation with GraalVM for fast startup times and reduced memory footprint.

## Features

- **Spring Boot 3.2.0** with Java 21
- **Spring Data JDBC** for database operations
- **H2 Database** for development and testing
- **PostgreSQL** support for production
- **GraalVM Native Image** compilation
- **RESTful API** with functional routing
- **Spring Boot Actuator** for monitoring

## Quick Start

### Prerequisites

- Java 21 (GraalVM CE 21 recommended for native compilation)
- Maven 3.6+
- SDKMAN (optional, for easy Java version management)

### Install GraalVM (if not already installed)

```bash
# Using SDKMAN
sdk install java 21-graalce
sdk use java 21-graalce

# Verify installation
java -version
native-image --version
```

### Build and Run

#### Standard JVM Mode

```bash
# Build the application
./mvnw clean compile

# Run tests
./mvnw test

# Run the application
./mvnw spring-boot:run
```

#### Native Image Mode

```bash
# Build native executable (requires GraalVM)
./mvnw -DskipTests -Pnative native:compile

# Run the native executable
./target/service
```

## Project Structure

```
service/
├── src/
│   ├── main/
│   │   ├── java/com/elainehello/service/
│   │   │   ├── ServiceApplication.java    # Main application class
│   │   │   ├── Customer.java              # Customer record
│   │   │   └── CustomerRepository.java    # Data repository
│   │   └── resources/
│   │       ├── application.properties     # Main config
│   │       ├── application-dev.properties # Dev profile config
│   │       ├── application-test.properties # Test config
│   │       ├── schema.sql                 # Database schema
│   │       └── data.sql                   # Sample data
│   └── test/
├── pom.xml                                # Maven configuration
└── README.md
```

## API Endpoints

| Method | Endpoint     | Description          |
| ------ | ------------ | -------------------- |
| GET    | `/customers` | Get all customers    |
| GET    | `/actuator`  | Spring Boot Actuator |

### Example Usage

```bash
# Get all customers
curl http://localhost:8081/customers

# Check application health
curl http://localhost:8081/actuator/health
```

## Database Configuration

### Development (H2 In-Memory)

- **URL**: `jdbc:h2:mem:devdb`
- **Console**: http://localhost:8081/h2-console (when enabled)
- **Username**: `sa`
- **Password**: (empty)

### Testing (H2 In-Memory)

- **URL**: `jdbc:h2:mem:testdb`
- **Username**: `sa`
- **Password**: (empty)

### Production (PostgreSQL)

Configure in `application.properties` or environment variables:

```properties
spring.datasource.url=jdbc:postgresql://localhost:5432/servicedb
spring.datasource.username=myuser
spring.datasource.password=mypassword
```

## GraalVM Native Image

### Why Use Native Images?

1. **Fast Startup**: Milliseconds vs seconds
2. **Lower Memory Usage**: No JVM overhead
3. **Self-Contained**: No Java runtime required
4. **Container Friendly**: Smaller images, faster cold starts

### Performance Comparison

```bash
# Native executable startup
time ./target/service
# Typical startup: ~50-100ms

# JVM startup
time java -jar target/service-0.0.1-SNAPSHOT.jar
# Typical startup: ~2-5 seconds
```

### File Sizes

- **Native executable**: ~112MB (includes everything)
- **JAR file**: ~25MB (requires JVM)
- **JVM + JAR total**: ~200MB+ (JVM installation + JAR)

### Build Process Breakdown

The native compilation process includes:

1. **Analysis**: Finding all reachable code
2. **Universe Building**: Creating the closed world
3. **Method Parsing/Inlining**: Optimizations
4. **Compilation**: Native code generation
5. **Image Creation**: Final executable

## Profiles

### Development Profile (`dev`)

- H2 in-memory database
- H2 console enabled
- Debug logging
- Hot reload with DevTools

### Test Profile (`test`)

- H2 in-memory database
- No H2 console
- Test-specific configurations

### Production Profile

- PostgreSQL database
- Optimized logging
- Security configurations

## Dependencies

### Core Dependencies

- `spring-boot-starter-web`: Web framework
- `spring-boot-starter-data-jdbc`: Database access
- `spring-boot-starter-actuator`: Monitoring endpoints

### Database Dependencies

- `h2`: Embedded database for dev/test
- `postgresql`: PostgreSQL driver for production

### Build Dependencies

- `native-maven-plugin`: GraalVM native compilation
- `spring-boot-maven-plugin`: Spring Boot packaging

## Troubleshooting

### Common Issues

1. **"release 25 is not found"**

   - Solution: Use Java 21, not Java 25 (which doesn't exist)

2. **"Cannot load driver class: org.h2.Driver"**

   - Solution: Ensure H2 dependency has `runtime` scope

3. **"'gu' tool was not found"**
   - Solution: Install GraalVM (not regular OpenJDK)

### Useful Commands

```bash
# Check Java version
java -version

# Check Maven version
./mvnw -version

# Clean build
./mvnw clean

# Skip tests
./mvnw -DskipTests package

# Run with specific profile
./mvnw spring-boot:run -Dspring-boot.run.profiles=dev
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass
6. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).
