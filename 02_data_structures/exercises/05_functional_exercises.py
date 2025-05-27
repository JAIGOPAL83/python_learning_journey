#!/usr/bin/env python3
"""
Practice exercises for functional programming operations with data structures.
Focus on using map, filter, reduce, and lambda functions.
"""

from typing import List, Dict, Any, Callable
from functools import reduce
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Product:
    name: str
    price: float
    category: str
    stock: int

def exercise_1(numbers: List[int]) -> List[int]:
    """
    Exercise 1: Chain of Operations
    
    Task: Given a list of integers, perform the following operations:
    1. Filter out negative numbers
    2. Square each remaining number
    3. Filter out numbers greater than 100
    4. Sort in descending order
    
    Example:
    Input: [-4, -2, 0, 2, 4, 8, 16]
    Output: [64, 16, 4]
    
    Requirements:
    - Use only map, filter, and lambda functions
    - No list comprehensions or explicit loops
    """
    # Your solution here
    # solution = sorted(
    #     filter(lambda x: x <= 100,
    #         map(lambda x: x**2,
    #             filter(lambda x: x >= 0, numbers))),
    #     reverse=True
    # )
    solution = numbers
    
    return solution

def exercise_2(text: str) -> Dict[str, int]:
    """
    Exercise 2: Word Analysis
    
    Task: Given a text string, create a dictionary with the following metrics:
    - word_count: Total number of words
    - avg_length: Average word length
    - long_words: Number of words longer than 5 characters
    - unique_words: Number of unique words (case-insensitive)
    
    Example:
    Input: "The quick brown fox jumps over the lazy dog"
    Output: {
        'word_count': 9,
        'avg_length': 4.0,
        'long_words': 3,
        'unique_words': 8
    }
    
    Requirements:
    - Use functional programming concepts (map, filter, reduce)
    - No explicit loops
    """
    # Your solution here
    # words = text.lower().split()
    # solution = {
    #     'word_count': len(words),
    #     'avg_length': reduce(lambda x, y: x + len(y), words, 0) / len(words),
    #     'long_words': len(list(filter(lambda x: len(x) > 5, words))),
    #     'unique_words': len(set(words))
    # }
    solution = {}
    
    return solution

def exercise_3(products: List[Product]) -> Dict[str, Any]:
    """
    Exercise 3: Product Analysis
    
    Task: Given a list of Product objects, compute the following:
    1. Total value of inventory (price * stock) per category
    2. Average price per category
    3. List of products with low stock (< 10) sorted by price
    
    Example:
    Input: [
        Product("Laptop", 1000, "Electronics", 5),
        Product("Mouse", 25, "Electronics", 15),
        Product("Notebook", 5, "Stationery", 100)
    ]
    Output: {
        'inventory_value': {'Electronics': 5375, 'Stationery': 500},
        'avg_price': {'Electronics': 512.5, 'Stationery': 5.0},
        'low_stock': ["Laptop"]
    }
    
    Requirements:
    - Use functional programming concepts
    - Minimize use of explicit loops
    """
    # Your solution here
    # from itertools import groupby
    # from operator import attrgetter
    # 
    # # Group products by category
    # by_category = {
    #     category: list(items)
    #     for category, items in groupby(
    #         sorted(products, key=attrgetter('category')),
    #         key=attrgetter('category')
    #     )
    # }
    # 
    # solution = {
    #     'inventory_value': {
    #         cat: sum(map(lambda p: p.price * p.stock, prods))
    #         for cat, prods in by_category.items()
    #     },
    #     'avg_price': {
    #         cat: sum(map(lambda p: p.price, prods)) / len(prods)
    #         for cat, prods in by_category.items()
    #     },
    #     'low_stock': sorted(
    #         [p.name for p in products if p.stock < 10],
    #         key=lambda name: next(p.price for p in products if p.name == name)
    #     )
    # }
    solution = {}
    
    return solution

