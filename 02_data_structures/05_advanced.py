#!/usr/bin/env python3
"""
Python Advanced Data Structure Operations
This script demonstrates advanced operations and combinations of Python data structures.
"""

from collections import defaultdict, Counter, deque
from typing import List, Dict, Set, Tuple
import heapq
from dataclasses import dataclass
from datetime import datetime

def demonstrate_advanced_comprehensions():
    """Demonstrate advanced comprehension techniques."""
    print("=== Advanced Comprehensions ===")
    
    # Nested list comprehension
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flattened = [num for row in matrix for num in row]
    print(f"Flattened matrix: {flattened}")
    
    # Conditional list comprehension
    numbers = [-4, -2, 0, 2, 4]
    abs_even = [x for x in numbers if x % 2 == 0 if x > 0]
    print(f"Positive even numbers: {abs_even}")
    
    # Dictionary comprehension with zip
    keys = ['a', 'b', 'c']
    values = [1, 2, 3]
    squared_dict = {k: v**2 for k, v in zip(keys, values)}
    print(f"Squared dictionary: {squared_dict}")
    
    # Set comprehension with complex condition
    words = ["hello", "world", "python", "programming"]
    long_words = {word.title() for word in words if len(word) > 5}
    print(f"Long words set: {long_words}")

def demonstrate_nested_structures():
    """Demonstrate operations with nested data structures."""
    print("\n=== Nested Data Structures ===")
    
    # Complex nested structure
    data = {
        'users': [
            {
                'id': 1,
                'name': 'Alice',
                'skills': {'Python', 'SQL'},
                'projects': [
                    {'name': 'Web App', 'status': 'completed'},
                    {'name': 'API', 'status': 'in_progress'}
                ]
            },
            {
                'id': 2,
                'name': 'Bob',
                'skills': {'Java', 'Python'},
                'projects': [
                    {'name': 'Mobile App', 'status': 'completed'}
                ]
            }
        ]
    }
    
    # Extract all unique skills
    all_skills = {
        skill 
        for user in data['users'] 
        for skill in user['skills']
    }
    print(f"All unique skills: {all_skills}")
    
    # Count completed projects per user
    completed_projects = {
        user['name']: len([
            p for p in user['projects'] 
            if p['status'] == 'completed'
        ])
        for user in data['users']
    }
    print(f"Completed projects per user: {completed_projects}")

def demonstrate_advanced_sorting():
    """Demonstrate advanced sorting techniques."""
    print("\n=== Advanced Sorting ===")
    
    @dataclass
    class Person:
        name: str
        age: int
        city: str
        
    # Sample data
    people = [
        Person("Alice", 30, "New York"),
        Person("Bob", 25, "Boston"),
        Person("Charlie", 35, "New York"),
        Person("David", 25, "Chicago")
    ]
    
    # Sort by multiple criteria
    sorted_people = sorted(
        people,
        key=lambda x: (x.age, x.name)  # Sort by age, then name
    )
    print("People sorted by age and name:")
    for person in sorted_people:
        print(f"  {person.name}: {person.age} years")
    
    # Group by city using defaultdict
    by_city = defaultdict(list)
    for person in people:
        by_city[person.city].append(person)
    
    print("\nPeople grouped by city:")
    for city, city_people in by_city.items():
        print(f"  {city}: {[p.name for p in city_people]}")

def demonstrate_priority_queue():
    """Demonstrate priority queue operations using heapq."""
    print("\n=== Priority Queue Operations ===")
    
    # Create a priority queue of tasks
    tasks = [
        (3, "Low priority task"),
        (1, "High priority task"),
        (2, "Medium priority task")
    ]
    heapq.heapify(tasks)
    
    print("Processing tasks by priority:")
    while tasks:
        priority, task = heapq.heappop(tasks)
        print(f"  Priority {priority}: {task}")

