#!/usr/bin/env python3
"""
Practice exercises for advanced sorting operations.
Focus on custom sorting, multiple criteria, and sorting with classes.
"""

from dataclasses import dataclass
from typing import List, Tuple
from datetime import datetime

@dataclass
class Student:
    name: str
    grade: float
    age: int
    subjects: List[str]

@dataclass
class Transaction:
    date: datetime
    amount: float
    category: str
    description: str

def exercise_1(students: List[Student]) -> List[Student]:
    """
    Exercise 1: Multi-Criteria Student Sorting
    
    Task: Sort students by:
    1. Grade (descending)
    2. Age (ascending)
    3. Name (alphabetically)
    
    Example input:
    [
        Student('Alice', 85.5, 20, ['Math', 'Physics']),
        Student('Bob', 85.5, 19, ['Chemistry']),
        Student('Charlie', 90.0, 20, ['Biology']),
        Student('David', 85.5, 20, ['Physics'])
    ]
    
    Expected output order: Charlie, Alice, David, Bob
    (First by grade desc, then age asc, then name asc)
    """
    # Your solution here
    # solution = sorted(
    #     students,
    #     key=lambda s: (-s.grade, s.age, s.name)
    # )
    solution = students
    
    return solution

def exercise_2(transactions: List[Transaction]) -> List[Tuple[str, float]]:
    """
    Exercise 2: Transaction Analysis
    
    Task: Return a list of tuples (category, total_amount) sorted by total amount
    in descending order, where total_amount is the sum of all transaction amounts
    in that category.
    
    Example input:
    [
        Transaction(datetime(2024, 1, 1), 100.0, 'Food', 'Grocery'),
        Transaction(datetime(2024, 1, 2), 50.0, 'Food', 'Restaurant'),
        Transaction(datetime(2024, 1, 3), 200.0, 'Transport', 'Flight'),
        Transaction(datetime(2024, 1, 4), 25.0, 'Transport', 'Taxi')
    ]
    
    Expected output: [('Food', 150.0), ('Transport', 225.0)]
    """
    # Your solution here
    # from collections import defaultdict
    # totals = defaultdict(float)
    # for t in transactions:
    #     totals[t.category] += t.amount
    # solution = sorted(
    #     [(cat, total) for cat, total in totals.items()],
    #     key=lambda x: -x[1]
    # )
    solution = []
    
    return solution

def exercise_3(words: List[str]) -> List[str]:
    """
    Exercise 3: Custom String Sorting
    
    Task: Sort strings by:
    1. Number of unique vowels (descending)
    2. Total length (descending)
    3. Alphabetically (ascending)
    
    Example input:
    ['hello', 'world', 'python', 'programming', 'code']
    
    Expected output:
    ['programming', 'python', 'hello', 'world', 'code']
    """
    # Your solution here
    # def count_unique_vowels(s: str) -> int:
    #     return len(set(c for c in s.lower() if c in 'aeiou'))
    # 
    # solution = sorted(
    #     words,
    #     key=lambda w: (-count_unique_vowels(w), -len(w), w)
    # )
    solution = words
    
    return solution

def exercise_4(matrix: List[List[int]]) -> List[List[int]]:
    """
    Exercise 4: Matrix Row Sorting
    
    Task: Sort the rows of a matrix based on:
    1. Sum of elements (descending)
    2. Maximum element (descending)
    3. Length of row (descending)
    
    Example input:
    [
        [1, 2, 3],
        [4, 5],
        [6],
        [1, 1, 1, 1]
    ]
    
    Expected output:
    [
        [4, 5],      # sum=9, max=5, len=2
        [1, 2, 3],   # sum=6, max=3, len=3
        [1, 1, 1, 1],# sum=4, max=1, len=4
        [6]          # sum=6, max=6, len=1
    ]
    """
    # Your solution here
    # solution = sorted(
    #     matrix,
    #     key=lambda row: (-sum(row), -max(row), -len(row))
    # )
    solution = matrix
    
    return solution

def check_exercise_1(func, test_data):
    """Helper function to check exercise 1 results."""
    result = func(test_data)
    print("\nTesting Exercise 1:")
    print("Result order:", [s.name for s in result])
    expected_order = ['Charlie', 'Alice', 'David', 'Bob']
    print("Expected order:", expected_order)
    print(f"{'✓ Correct!' if [s.name for s in result] == expected_order else '✗ Not quite right.'}")

def check_exercise_2(func, test_data):
    """Helper function to check exercise 2 results."""
    result = func(test_data)
    print("\nTesting Exercise 2:")
    print("Your output:", result)
    expected = [('Transport', 225.0), ('Food', 150.0)]
    print("Expected output:", expected)
    print(f"{'✓ Correct!' if result == expected else '✗ Not quite right.'}")

def check_exercise_3(func, test_data, expected):
    """Helper function to check exercise 3 results."""
    result = func(test_data)
    print("\nTesting Exercise 3:")
    print("Your output:", result)
    print("Expected output:", expected)
    print(f"{'✓ Correct!' if result == expected else '✗ Not quite right.'}")

def check_exercise_4(func, test_data, expected):
    """Helper function to check exercise 4 results."""
    result = func(test_data)
    print("\nTesting Exercise 4:")
    print("Your output:", result)
    print("Expected output:", expected)
    print(f"{'✓ Correct!' if result == expected else '✗ Not quite right.'}")

def main():
    """Run all exercises with test data."""
    # Test data for Exercise 1
    students = [
        Student('Alice', 85.5, 20, ['Math', 'Physics']),
        Student('Bob', 85.5, 19, ['Chemistry']),
        Student('Charlie', 90.0, 20, ['Biology']),
        Student('David', 85.5, 20, ['Physics'])
    ]
    check_exercise_1(exercise_1, students)
    
    # Test data for Exercise 2
    transactions = [
        Transaction(datetime(2024, 1, 1), 100.0, 'Food', 'Grocery'),
        Transaction(datetime(2024, 1, 2), 50.0, 'Food', 'Restaurant'),
        Transaction(datetime(2024, 1, 3), 200.0, 'Transport', 'Flight'),
        Transaction(datetime(2024, 1, 4), 25.0, 'Transport', 'Taxi')
    ]
    check_exercise_2(exercise_2, transactions)
    
    # Test data for Exercise 3
    words = ['hello', 'world', 'python', 'programming', 'code']
    expected_words = ['programming', 'python', 'hello', 'world', 'code']
    check_exercise_3(exercise_3, words, expected_words)
    
    # Test data for Exercise 4
    matrix = [
        [1, 2, 3],
        [4, 5],
        [6],
        [1, 1, 1, 1]
    ]
    expected_matrix = [
        [4, 5],
        [1, 2, 3],
        [1, 1, 1, 1],
        [6]
    ]
    check_exercise_4(exercise_4, matrix, expected_matrix)

if __name__ == "__main__":
    main() 