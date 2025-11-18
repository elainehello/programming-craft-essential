# Chapter 01: Object-Oriented Design Principles

This directory contains Python examples demonstrating fundamental object-oriented design principles and best practices. Each file showcases a specific concept that forms the foundation of good software design.

## Files Overview

### 🔐 Encapsulation

#### `encapsulate.py`

Demonstrates **polymorphism** as a form of encapsulation using inheritance.

- Shows how different payment methods (`CreditCard`, `PayPal`) can be treated uniformly
- Implements a common interface through inheritance from `PaymentBase`
- Example of runtime polymorphism where method calls are resolved dynamically

```python
# Usage example from the file
payments = [CreditCard(200), PayPal(700)]
for payment in payments:
    payment.process_payment()  # Polymorphic behavior
```

#### `encapsulate_bis.py`

Shows **property-based encapsulation** using Python properties.

- Protects internal state with private attributes (`_radius`)
- Validates data through property setters
- Provides controlled access to object attributes

### 🔌 Interface Programming

#### `abstractclass.py`

Demonstrates the **"Program to Interfaces"** principle using Abstract Base Classes (ABC).

- Defines contracts that concrete classes must implement
- Uses `@abstractmethod` decorator to enforce implementation
- Shows formal interface definition using ABC

#### `interfaces.py`

Practical example of interface usage with different logger implementations.

- `Logger` ABC defines the contract for logging
- Multiple implementations: `ConsoleLogger`, `FileLogger`
- Shows how interfaces enable swappable implementations

#### `interfaces_bis.py`

Same logging example but using **Python Protocols** instead of ABC.

- More flexible approach using structural typing
- No explicit inheritance required
- Duck typing with compile-time checking

### 📋 Protocol-Based Design

#### `protocol.py`

Deep dive into **Python Protocols** for structural subtyping.

- Shows how objects are validated based on their structure, not inheritance
- Demonstrates duck typing: "If it walks like a duck and quacks like a duck..."
- Compile-time type safety without runtime overhead

### 🧩 Composition

#### `composition.py`

Illustrates **composition over inheritance** principle.

- `Car` class contains an `Engine` object rather than inheriting from it
- Shows "has-a" relationship vs "is-a" relationship
- More flexible than inheritance for building complex objects

### 🔗 Loose Coupling

#### `loose_coupling.py`

Demonstrates **dependency injection** for achieving loose coupling.

- Components interact through well-defined interfaces
- Easy to swap implementations without changing dependent code
- `MessageService` works with any object that implements the `Sender` protocol

## Key Concepts Demonstrated

### 1. **Encapsulation**

- Data hiding and controlled access
- Property decorators for validation
- Polymorphism through inheritance

### 2. **Interface Segregation**

- Program to interfaces, not implementations
- Abstract Base Classes vs Protocols
- Structural vs nominal typing

### 3. **Composition over Inheritance**

- Building objects through composition
- More flexible than class inheritance
- Better code reusability

### 4. **Dependency Injection**

- Loose coupling between components
- Easy testing and maintenance
- Flexible system architecture

## Running the Examples

Each file can be run independently:

```bash
python abstractclass.py
python composition.py
python encapsulate.py
python encapsulate_bis.py
python interfaces.py
python interfaces_bis.py
python loose_coupling.py
python protocol.py
```

## Design Patterns Foundation

These examples lay the groundwork for understanding more complex design patterns by demonstrating:

- **SOLID Principles** (especially Single Responsibility, Open/Closed, and Dependency Inversion)
- **Favor Composition over Inheritance**
- **Program to Interfaces**
- **Dependency Injection**

These fundamentals are essential for implementing design patterns like Strategy, Observer, Factory, and many others covered in subsequent chapters.

## Best Practices Highlighted

1. **Type Hints**: All examples use proper Python type annotations
2. **Documentation**: Clear docstrings explaining the purpose
3. **Separation of Concerns**: Each class has a single responsibility
4. **Testability**: Loosely coupled design makes testing easier
5. **Flexibility**: Easy to extend and modify without breaking existing code

---

_These examples serve as building blocks for more advanced design patterns and architectural concepts._
