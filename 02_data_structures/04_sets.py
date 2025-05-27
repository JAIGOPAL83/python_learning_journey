#!/usr/bin/env python3
"""
Python Sets
This script demonstrates the creation, manipulation, and operations on Python sets.
Sets are unordered collections of unique elements.
"""

def demonstrate_set_creation():
    """Demonstrate different ways to create sets."""
    print("=== Set Creation ===")
    
    # Empty set (note: empty_set = {} creates an empty dictionary)
    empty_set = set()
    print(f"Empty set: {empty_set}")
    
    # Set from list
    numbers = set([1, 2, 3, 2, 1])  # Duplicates are removed
    print(f"Set from list: {numbers}")
    
    # Set with literal notation
    fruits = {'apple', 'banana', 'orange', 'apple'}  # Duplicates are removed
    print(f"Set literal: {fruits}")
    
    # Set from string
    letters = set('hello')  # Creates set of unique characters
    print(f"Set from string: {letters}")
    
    # Set comprehension
    squares = {x**2 for x in range(5)}
    print(f"Set comprehension: {squares}")
    
    # Frozen set (immutable)
    frozen = frozenset([1, 2, 3])
    print(f"Frozen set: {frozen}")

def demonstrate_set_operations():
    """Demonstrate basic set operations."""
    print("\n=== Set Operations ===")
    
    # Create sample sets
    A = {1, 2, 3, 4, 5}
    B = {4, 5, 6, 7, 8}
    print(f"Set A: {A}")
    print(f"Set B: {B}")
    
    # Union (all elements from both sets)
    union = A | B  # or A.union(B)
    print(f"Union (A | B): {union}")
    
    # Intersection (elements common to both sets)
    intersection = A & B  # or A.intersection(B)
    print(f"Intersection (A & B): {intersection}")
    
    # Difference (elements in A but not in B)
    difference = A - B  # or A.difference(B)
    print(f"Difference (A - B): {difference}")
    
    # Symmetric difference (elements in either set but not both)
    symmetric_difference = A ^ B  # or A.symmetric_difference(B)
    print(f"Symmetric difference (A ^ B): {symmetric_difference}")
    
    # Subset and superset
    C = {1, 2}
    print(f"\nSet C: {C}")
    print(f"Is C subset of A?: {C <= A}")  # or C.issubset(A)
    print(f"Is A superset of C?: {A >= C}")  # or A.issuperset(C)
    
    # Disjoint sets (no common elements)
    D = {10, 11, 12}
    print(f"Set D: {D}")
    print(f"Are A and D disjoint?: {A.isdisjoint(D)}")

def demonstrate_set_methods():
    """Demonstrate common set methods."""
    print("\n=== Set Methods ===")
    
    # Create a set
    numbers = {1, 2, 3}
    print(f"Original set: {numbers}")
    
    # Add element
    numbers.add(4)
    print(f"After adding 4: {numbers}")
    
    # Add multiple elements
    numbers.update([5, 6, 7])
    print(f"After updating with [5, 6, 7]: {numbers}")
    
    # Remove element (raises error if not found)
    numbers.remove(7)
    print(f"After removing 7: {numbers}")
    
    # Discard element (no error if not found)
    numbers.discard(10)  # No error
    print(f"After discarding 10 (not present): {numbers}")
    
    # Pop random element
    popped = numbers.pop()
    print(f"Popped element: {popped}")
    print(f"After pop: {numbers}")
    
    # Clear set
    numbers.clear()
    print(f"After clear: {numbers}")

def demonstrate_practical_examples():
    """Demonstrate practical examples using sets."""
    print("\n=== Practical Examples ===")
    
    # Remove duplicates from a list while preserving order
    def unique_ordered(sequence):
        seen = set()
        return [x for x in sequence if not (x in seen or seen.add(x))]
    
    numbers = [1, 3, 2, 2, 4, 1, 5, 3]
    print(f"Original list: {numbers}")
    print(f"Unique ordered: {unique_ordered(numbers)}")
    
    # Find common characters in strings
    def common_chars(str1, str2):
        return set(str1) & set(str2)
    
    word1 = "hello"
    word2 = "world"
    print(f"\nCommon characters in '{word1}' and '{word2}': {common_chars(word1, word2)}")
    
    # Check if string is pangram (contains all alphabet letters)
    def is_pangram(text):
        alphabet = set('abcdefghijklmnopqrstuvwxyz')
        return alphabet <= set(text.lower())
    
    text = "The quick brown fox jumps over the lazy dog"
    print(f"\nIs '{text}' a pangram? {is_pangram(text)}")

def demonstrate_set_performance():
    """Demonstrate set performance characteristics."""
    print("\n=== Set Performance Examples ===")
    
    # Membership testing comparison
    import time
    
    # Create large list and set with same elements
    size = 10000
    numbers_list = list(range(size))
    numbers_set = set(range(size))
    
    # Test membership in list
    start_time = time.time()
    _ = size - 1 in numbers_list
    list_time = time.time() - start_time
    
    # Test membership in set
    start_time = time.time()
    _ = size - 1 in numbers_set
    set_time = time.time() - start_time
    
    print(f"Time to find element in list: {list_time:.6f} seconds")
    print(f"Time to find element in set: {set_time:.6f} seconds")
    
    # Memory usage comparison
    import sys
    list_size = sys.getsizeof(numbers_list)
    set_size = sys.getsizeof(numbers_set)
    
    print(f"\nMemory used by list: {list_size} bytes")
    print(f"Memory used by set: {set_size} bytes")

def main():
    """Main function to run all demonstrations."""
    demonstrate_set_creation()
    demonstrate_set_operations()
    demonstrate_set_methods()
    demonstrate_practical_examples()
    demonstrate_set_performance()

if __name__ == "__main__":
    main() 