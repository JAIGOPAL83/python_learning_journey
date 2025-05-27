#!/usr/bin/env python3
"""
Python Basic Operations
This script demonstrates the basic operators and operations in Python.
"""

def arithmetic_operations():
    """Demonstrate arithmetic operators."""
    a = 10
    b = 3
    
    # Basic arithmetic
    print("=== Arithmetic Operations ===")
    print(f"Addition: {a} + {b} = {a + b}")
    print(f"Subtraction: {a} - {b} = {a - b}")
    print(f"Multiplication: {a} * {b} = {a * b}")
    print(f"Division: {a} / {b} = {a / b}")  # Returns float
    print(f"Floor Division: {a} // {b} = {a // b}")  # Returns int
    print(f"Modulus: {a} % {b} = {a % b}")  # Returns remainder
    print(f"Exponentiation: {a} ** {b} = {a ** b}")  # a to the power of b

def comparison_operations():
    """Demonstrate comparison operators."""
    x = 5
    y = 10
    
    print("\n=== Comparison Operations ===")
    print(f"Equal to: {x} == {y} is {x == y}")
    print(f"Not equal to: {x} != {y} is {x != y}")
    print(f"Greater than: {x} > {y} is {x > y}")
    print(f"Less than: {x} < {y} is {x < y}")
    print(f"Greater than or equal to: {x} >= {y} is {x >= y}")
    print(f"Less than or equal to: {x} <= {y} is {x <= y}")

def logical_operations():
    """Demonstrate logical operators."""
    a = True
    b = False
    
    print("\n=== Logical Operations ===")
    print(f"AND: {a} and {b} is {a and b}")
    print(f"OR: {a} or {b} is {a or b}")
    print(f"NOT: not {a} is {not a}")
    
    # Short-circuit evaluation
    print("\n=== Short-circuit Evaluation ===")
    x = 5
    print(f"True or (x/0) is {True or (x/0)}")  # Second part not evaluated
    print(f"False and (x/0) is {False and (x/0)}")  # Second part not evaluated

def assignment_operations():
    """Demonstrate assignment operators."""
    print("\n=== Assignment Operations ===")
    
    # Simple assignment
    x = 5
    print(f"Initial value: x = {x}")
    
    # Add and assign
    x += 3  # Same as: x = x + 3
    print(f"After x += 3: x = {x}")
    
    # Subtract and assign
    x -= 2  # Same as: x = x - 2
    print(f"After x -= 2: x = {x}")
    
    # Multiply and assign
    x *= 4  # Same as: x = x * 4
    print(f"After x *= 4: x = {x}")
    
    # Divide and assign
    x /= 2  # Same as: x = x / 2
    print(f"After x /= 2: x = {x}")

def main():
    """Main function to run all demonstrations."""
    arithmetic_operations()
    comparison_operations()
    logical_operations()
    assignment_operations()

if __name__ == "__main__":
    main() 