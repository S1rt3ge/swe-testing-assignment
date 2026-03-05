# Testing Strategy

This document describes the testing approach for the Quick-Calc application, aligned with concepts from Lecture 3 — Software Engineering & Testing.

## Overview

The testing strategy focuses on verifying the core calculation logic and user interaction flows. Tests are organized into two categories: unit tests and integration tests.

## What Was Tested

- **Core arithmetic operations**: Addition, subtraction, multiplication, and division
- **Edge cases**: Division by zero, negative numbers, decimal numbers, and large numbers
- **User workflows**: Complete calculation sequences and clear functionality
- **State management**: Proper reset of calculator state after operations

## What Was Not Tested

- **UI rendering**: Visual elements and layout were not tested as the focus is on business logic
- **Performance**: Load times and response speeds were not measured
- **Security**: Input sanitization and potential injection attacks were not tested
- **Accessibility**: Keyboard navigation and screen reader compatibility were not tested

These areas were intentionally excluded as they are non-functional requirements outside the scope of this assignment.

## Lecture Concepts Applied

### The Testing Pyramid

The test suite follows the Testing Pyramid principle, which recommends having more low-level unit tests than high-level integration or end-to-end tests.

| Level | Count | Description |
|-------|-------|-------------|
| Unit Tests | 10 | Test individual methods in isolation |
| Integration Tests | 4 | Test interaction between components |

This 10:4 ratio reflects the pyramid's guidance: a broad base of fast, isolated unit tests with a smaller layer of integration tests that verify component interactions.

### Black-box vs White-box Testing

- **Unit Tests (White-box)**: Tests in `test_calculator.py` were written with knowledge of the internal implementation. Test cases target specific methods (`add`, `subtract`, `multiply`, `divide`) and verify their behavior based on the known logic.

- **Integration Tests (Black-box)**: Tests in `test_integration.py` treat the calculator as a black box. They simulate user actions (`enter_digit`, `set_operator`, `calculate`) without relying on internal state details, focusing on input-output behavior.

### Functional vs Non-Functional Testing

This project focuses exclusively on **functional testing** — verifying that the calculator performs its intended operations correctly. All tests validate specific behaviors:

- Correct calculation results
- Proper error handling for division by zero
- State reset after clear operation

**Non-functional testing** (performance, usability, security, scalability) was intentionally not included as the assignment focuses on functional correctness and testing fundamentals.

### Regression Testing

The test suite serves as a regression testing safety net for future development. When adding new features (e.g., memory functions, percentage calculations, or keyboard support), running `pytest` will immediately reveal if existing functionality has been broken.

To use this suite for regression testing:
1. Make code changes
2. Run `pytest` to execute all tests
3. If any test fails, the change introduced a regression that must be fixed

This approach ensures that bug fixes or new features do not inadvertently break existing functionality.

## Test Results Summary

| Test Name | Type | Status |
|-----------|------|--------|
| test_addition_positive_numbers | Unit | Pass |
| test_subtraction_positive_numbers | Unit | Pass |
| test_multiplication_positive_numbers | Unit | Pass |
| test_division_positive_numbers | Unit | Pass |
| test_division_by_zero | Unit | Pass |
| test_addition_negative_numbers | Unit | Pass |
| test_division_decimal_numbers | Unit | Pass |
| test_multiplication_large_numbers | Unit | Pass |
| test_subtraction_result_negative | Unit | Pass |
| test_addition_with_decimals | Unit | Pass |
| test_full_addition_workflow | Integration | Pass |
| test_clear_resets_display | Integration | Pass |
| test_chained_operations | Integration | Pass |
| test_division_by_zero_in_workflow | Integration | Pass |

## Running Tests

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run only unit tests
pytest test_calculator.py

# Run only integration tests
pytest test_integration.py
```
