#!/usr/bin/env python3
"""
Python Input and Output
This script demonstrates various ways to handle input and output in Python.
"""

def demonstrate_print():
    """Demonstrate different ways to use the print function."""
    print("=== Print Function Examples ===")
    
    # Basic print
    print("Hello, World!")
    
    # Print multiple items
    name = "Alice"
    age = 25
    print("Name:", name, "Age:", age)
    
    # Print with separator
    print("Python", "is", "awesome", sep=" -> ")
    
    # Print with end
    print("This line", end=" ")
    print("continues here")
    
    # Print formatted numbers
    price = 19.99
    quantity = 5
    print(f"\nPrice: ${price:.2f}")
    print(f"Total: ${price * quantity:.2f}")

def demonstrate_string_formatting():
    """Demonstrate different string formatting methods."""
    print("\n=== String Formatting Examples ===")
    
    name = "Bob"
    age = 30
    height = 1.75
    
    # Using f-strings (Python 3.6+)
    print(f"Name: {name}, Age: {age}, Height: {height:.2f}m")
    
    # Using .format()
    print("Name: {}, Age: {}, Height: {:.2f}m".format(name, age, height))
    
    # Using % operator (older style)
    print("Name: %s, Age: %d, Height: %.2fm" % (name, age, height))
    
    # Padding and alignment
    print(f"\n{'Left':<10}|{'Center':^10}|{'Right':>10}")
    print("-" * 32)
    
    # Number formatting
    number = 1234.5678
    print(f"\nNumber formatting:")
    print(f"Regular: {number}")
    print(f"2 decimal places: {number:.2f}")
    print(f"Scientific notation: {number:e}")
    print(f"Percentage: {number/100:.1%}")

def demonstrate_input():
    """Demonstrate how to get user input."""
    print("\n=== Input Examples ===")
    
    # Basic input
    print("\nNote: These are examples of input usage.")
    print("(The actual input calls are commented out to avoid blocking the script)")
    
    # Example of getting string input
    # name = input("Enter your name: ")
    # print(f"Hello, {name}!")
    
    # Example of getting numeric input
    # try:
    #     age = int(input("Enter your age: "))
    #     print(f"In 5 years, you'll be {age + 5}")
    # except ValueError:
    #     print("Please enter a valid number")
    
    # Example of input with default value
    def get_input_with_default(prompt, default):
        # return input(f"{prompt} [{default}]: ") or default
        return default  # For demonstration, always return default
    
    color = get_input_with_default("Enter your favorite color", "blue")
    print(f"Your favorite color is: {color}")

def main():
    """Main function to run all demonstrations."""
    demonstrate_print()
    demonstrate_string_formatting()
    demonstrate_input()

if __name__ == "__main__":
    main() 