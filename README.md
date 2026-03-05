# Quick-Calc

A simple calculator application developed as part of the Advanced Software Engineering course (Lecture 3 — Software Engineering & Testing). This project demonstrates a multi-layered testing strategy and professional version control practices using Git and GitHub.

## Features

- **Addition** — Adds two numbers
- **Subtraction** — Subtracts two numbers
- **Multiplication** — Multiplies two numbers
- **Division** — Divides two numbers with graceful handling of division by zero
- **Clear (C)** — Resets the current input and result to zero

## Setup Instructions

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/swe-testing-assignment.git
   cd swe-testing-assignment
   ```

2. Install dependencies:
   ```bash
   pip install pytest
   ```

3. Run the application (interactive mode):
   ```bash
   python main.py
   ```

## How to Run Tests

Execute the full test suite with:

```bash
pytest
```

To run with verbose output:

```bash
pytest -v
```

To generate a coverage report:

```bash
pytest --cov=calculator
```

## Testing Framework Research

### Pytest vs Unittest

For this project, I evaluated two popular Python testing frameworks: **Pytest** and **Unittest** (the built-in testing module).

**Unittest** is Python's built-in testing framework, inspired by Java's JUnit. It uses a class-based approach with test methods prefixed by `test_`. Its main advantages are that it requires no installation (included in the standard library) and provides a familiar structure for developers coming from JUnit backgrounds. However, it requires more boilerplate code, has less intuitive assertion messages, and lacks powerful fixtures and plugins.

**Pytest** is a third-party testing framework that has become the de facto standard for Python testing. It supports both class-based and function-based tests, offers a simpler syntax with plain `assert` statements, and provides detailed failure messages automatically. Pytest's fixture system is more flexible than unittest's setup/teardown methods, and it has a rich ecosystem of plugins (e.g., pytest-cov for coverage, pytest-xdist for parallel execution). The main drawback is that it requires installation as an external dependency.

**Decision**: I chose **Pytest** for this project because its concise syntax reduces boilerplate, making tests easier to read and maintain. The detailed assertion introspection helps quickly identify failures, and the fixture system simplifies test setup. For a learning project focused on testing best practices, Pytest's modern approach and extensive documentation make it the better choice.
