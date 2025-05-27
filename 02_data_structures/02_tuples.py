#!/usr/bin/env python3
"""
Python Tuples
This script demonstrates the creation, usage, and concepts of Python tuples.
"""

from collections import namedtuple
from typing import Tuple

def demonstrate_tuple_creation():
    """Demonstrate different ways to create tuples."""
    print("=== Tuple Creation ===")
    
    # Empty tuple
    empty_tuple = ()
    print(f"Empty tuple: {empty_tuple}")
    
    # Single element tuple (note the comma)
    single_tuple = (1,)
    print(f"Single element tuple: {single_tuple}")
    
    # Multiple element tuple
    numbers = (1, 2, 3, 4, 5)
    print(f"Number tuple: {numbers}")
    
    # Mixed type tuple
    mixed = (1, "hello", 3.14, True)
    print(f"Mixed type tuple: {mixed}")
    
    # Tuple packing
    packed = 1, 2, 3  # Parentheses are optional
    print(f"Packed tuple: {packed}")
    
    # Tuple from list
    list_to_tuple = tuple([1, 2, 3])
    print(f"Tuple from list: {list_to_tuple}")

def demonstrate_tuple_operations():
    """Demonstrate basic tuple operations."""
    print("\n=== Tuple Operations ===")
    
    coordinates = (3, 4)
    print(f"Original tuple: {coordinates}")
    
    # Accessing elements
    print(f"X coordinate: {coordinates[0]}")
    print(f"Y coordinate: {coordinates[-1]}")
    
    # Tuple unpacking
    x, y = coordinates
    print(f"Unpacked coordinates: x={x}, y={y}")
    
    # Multiple assignment with tuples
    (a, b), (c, d) = (1, 2), (3, 4)
    print(f"Multiple assignment: a={a}, b={b}, c={c}, d={d}")
    
    # Slicing
    numbers = (0, 1, 2, 3, 4, 5)
    print(f"\nOriginal numbers: {numbers}")
    print(f"First three numbers: {numbers[:3]}")
    print(f"Last three numbers: {numbers[-3:]}")
    print(f"Every second number: {numbers[::2]}")

def demonstrate_tuple_methods():
    """Demonstrate tuple methods and operations."""
    print("\n=== Tuple Methods ===")
    
    numbers = (1, 2, 2, 3, 4, 2)
    print(f"Tuple: {numbers}")
    
    # Count occurrences
    print(f"Count of 2: {numbers.count(2)}")
    
    # Find index
    print(f"Index of first 2: {numbers.index(2)}")
    
    # Length
    print(f"Length of tuple: {len(numbers)}")
    
    # Concatenation
    tuple1 = (1, 2)
    tuple2 = (3, 4)
    concatenated = tuple1 + tuple2
    print(f"\nConcatenated tuples: {concatenated}")
    
    # Repetition
    repeated = tuple1 * 3
    print(f"Repeated tuple: {repeated}")

def demonstrate_named_tuples():
    """Demonstrate named tuples from collections module."""
    print("\n=== Named Tuples ===")
    
    # Creating a named tuple class
    Point = namedtuple('Point', ['x', 'y'])
    
    # Creating named tuple instances
    p1 = Point(3, 4)
    p2 = Point(6, 8)
    
    print(f"Point 1: {p1}")
    print(f"X coordinate: {p1.x}")
    print(f"Y coordinate: {p1.y}")
    
    # Converting to dictionary
    point_dict = p1._asdict()
    print(f"As dictionary: {point_dict}")
    
    # Creating new instance with _replace
    p3 = p1._replace(x=10)
    print(f"New point with replaced x: {p3}")

def demonstrate_practical_examples():
    """Demonstrate practical examples using tuples."""
    print("\n=== Practical Examples ===")
    
    def minmax(numbers: list) -> Tuple[float, float]:
        """Return minimum and maximum of a sequence."""
        return (min(numbers), max(numbers))
    
    numbers = [5, 2, 8, 1, 9, 3]
    minimum, maximum = minmax(numbers)
    print(f"Numbers: {numbers}")
    print(f"Min: {minimum}, Max: {maximum}")
    
    # Using tuples for dictionary keys
    locations = {
        (40.7128, -74.0060): "New York",
        (51.5074, -0.1278): "London",
        (35.6762, 139.6503): "Tokyo"
    }
    
    print("\nCity Locations:")
    for coords, city in locations.items():
        print(f"{city}: {coords}")
    
    # Return multiple values from function
    def get_circle_info(radius: float) -> Tuple[float, float]:
        """Return area and circumference of a circle."""
        import math
        area = math.pi * radius ** 2
        circumference = 2 * math.pi * radius
        return area, circumference
    
    radius = 5
    area, circumference = get_circle_info(radius)
    print(f"\nCircle with radius {radius}:")
    print(f"Area: {area:.2f}")
    print(f"Circumference: {circumference:.2f}")

def main():
    """Main function to run all demonstrations."""
    demonstrate_tuple_creation()
    demonstrate_tuple_operations()
    demonstrate_tuple_methods()
    demonstrate_named_tuples()
    demonstrate_practical_examples()

if __name__ == "__main__":
    main() 