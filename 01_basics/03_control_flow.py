#!/usr/bin/env python3
"""
Python Control Flow
This script demonstrates control flow statements in Python including if/else, loops, and control statements.
"""

def demonstrate_if_statements():
    """Demonstrate if, elif, and else statements."""
    print("=== If Statement Examples ===")
    
    # Simple if-else
    age = 18
    if age >= 18:
        print("You are an adult")
    else:
        print("You are a minor")
    
    # if-elif-else chain
    score = 85
    print(f"\nScore: {score}")
    if score >= 90:
        print("Grade: A")
    elif score >= 80:
        print("Grade: B")
    elif score >= 70:
        print("Grade: C")
    else:
        print("Grade: F")
    
    # Nested if statements
    is_weekend = True
    is_sunny = True
    
    if is_weekend:
        if is_sunny:
            print("\nPerfect day for a picnic!")
        else:
            print("\nGood day for indoor activities")
    else:
        print("\nWork day!")

def demonstrate_while_loops():
    """Demonstrate while loops and control statements."""
    print("\n=== While Loop Examples ===")
    
    # Simple while loop
    count = 0
    while count < 5:
        print(f"Count is: {count}")
        count += 1
    
    # while loop with break
    print("\nWhile loop with break:")
    number = 0
    while True:
        if number >= 3:
            break
        print(f"Number is: {number}")
        number += 1
    
    # while loop with continue
    print("\nWhile loop with continue (skip even numbers):")
    count = -1
    while count < 4:
        count += 1
        if count % 2 == 0:  # Skip even numbers
            continue
        print(f"Count is: {count}")

def demonstrate_for_loops():
    """Demonstrate for loops and iterations."""
    print("\n=== For Loop Examples ===")
    
    # Iterating over a range
    print("Iterating over range(5):")
    for i in range(5):
        print(f"Index: {i}")
    
    # Iterating over a string
    print("\nIterating over a string:")
    for char in "Python":
        print(f"Character: {char}")
    
    # Using enumerate
    print("\nUsing enumerate:")
    fruits = ["apple", "banana", "cherry"]
    for index, fruit in enumerate(fruits):
        print(f"Index {index}: {fruit}")
    
    # Nested for loops
    print("\nNested for loops (multiplication table):")
    for i in range(1, 4):
        for j in range(1, 4):
            print(f"{i} x {j} = {i*j}")
        print()  # Empty line between rows

def main():
    """Main function to run all demonstrations."""
    demonstrate_if_statements()
    demonstrate_while_loops()
    demonstrate_for_loops()

if __name__ == "__main__":
    main() 