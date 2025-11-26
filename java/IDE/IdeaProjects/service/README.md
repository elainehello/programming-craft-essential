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

### What's Inside the Native Executable?

The 113MB native executable is a **completely self-contained binary** that includes:

#### Core Runtime Components (~40MB)

- **Substrate VM**: GraalVM's lightweight runtime (replaces the JVM)
- **Garbage Collector**: Serial GC for memory management
- **Memory Management**: Heap and stack management
- **Thread Management**: Native threading support
- **JNI Support**: Java Native Interface for system calls

#### Application Framework (~35MB)

- **Spring Boot Framework**: Core Spring container, auto-configuration, and lifecycle management
- **Spring Data JDBC**: Database abstraction and repository implementations
- **Spring Web MVC**: Web framework, servlet container, and request handling
- **Embedded Tomcat**: Full web server (Catalina engine, connectors, JSP support)

#### Dependencies & Libraries (~25MB)

- **H2 Database Engine**: Complete embedded SQL database
- **PostgreSQL JDBC Driver**: Database connectivity
- **Jackson JSON**: Serialization/deserialization
- **Spring Boot Actuator**: Monitoring and management endpoints
- **HikariCP**: Connection pooling
- **Logging Framework**: SLF4J and Logback

#### Application Code & Resources (~8MB)

- **Your Application**: Compiled business logic
- **Configuration Files**: application.properties, SQL scripts
- **Static Resources**: Any bundled assets

#### Reflection Metadata & AOT (~5MB)

- **Pre-computed Reflection**: All reflection calls resolved at compile time
- **Native Image Metadata**: Configuration for native compilation
- **Ahead-of-Time Optimizations**: Pre-compiled and optimized code paths

### Size Comparison Analysis

```bash
# Check the native executable size
du -hs ./target/service
# Output: 113M

# Compare with JAR file
du -hs ./target/service-0.0.1-SNAPSHOT.jar
# Output: ~25M (but needs JVM)

# Typical JVM installation size
# OpenJDK 21: ~300-400MB
# Total JVM deployment: ~325-425MB
```

### Performance Benefits vs Size Trade-off

| Metric           | Native Image | JVM + JAR                |
| ---------------- | ------------ | ------------------------ |
| **File Size**    | 113MB        | ~350MB (JVM + JAR)       |
| **Startup Time** | ~50-100ms    | ~2-5 seconds             |
| **Memory Usage** | ~20-50MB     | ~100-200MB               |
| **Cold Start**   | Instant      | JVM warmup required      |
| **Distribution** | Single file  | JVM + JAR + dependencies |

### Why Native Images Are Worth It

1. **Deployment Simplicity**: Single executable file, no JVM installation needed
2. **Container Optimization**:

   ```dockerfile
   # Native image container
   FROM scratch
   COPY service /service
   ENTRYPOINT ["/service"]
   # Final image: ~115MB

   # vs JVM container
   FROM openjdk:21-jre
   COPY service.jar /app.jar
   ENTRYPOINT ["java", "-jar", "/app.jar"]
   # Final image: ~400-500MB
   ```

3. **Cloud & Serverless**: Perfect for AWS Lambda, Google Cloud Run, Azure Functions
4. **Microservices**: Faster scaling, lower resource consumption
5. **Edge Computing**: Suitable for resource-constrained environments

### Build Process Breakdown

The native compilation process includes:

1. **Analysis** (46.8s): Finding all reachable code paths

   - 24,088 reachable types (90.6% of total)
   - 38,614 reachable fields (64.7% of total)
   - 115,183 reachable methods (63.4% of total)

2. **Universe Building** (10.5s): Creating the closed world assumption
3. **Method Parsing/Inlining** (4.1s + 5.3s): Code optimizations
4. **Compilation** (49.7s): Converting to native machine code
5. **Image Creation** (10.6s): Final executable assembly

**Final breakdown:**

- **Code area**: 56.38MB (50.20%) - Your compiled application code
- **Image heap**: 51.80MB (46.12%) - Objects and resources
- **Other data**: 4.14MB (3.68%) - Metadata and runtime info

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

# Analyze native image size
./mvnw -Pnative native:compile -Dverbose
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
