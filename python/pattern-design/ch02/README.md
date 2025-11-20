# Chapter 02: SOLID Principles

This directory contains Python examples demonstrating the five **SOLID principles** of object-oriented design. These principles form the foundation of maintainable, extensible, and robust software architecture.

## Overview: The SOLID Principles

**SOLID** is an acronym that represents five key principles:

- **S** - Single Responsibility Principle (SRP)
- **O** - Open-Closed Principle (OCP)
- **L** - Liskov Substitution Principle (LSP)
- **I** - Interface Segregation Principle (ISP)
- **D** - Dependency Inversion Principle (DIP)

---

## 🎯 Single Responsibility Principle (SRP)

### `srp.py`

**"A class should have only one reason to change"**

Demonstrates how to separate concerns by giving each class a single responsibility:

- `Report` class: Responsible only for report content and generation
- `ReportSaver` class: Responsible only for saving reports to files

```python
# Good separation of concerns
report = Report("content")
saver = ReportSaver(report)
saver.save_to_file("report.txt")
```

**Key Benefits:**

- Easier to understand and maintain
- Changes to saving logic don't affect report generation
- Each class has a clear, focused purpose

---

## 🔓 Open-Closed Principle (OCP)

### `ocp.py`

**"Software entities should be open for extension but closed for modification"**

Shows how to add new functionality without changing existing code:

- `Shape` protocol defines the interface
- New shapes can be added without modifying existing code
- `calculate_area()` function works with any shape

```python
# Adding a new shape doesn't require changing existing code
class Triangle:
    def area(self) -> float:
        return 0.5 * self.base * self.height
```

**Key Benefits:**

- Reduces risk of breaking existing functionality
- Enables easy extension of features
- Follows the protocol-based design pattern

---

## 🔄 Liskov Substitution Principle (LSP)

### `lsp.py` - ✅ Correct Implementation

**"Objects of a superclass should be replaceable with objects of a subclass without breaking functionality"**

Demonstrates proper LSP compliance:

- Both `EnglishGreeter` and `SpanishGreeter` properly implement the `Greeter` protocol
- Both can be used interchangeably in the `welcome()` function
- Contract is maintained: both return greeting strings

### `lsp_.py` - ✅ Another Good Example

Shows inheritance-based LSP compliance with birds:

- All bird subclasses properly override the `move()` method
- Each provides appropriate behavior for their type
- Full substitutability is maintained

### `lsp_violate.py` - ❌ LSP Violation Example

Shows what **NOT** to do:

- `SilentNotifier` violates the notification contract
- Breaks the expectation that notifiers actually notify users
- Demonstrates how LSP violations can break program correctness

**Key Benefits:**

- Ensures reliable polymorphism
- Maintains program correctness
- Enables confident use of inheritance hierarchies

---

## 🔧 Interface Segregation Principle (ISP)

### `isp.py`

**"Clients should not be forced to depend on interfaces they don't use"**

Demonstrates proper interface segregation:

- Separate protocols: `Printer`, `Scanner`, `Fax`
- `SimplePrinter` only implements what it needs (`Printer`)
- `AllInOnePrinter` can implement multiple protocols as needed

```python
# Good: Small, focused interfaces
def do_the_print(printer: Printer) -> None:  # Only needs print capability
    printer.print_document()
```

**Key Benefits:**

- No forced implementation of unused methods
- More flexible and maintainable code
- Clear separation of capabilities

---

## 🔀 Dependency Inversion Principle (DIP)

### `dip.py`

**"High-level modules should not depend on low-level modules. Both should depend on abstractions"**

Shows proper dependency inversion:

- `Notification` (high-level) depends on `MessageSender` protocol (abstraction)
- `Email` (low-level) implements the protocol
- Dependencies are injected, not hard-coded

```python
# Dependency injection in action
email = Email()  # Create concrete implementation
notif = Notification(sender=email)  # Inject dependency
notif.send("message")  # Use through abstraction
```

**Key Benefits:**

- Loose coupling between components
- Easy testing with mock objects
- Flexible architecture that supports change

---

## 🔄 Running the Examples

Each file can be executed independently to see the principles in action:

```bash
# Single Responsibility Principle
python srp.py

# Open-Closed Principle
python ocp.py

# Liskov Substitution Principle - Good examples
python lsp.py
python lsp_.py

# Liskov Substitution Principle - Violation example
python lsp_violate.py

# Interface Segregation Principle
python isp.py

# Dependency Inversion Principle
python dip.py
```

## 🎨 Design Patterns Foundation

These SOLID principles are essential for implementing design patterns effectively:

### How SOLID Enables Patterns:

- **SRP** → Strategy, Command, Observer patterns
- **OCP** → Decorator, Strategy, Template Method patterns
- **LSP** → Template Method, Strategy, State patterns
- **ISP** → Adapter, Facade, Bridge patterns
- **DIP** → Factory, Observer, Strategy patterns

### Common Anti-Patterns Avoided:

1. **God Objects** (violates SRP)
2. **Fragile Base Class** (violates LSP)
3. **Interface Pollution** (violates ISP)
4. **Tight Coupling** (violates DIP)
5. **Modification Cascade** (violates OCP)

## 🏗️ Architectural Benefits

Following SOLID principles leads to:

- **Maintainable Code**: Easy to modify and extend
- **Testable Code**: Dependencies can be easily mocked
- **Reusable Components**: Loosely coupled, focused classes
- **Robust Architecture**: Changes in one area don't break others
- **Team Productivity**: Clear responsibilities and interfaces

## 📚 Key Takeaways

1. **Each principle addresses specific design problems**
2. **They work together synergistically**
3. **Protocols/interfaces are crucial for flexibility**
4. **Dependency injection enables loose coupling**
5. **Think about "contracts" and "responsibilities"**
6. **Design for change and extension**

---

_These examples demonstrate how SOLID principles create the foundation for clean, maintainable, and extensible object-oriented code that forms the basis for effective design pattern implementation._
