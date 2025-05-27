#!/usr/bin/env python3
"""
Tuples vs Lists Comparison
This script demonstrates the key differences between tuples and lists.
"""

def demonstrate_mutability_difference():
    """Demonstrate the fundamental difference in mutability."""
    print("=== Mutability Difference ===")
    
    # List - Mutable
    my_list = [1, 2, 3]
    print("Original list:", my_list)
    
    # Lists can be modified
    my_list[0] = 100        # Modify element
    my_list.append(4)       # Add element
    my_list.remove(2)       # Remove element
    print("Modified list:", my_list)
    
    # Tuple - Immutable
    my_tuple = (1, 2, 3)
    print("\nOriginal tuple:", my_tuple)
    
    # Tuples cannot be modified
    print("Trying to modify tuple (will cause error):")
    try:
        my_tuple[0] = 100
    except TypeError as e:
        print(f"Error: {e}")

def demonstrate_performance_differences():
    """Demonstrate memory and performance characteristics."""
    print("\n=== Performance Differences ===")
    
    import sys
    
    # Memory size comparison
    list_example = [1, 2, 3, 4, 5]
    tuple_example = (1, 2, 3, 4, 5)
    
    print(f"List size in memory: {sys.getsizeof(list_example)} bytes")
    print(f"Tuple size in memory: {sys.getsizeof(tuple_example)} bytes")
    
    # Creation speed comparison
    from timeit import timeit
    
    list_creation = timeit(stmt="[1, 2, 3, 4, 5]", number=1000000)
    tuple_creation = timeit(stmt="(1, 2, 3, 4, 5)", number=1000000)
    
    print(f"\nTime to create list 1M times: {list_creation:.4f} seconds")
    print(f"Time to create tuple 1M times: {tuple_creation:.4f} seconds")

def demonstrate_usage_cases():
    """Demonstrate common use cases for tuples vs lists."""
    print("\n=== Usage Cases ===")
    
    # Tuples as dictionary keys (immutable)
    coordinate_map = {
        (0, 0): "Origin",
        (1, 0): "Right",
        (0, 1): "Up"
    }
    print("Dictionary with tuple keys:", coordinate_map)
    
    try:
        # This will fail - lists can't be dictionary keys
        invalid_dict = {[0, 0]: "Origin"}
    except TypeError as e:
        print("\nTrying to use list as dict key:")
        print(f"Error: {e}")
    
    # Multiple return values (naturally a tuple)
    def get_dimensions():
        return (1920, 1080)  # Returns tuple
    
    # Tuple unpacking
    width, height = get_dimensions()
    print(f"\nUnpacked dimensions: {width}x{height}")
    
    # Named tuples for structured data
    from collections import namedtuple
    Point = namedtuple('Point', ['x', 'y'])
    p = Point(x=3, y=4)
    print(f"\nNamed tuple example: {p}")
    print(f"Access by name: p.x = {p.x}, p.y = {p.y}")

def demonstrate_when_to_use():
    """Demonstrate when to use tuples vs lists."""
    print("\n=== When to Use Each ===")
    
    # Use tuples for:
    coordinates = (3, 4)        # Coordinates (x,y)
    rgb_color = (255, 128, 0)  # Color values
    date = (2024, 3, 14)       # Date (year, month, day)
    
    print("Tuples for fixed-length, immutable data:")
    print(f"- Coordinates: {coordinates}")
    print(f"- RGB Color: {rgb_color}")
    print(f"- Date: {date}")
    
    # Use lists for:
    shopping_list = ["apple", "banana", "orange"]  # Collection that changes
    scores = [98, 87, 95, 92]                     # Series of values
    queue = ["task1", "task2", "task3"]           # Queue/Stack operations
    
    print("\nLists for mutable collections:")
    print(f"- Shopping list: {shopping_list}")
    print(f"- Scores: {scores}")
    print(f"- Task queue: {queue}")

def main():
    """Main function to run all demonstrations."""
    demonstrate_mutability_difference()
    demonstrate_performance_differences()
    demonstrate_usage_cases()
    demonstrate_when_to_use()

if __name__ == "__main__":
    main() 