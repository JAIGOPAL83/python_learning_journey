#!/usr/bin/env python3
"""
Python Variables and Data Types
This script demonstrates the basic usage of variables and different data types in Python.
"""

def demonstrate_numbers():
    """Demonstrate number data types and operations."""
    # Integer
    age = 25
    print(f"Age (integer): {age}")
    
    # Float
    height = 1.75
    print(f"Height (float): {height}")
    
    # Basic arithmetic
    print(f"Age + 5: {age + 5}")
    print(f"Height * 2: {height * 2}")

def demonstrate_strings():
    """Demonstrate string operations and methods."""
    # String declaration
    name = "Python"
    description = 'Programming Language'
    
    # String concatenation
    full_text = name + " " + description
    print(f"Concatenated string: {full_text}")
    
    # String methods
    print(f"Uppercase: {name.upper()}")
    print(f"Length of name: {len(name)}")
    print(f"Replace 'o' with '0': {name.replace('o', '0')}")

def demonstrate_booleans():
    """Demonstrate boolean operations."""
    is_python_fun = True
    is_difficult = False
    
    print(f"Is Python fun? {is_python_fun}")
    print(f"Is Python difficult? {is_difficult}")
    
    # Boolean operations
    print(f"AND operation: {is_python_fun and is_difficult}")
    print(f"OR operation: {is_python_fun or is_difficult}")
    print(f"NOT operation: {not is_difficult}")

def demonstrate_type_conversion():
    """Demonstrate type conversion between different data types."""
    # String to int
    str_number = "42"
    number = int(str_number)
    print(f"String to integer: {number} (type: {type(number)})")
    
    # Int to float
    float_number = float(number)
    print(f"Integer to float: {float_number} (type: {type(float_number)})")
    
    # Number to string
    back_to_string = str(number)
    print(f"Number to string: {back_to_string} (type: {type(back_to_string)})")

def main():
    """Main function to run all demonstrations."""
    print("\n=== Number Examples ===")
    demonstrate_numbers()
    
    print("\n=== String Examples ===")
    demonstrate_strings()
    
    print("\n=== Boolean Examples ===")
    demonstrate_booleans()
    
    print("\n=== Type Conversion Examples ===")
    demonstrate_type_conversion()

if __name__ == "__main__":
    main() 