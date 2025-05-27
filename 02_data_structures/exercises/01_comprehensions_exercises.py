#!/usr/bin/env python3
"""
Practice exercises for advanced comprehensions.
Try to solve these exercises using comprehensions.
"""

def exercise_1():
    """
    Exercise 1: Nested List Comprehension
    
    Task: Given a list of strings, create a list of tuples where each tuple contains
    the string and its length, but only for strings with more than 3 characters.
    
    Expected output for example_words:
    [('python', 6), ('javascript', 10), ('code', 4)]
    """
    example_words = ['py', 'python', 'javascript', 'code', 'hi']
    
    # Your solution here
    # solution = [(word, len(word)) for word in example_words if len(word) > 3]
    solution = []
    
    return solution

def exercise_2():
    """
    Exercise 2: Dictionary Comprehension
    
    Task: Create a dictionary where keys are numbers from 1 to 5 and values are
    their cubes, but only for odd numbers.
    
    Expected output:
    {1: 1, 3: 27, 5: 125}
    """
    # Your solution here
    # solution = {x: x**3 for x in range(1, 6) if x % 2 != 0}
    solution = {}
    
    return solution

def exercise_3():
    """
    Exercise 3: Set Comprehension
    
    Task: Given two lists of numbers, create a set of tuples where:
    - First element is from list_a
    - Second element is from list_b
    - Sum of elements is even
    
    Expected output for example lists:
    {(1, 3), (2, 2), (3, 1)}
    """
    list_a = [1, 2, 3, 4]
    list_b = [1, 2, 3, 4]
    
    # Your solution here
    # solution = {(a, b) for a in list_a for b in list_b if (a + b) % 2 == 0}
    solution = set()
    
    return solution

def exercise_4():
    """
    Exercise 4: Nested Dictionary Comprehension
    
    Task: Given a list of words, create a dictionary where:
    - Keys are the lengths of words
    - Values are dictionaries containing the words of that length as keys
      and their reversed spelling as values
    
    Expected output for example_words:
    {3: {'cat': 'tac', 'dog': 'god'}, 
     5: {'hello': 'olleh', 'world': 'dlrow'}}
    """
    example_words = ['cat', 'dog', 'hello', 'world']
    
    # Your solution here
    # solution = {
    #     length: {word: word[::-1] for word in example_words if len(word) == length}
    #     for length in {len(word) for word in example_words}
    # }
    solution = {}
    
    return solution

def check_exercise(exercise_func, expected_output):
    """Helper function to check exercise results."""
    result = exercise_func()
    print(f"\nTesting {exercise_func.__name__}:")
    print(f"Your output: {result}")
    print(f"Expected output: {expected_output}")
    print(f"{'✓ Correct!' if result == expected_output else '✗ Not quite right.'}")

def main():
    """Run all exercises and check results."""
    # Exercise 1
    expected_1 = [('python', 6), ('javascript', 10), ('code', 4)]
    check_exercise(exercise_1, expected_1)
    
    # Exercise 2
    expected_2 = {1: 1, 3: 27, 5: 125}
    check_exercise(exercise_2, expected_2)
    
    # Exercise 3
    expected_3 = {(1, 3), (2, 2), (3, 1)}
    check_exercise(exercise_3, expected_3)
    
    # Exercise 4
    expected_4 = {
        3: {'cat': 'tac', 'dog': 'god'},
        5: {'hello': 'olleh', 'world': 'dlrow'}
    }
    check_exercise(exercise_4, expected_4)

if __name__ == "__main__":
    main() 