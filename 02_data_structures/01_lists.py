#!/usr/bin/env python3
"""
Python Lists
This script demonstrates the creation, manipulation, and operations on Python lists.
"""

def demonstrate_list_creation():
    """Demonstrate different ways to create lists."""
    print("=== List Creation ===")
    
    # Empty list
    empty_list = []
    print(f"Empty list: {empty_list}")
    
    # List with initial values
    numbers = [1, 2, 3, 4, 5]
    print(f"Number list: {numbers}")
    
    # Mixed type list
    mixed = [1, "hello", 3.14, True]
    print(f"Mixed type list: {mixed}")
    
    # List from range
    range_list = list(range(5))
    print(f"List from range: {range_list}")
    
    # List from string
    char_list = list("Python")
    print(f"List from string: {char_list}")

def demonstrate_list_operations():
    """Demonstrate basic list operations."""
    print("\n=== List Operations ===")
    
    fruits = ["apple", "banana", "cherry"]
    print(f"Original list: {fruits}")
    
    # Accessing elements
    print(f"First fruit: {fruits[0]}")
    print(f"Last fruit: {fruits[-1]}")
    
    # Slicing
    numbers = [0, 1, 2, 3, 4, 5]
    print(f"\nOriginal numbers: {numbers}")
    print(f"First three numbers: {numbers[:3]}")
    print(f"Last three numbers: {numbers[-3:]}")
    print(f"Every second number: {numbers[::2]}")
    print(f"Reversed list: {numbers[::-1]}")

def demonstrate_list_methods():
    """Demonstrate common list methods."""
    print("\n=== List Methods ===")
    
    fruits = ["apple", "banana"]
    print(f"Original list: {fruits}")
    
    # append: Add single element
    fruits.append("cherry")
    print(f"After append: {fruits}")
    
    # extend: Add multiple elements
    fruits.extend(["date", "elderberry"])
    print(f"After extend: {fruits}")
    
    # insert: Add element at specific position
    fruits.insert(1, "blueberry")
    print(f"After insert: {fruits}")
    
    # remove: Remove first occurrence
    fruits.remove("banana")
    print(f"After remove: {fruits}")
    
    # pop: Remove and return element
    popped = fruits.pop()
    print(f"Popped element: {popped}")
    print(f"After pop: {fruits}")
    
    # sort: Sort list in place
    fruits.sort()
    print(f"After sort: {fruits}")
    
    # reverse: Reverse list in place
    fruits.reverse()
    print(f"After reverse: {fruits}")

def demonstrate_list_comprehension():
    """Demonstrate list comprehensions."""
    print("\n=== List Comprehensions ===")
    
    # Simple comprehension
    squares = [x**2 for x in range(5)]
    print(f"Squares: {squares}")
    
    # Comprehension with condition
    even_squares = [x**2 for x in range(10) if x % 2 == 0]
    print(f"Even squares: {even_squares}")
    
    # Nested comprehension
    matrix = [[i+j for j in range(3)] for i in range(3)]
    print(f"Matrix: {matrix}")
    
    # Flattening a matrix
    flattened = [num for row in matrix for num in row]
    print(f"Flattened matrix: {flattened}")

def demonstrate_practical_examples():
    """Demonstrate practical examples using lists."""
    print("\n=== Practical Examples ===")
    
    # Finding unique elements while preserving order
    def unique_ordered(lst):
        seen = set()
        return [x for x in lst if not (x in seen or seen.add(x))]
    
    numbers = [1, 2, 2, 3, 4, 3, 5]
    print(f"Original list: {numbers}")
    print(f"Unique ordered: {unique_ordered(numbers)}")
    
    # Finding the second largest number
    def second_largest(lst):
        unique_sorted = sorted(set(lst), reverse=True)
        return unique_sorted[1] if len(unique_sorted) > 1 else None
    
    numbers = [5, 2, 8, 1, 9, 3, 8]
    print(f"\nNumbers: {numbers}")
    print(f"Second largest: {second_largest(numbers)}")
    
    # Merging and sorting lists
    def merge_sorted(lst1, lst2):
        return sorted(lst1 + lst2)
    
    list1 = [1, 3, 5]
    list2 = [2, 4, 6]
    print(f"\nList 1: {list1}")
    print(f"List 2: {list2}")
    print(f"Merged and sorted: {merge_sorted(list1, list2)}")

def main():
    """Main function to run all demonstrations."""
    demonstrate_list_creation()
    demonstrate_list_operations()
    demonstrate_list_methods()
    demonstrate_list_comprehension()
    demonstrate_practical_examples()

if __name__ == "__main__":
    main() 