def demonstrate_custom_data_structure():
    """Demonstrate implementation of a custom data structure."""
    print("\n=== Custom Data Structure ===")
    
    class LRUCache:
        """Least Recently Used (LRU) cache implementation."""
        
        def __init__(self, capacity: int):
            self.capacity = capacity
            self.cache = {}
            self.usage = deque()
        
        def get(self, key: str) -> str:
            if key not in self.cache:
                return "Not found"
            
            # Move to most recently used
            self.usage.remove(key)
            self.usage.append(key)
            return self.cache[key]
        
        def put(self, key: str, value: str) -> None:
            if key in self.cache:
                self.usage.remove(key)
            elif len(self.cache) >= self.capacity:
                # Remove least recently used
                oldest = self.usage.popleft()
                del self.cache[oldest]
            
            self.cache[key] = value
            self.usage.append(key)
    
    # Demonstrate LRU Cache
    cache = LRUCache(2)  # Cache with capacity 2
    cache.put("A", "Value A")
    cache.put("B", "Value B")
    print(f"Get A: {cache.get('A')}")
    cache.put("C", "Value C")  # This will remove B
    print(f"Get B: {cache.get('B')}")  # Should be "Not found"
    print(f"Get C: {cache.get('C')}")

def demonstrate_functional_operations():
    """Demonstrate functional programming operations on data structures."""
    print("\n=== Functional Operations ===")
    
    from functools import reduce
    
    # Map and filter with lambda
    numbers = [1, 2, 3, 4, 5]
    squared_evens = list(
        map(lambda x: x**2,
            filter(lambda x: x % 2 == 0, numbers))
    )
    print(f"Squared even numbers: {squared_evens}")
    
    # Reduce with lambda
    product = reduce(lambda x, y: x * y, numbers)
    print(f"Product of numbers: {product}")
    
    # Combining map, filter, reduce
    words = ["hello", "world", "python", "programming"]
    avg_word_length = reduce(
        lambda x, y: x + y,
        map(len, filter(lambda w: len(w) > 4, words))
    ) / len(list(filter(lambda w: len(w) > 4, words)))
    
    print(f"Average length of words longer than 4 chars: {avg_word_length:.2f}")

def demonstrate_practical_application():
    """Demonstrate a practical application combining multiple data structures."""
    print("\n=== Practical Application: Log Analysis ===")
    
    # Sample log entries
    log_entries = [
        "2024-03-14 10:00:00 ERROR Database connection failed",
        "2024-03-14 10:01:00 INFO Server started",
        "2024-03-14 10:01:30 WARNING High memory usage",
        "2024-03-14 10:02:00 ERROR Database connection failed",
        "2024-03-14 10:02:30 INFO Request processed",
        "2024-03-14 10:03:00 ERROR Network timeout"
    ]
    
    # Parse and analyze logs
    def analyze_logs(logs: List[str]) -> Dict[str, dict]:
        # Initialize data structures
        error_counts = Counter()
        error_times = defaultdict(list)
        severity_stats = defaultdict(int)
        
        for entry in logs:
            # Parse log entry
            timestamp_str, severity, *message = entry.split()
            timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d")
            message = " ".join(message)
            
            # Update statistics
            if severity == "ERROR":
                error_counts[message] += 1
                error_times[message].append(timestamp)
            severity_stats[severity] += 1
        
        return {
            "error_counts": dict(error_counts),
            "severity_stats": dict(severity_stats),
            "unique_errors": len(error_counts)
        }
    
    # Analyze logs
    analysis = analyze_logs(log_entries)
    
    print("Log Analysis Results:")
    print(f"  Total unique errors: {analysis['unique_errors']}")
    print("  Error counts:")
    for error, count in analysis['error_counts'].items():
        print(f"    {error}: {count}")
    print("  Severity distribution:")
    for severity, count in analysis['severity_stats'].items():
        print(f"    {severity}: {count}")

def main():
    """Main function to run all demonstrations."""
    demonstrate_advanced_comprehensions()
    demonstrate_nested_structures()
    demonstrate_advanced_sorting()
    demonstrate_priority_queue()
    demonstrate_custom_data_structure()
    demonstrate_functional_operations()
    demonstrate_practical_application()

if __name__ == "__main__":
    main() 