def exercise_4(data: List[Dict[str, Any]], operations: List[Callable]) -> List[Any]:
    """
    Exercise 4: Pipeline Processing
    
    Task: Implement a data processing pipeline that applies a series of
    operations to a list of dictionaries. Each operation is a function that
    transforms the data in some way.
    
    Example:
    Input:
    data = [
        {'name': 'Alice', 'age': 30, 'score': 85},
        {'name': 'Bob', 'age': 25, 'score': 92},
        {'name': 'Charlie', 'age': 35, 'score': 78}
    ]
    operations = [
        lambda x: list(filter(lambda d: d['age'] > 25, x)),
        lambda x: list(map(lambda d: d['score'], x)),
        lambda x: reduce(lambda a, b: a + b, x) / len(x)
    ]
    
    Output: 81.5 (average score of people over 25)
    
    Requirements:
    - Implement using reduce to create a pipeline
    - Each operation should be a pure function
    """
    # Your solution here
    # solution = reduce(lambda acc, func: func(acc), operations, data)
    solution = data
    
    return solution

def check_exercise_1():
    """Test Exercise 1: Chain of Operations"""
    print("\nTesting Exercise 1: Chain of Operations")
    test_input = [-4, -2, 0, 2, 4, 8, 16]
    result = exercise_1(test_input)
    expected = [64, 16, 4]
    print(f"Input: {test_input}")
    print(f"Your output: {result}")
    print(f"Expected: {expected}")
    print(f"{'✓ Correct!' if result == expected else '✗ Not quite right.'}")

def check_exercise_2():
    """Test Exercise 2: Word Analysis"""
    print("\nTesting Exercise 2: Word Analysis")
    test_input = "The quick brown fox jumps over the lazy dog"
    result = exercise_2(test_input)
    expected = {
        'word_count': 9,
        'avg_length': 4.0,
        'long_words': 3,
        'unique_words': 8
    }
    print(f"Input: {test_input}")
    print(f"Your output: {result}")
    print(f"Expected: {expected}")
    print(f"{'✓ Correct!' if result == expected else '✗ Not quite right.'}")

def check_exercise_3():
    """Test Exercise 3: Product Analysis"""
    print("\nTesting Exercise 3: Product Analysis")
    test_input = [
        Product("Laptop", 1000, "Electronics", 5),
        Product("Mouse", 25, "Electronics", 15),
        Product("Notebook", 5, "Stationery", 100)
    ]
    result = exercise_3(test_input)
    expected = {
        'inventory_value': {'Electronics': 5375, 'Stationery': 500},
        'avg_price': {'Electronics': 512.5, 'Stationery': 5.0},
        'low_stock': ["Laptop"]
    }
    print(f"Your output: {result}")
    print(f"Expected: {expected}")
    print(f"{'✓ Correct!' if result == expected else '✗ Not quite right.'}")

def check_exercise_4():
    """Test Exercise 4: Pipeline Processing"""
    print("\nTesting Exercise 4: Pipeline Processing")
    test_data = [
        {'name': 'Alice', 'age': 30, 'score': 85},
        {'name': 'Bob', 'age': 25, 'score': 92},
        {'name': 'Charlie', 'age': 35, 'score': 78}
    ]
    test_operations = [
        lambda x: list(filter(lambda d: d['age'] > 25, x)),
        lambda x: list(map(lambda d: d['score'], x)),
        lambda x: reduce(lambda a, b: a + b, x) / len(x)
    ]
    result = exercise_4(test_data, test_operations)
    expected = 81.5
    print(f"Your output: {result}")
    print(f"Expected: {expected}")
    print(f"{'✓ Correct!' if result == expected else '✗ Not quite right.'}")

def main():
    """Run all exercise tests."""
    check_exercise_1()
    check_exercise_2()
    check_exercise_3()
    check_exercise_4()

if __name__ == "__main__":
    main() 